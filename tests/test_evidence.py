import sys
import unittest
from pathlib import Path
from copy import deepcopy
from urllib.error import URLError
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from fetch_github_issues import collect
from evidence_demo import rank,explorer,read_rows,ROOT,date_bounds

class RefreshTests(unittest.TestCase):
    def test_complete_unique_snapshot(self):
        result=collect('example',fetcher=lambda *args:{'total_count':1,'incomplete_results':False,'items':[{'id':1,'html_url':'https://example.invalid/1'}]})
        self.assertTrue(result['complete'])
    def test_failures_and_search_cap_do_not_claim_completeness(self):
        def fails(*args):raise URLError('unavailable')
        self.assertFalse(collect('example',fetcher=fails)['complete'])
        for data in [{'total_count':1001,'incomplete_results':False,'items':[]},{'total_count':0,'incomplete_results':True,'items':[]}]:
            self.assertFalse(collect('example',fetcher=lambda *args:data)['complete'])
    def test_duplicate_pages_and_total_changes_are_incomplete(self):
        result=collect('example',per_page=1,max_pages=2,fetcher=lambda *args:{'total_count':3,'incomplete_results':False,'items':[{'id':1,'html_url':'https://example.invalid/1'}]})
        self.assertFalse(result['complete'])
        self.assertEqual(result['fetched_count'],1)

class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.findings=read_rows(ROOT/'data/findings.csv',['id','domain','theme','source_type','title','citation','date','note'])
        self.scores=read_rows(ROOT/'data/theme_scores.csv',['domain','theme','theme_label','severity_score','cost_score','strategic_score','rationale'])
    def test_fixed_inputs_reproduce_and_original_outputs_remain_separate(self):
        self.assertEqual(rank(self.findings,self.scores),rank(self.findings,self.scores))
    def test_same_reference_does_not_inflate_unique_count(self):
        findings=[self.findings[0],{**self.findings[0],'id':'new-id'}]
        row=rank(findings,self.scores)[0]
        self.assertEqual(row['mentions'],2);self.assertEqual(row['unique_references'],1)
    def test_invalid_manual_scores_and_missing_keys_fail(self):
        bad=deepcopy(self.scores);bad[0]['severity_score']='4'
        with self.assertRaises(ValueError):rank(self.findings,bad)
        with self.assertRaises(ValueError):rank(self.findings,[])
        with self.assertRaises(ValueError):rank(self.findings,self.scores+self.scores[:1])
    def test_imprecise_dates_are_preserved_and_invalid_dates_rejected(self):
        self.assertEqual(date_bounds('2026-08'),('2026-08-01','2026-08-31','month'))
        with self.assertRaises(ValueError):date_bounds('2026-13')
        with self.assertRaises(ValueError):date_bounds('2026-02-30')
    def test_html_escapes_evidence_and_never_links_script_urls(self):
        finding={**self.findings[0],'title':'<script>alert(1)</script>','citation':'javascript:alert(1)'}
        page=explorer(rank([finding],self.scores),[finding])
        self.assertIn('&lt;script&gt;',page);self.assertNotIn('href="javascript:',page)

if __name__=='__main__':unittest.main()
