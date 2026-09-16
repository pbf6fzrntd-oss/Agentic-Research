---
description: Regenerate and (if already published) republish the visual pipeline dashboard
---
Run `python3 pipeline/crm.py dashboard` to regenerate `pipeline/dashboard.html` from the current `pipeline/contacts.csv`.

Then check `pipeline/dashboard_url.txt` for an existing artifact URL:
- If it exists and has a URL, republish in place with the Artifact tool, passing that URL so it updates the same page rather than creating a new one: `Artifact({ file_path: "pipeline/dashboard.html", url: "<the URL from dashboard_url.txt>" })`.
- If it doesn't exist yet, publish a new artifact with the Artifact tool and write the resulting URL to `pipeline/dashboard_url.txt` so future runs update it in place.

Report the URL back once done.
