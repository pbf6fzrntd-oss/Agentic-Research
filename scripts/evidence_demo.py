"""Version 2 unique-reference scoring and a reproducible read-only evidence explorer."""
import argparse
import csv
import hashlib
import html
import io
import json
from collections import defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
from atomic import atomic_text
ROOT = Path(__file__).resolve().parent.parent
VERSION = 'unique-reference-v2'


def source_identity(citation):
    parts = urlsplit(citation.strip())
    if parts.scheme in ('https','http') and parts.netloc:
        return urlunsplit((parts.scheme.lower(),parts.netloc.lower(),parts.path.rstrip('/'),parts.query,''))
    return citation.strip()  # Hands-on logs have explicit non-URL references.


def date_bounds(value):
    # Preserve explicitly imprecise legacy observations; never invent a day.
    if value == '2026 (in-window, exact date not exposed by search)':return ('2026-01-01','2026-12-31','year')
    import calendar,re
    if re.fullmatch(r'\d{4}',value):return (value+'-01-01',value+'-12-31','year')
    if re.fullmatch(r'\d{4}-\d{2}',value):
        year,month=map(int,value.split('-'));last=calendar.monthrange(year,month)[1]
        return (value+'-01',f'{value}-{last:02d}','month')
    day=date.fromisoformat(value).isoformat();return (day,day,'day')

def read_rows(path, required):
    with Path(path).open(encoding='utf-8',newline='') as stream:
        reader=csv.DictReader(stream)
        if not set(required)<=set(reader.fieldnames or []):
            raise ValueError('Missing CSV columns')
        rows=list(reader)
    for row in rows:
        if None in row or any(not isinstance(row.get(field),str) or not row[field].strip() for field in required):
            raise ValueError('Malformed/empty required CSV field')
    return rows


def rank(findings,scores):
    seen_ids=set();groups=defaultdict(list);score_map={}
    for score in scores:
        key=(score['domain'],score['theme'])
        if key in score_map:raise ValueError('Duplicate theme score key')
        for field in ['severity_score','cost_score','strategic_score']:
            value=score[field]
            if str(value) not in ['0','1','2','3']:raise ValueError('Rubric scores must be integers 0..3')
        score_map[key]=score
    for finding in findings:
        if finding['id'] in seen_ids:raise ValueError('Duplicate finding ID')
        seen_ids.add(finding['id'])
        if finding['source_type'] not in ['PRIMARY','SECONDARY']:raise ValueError('Invalid source classification')
        date_bounds(finding['date'])
        groups[(finding['domain'],finding['theme'])].append(finding)
    result=[]
    for key,items in groups.items():
        if key not in score_map:raise ValueError('Missing theme score')
        score=score_map[key];unique=len({source_identity(it['citation']) for it in items})
        value=sum(int(score[field]) for field in ['severity_score','cost_score','strategic_score'])
        result.append({**score,'mentions':len(items),'unique_references':unique,'value':value,'priority_score':unique*value,'window_start':min(date_bounds(it['date'])[0] for it in items),'window_end':max(date_bounds(it['date'])[1] for it in items),'imprecise_dates':sum(date_bounds(it['date'])[2]!='day' for it in items)})
    return sorted(result,key=lambda row:(-row['priority_score'],row['domain'],row['theme']))


def explorer(rows,findings):
    esc=html.escape
    content=[]
    for row in rows:
        evidence=[f for f in findings if (f['domain'],f['theme'])==(row['domain'],row['theme'])]
        details=[]
        for f in evidence:
            citation=esc(f['citation']);parts=urlsplit(f['citation'])
            link=f'<a href="{citation}" target="_blank" rel="noreferrer">{citation}</a>' if parts.scheme in ('http','https') and parts.netloc else citation
            details.append(f'<li data-type="{esc(f["source_type"])}"><b>{esc(f["title"])}</b> · {esc(f["source_type"])} · {esc(f["date"])}<p>{esc(f["note"])}</p>{link}</li>')
        content.append(f'<article data-domain="{esc(row["domain"])}"><h2>{esc(row["theme_label"])}</h2><p>{esc(row["domain"])} / {esc(row["theme"])} · Priority {row["priority_score"]} = {row["unique_references"]} unique references × rubric value {row["value"]}. {row["mentions"]} mentions.</p><p>Observation date bounds: {row["window_start"]} through {row["window_end"]}. Imprecise observations: {row["imprecise_dates"]}</p><p>Severity {row["severity_score"]}, cost {row["cost_score"]}, strategic {row["strategic_score"]} (each 0–3).</p><p>{esc(row["rationale"])}</p><details><summary>Inspect evidence ({len(evidence)})</summary><ul>{"".join(details)}</ul></details></article>')
    domains=''.join(f'<option>{esc(d)}</option>' for d in sorted({r['domain'] for r in rows}))
    return '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Agentic Research evidence explorer</title><style>body{font:17px system-ui;background:#f1f4f6;color:#162a34;margin:auto;max-width:1050px;padding:24px}article{background:white;padding:20px;margin:18px 0;border:1px solid #cad4dc;border-radius:10px}input,select{padding:12px;max-width:100%;margin:5px}li{margin:20px 0}a{overflow-wrap:anywhere}summary{cursor:pointer}label{display:inline-block}</style><h1>Agentic Research evidence explorer</h1><p>Version 2 counts unique citation references, not independent people or a population response rate. Scores are manual judgments. Cross-domain priorities are not directly comparable. Phase 2 extrapolations remain in the report and are not new observed evidence.</p><p>Fixed-input demonstration; no live refresh occurs here. Filters change visible evidence, not the full-cohort score.</p><label>Domain <select id="domain"><option value="">All domains</option>'''+domains+'''</select></label><label>Source type <select id="type"><option value="">All evidence</option><option>PRIMARY</option><option>SECONDARY</option></select></label><label>Theme / evidence search <input id="query" type="search"></label><p id="status" role="status"></p>'''+''.join(content)+'''<script>const domain=document.getElementById('domain'),type=document.getElementById('type'),query=document.getElementById('query');function filter(){let visible=0;document.querySelectorAll('article').forEach(a=>{const show=(!domain.value||a.dataset.domain===domain.value)&&a.textContent.toLowerCase().includes(query.value.toLowerCase());let evidence=0;a.querySelectorAll('li').forEach(li=>{li.hidden=!!type.value&&li.dataset.type!==type.value;if(!li.hidden)evidence++;});a.hidden=!show||!evidence;if(!a.hidden)visible++;});document.getElementById('status').textContent=visible+' themes shown';}domain.onchange=type.onchange=query.oninput=filter;filter();</script></html>'''


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,default=ROOT/'generated'/'v2');args=parser.parse_args()
    required=['id','domain','theme','source_type','title','citation','date','note']
    findings=read_rows(ROOT/'data/findings.csv',required)
    scores=read_rows(ROOT/'data/theme_scores.csv',['domain','theme','theme_label','severity_score','cost_score','strategic_score','rationale'])
    rows=rank(findings,scores)
    buffer=io.StringIO();writer=csv.DictWriter(buffer,fieldnames=list(rows[0]) if rows else ['domain','theme']);writer.writeheader();writer.writerows(rows)
    manifest={'methodology':VERSION,'finding_count':len(findings),'theme_count':len(rows),'observation_window':[min(date_bounds(f['date'])[0] for f in findings),max(date_bounds(f['date'])[1] for f in findings)],'imprecise_date_count':sum(date_bounds(f['date'])[2]!='day' for f in findings),'inputs':{name:hashlib.sha256((ROOT/'data'/name).read_bytes()).hexdigest() for name in ['findings.csv','theme_scores.csv']},'caveat':'Unique references are not independent respondents or population response rates.'}
    atomic_text(args.out/'ranked.csv',buffer.getvalue());atomic_text(args.out/'index.html',explorer(rows,findings));atomic_text(args.out/'manifest.json',json.dumps(manifest,indent=2,sort_keys=True)+'\n')
    print(f'{len(rows)} validated themes -> {args.out}/index.html')

if __name__=='__main__':main()
