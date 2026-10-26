import urllib.request

routes = [
    '/about',
    '/company/about',
    '/company/approach',
    '/company/quality',
    '/company/leadership',
    '/company/partners',
    '/company/careers',
    '/company/offices',
    '/services/consulting',
    '/services/enterprise-solutions',
    '/services/information-management',
    '/services/outsourcing',
    '/services/professional-services',
    '/solutions/sap',
    '/solutions/data-governance',
    '/solutions/specialized-suites',
    '/industries/healthcare',
    '/industries/manufacturing',
    '/industries/oil-gas',
    '/industries/education',
    '/industries/textile-apparel',
    '/industries/logistics',
    '/resources/insights',
    '/resources/perspectives',
    '/resources/faqs',
    '/resources/downloads'
]

print("=" * 70)
print(f"TESTING {len(routes)} CORPORATE ROUTES FOR STATUS, CARDS & JSON")
print("=" * 70)

all_ok = True
for r in routes:
    try:
        req = urllib.request.urlopen(f'http://127.0.0.1:8000{r}')
        c = req.read().decode('utf-8')
        vcard_count = c.count('class="vcard"')
        has_json = "sumeru-topics-data" in c
        has_modal = "vcard-floating-panel" in c
        status = req.status
        print(f"{r:35} -> {status} OK | vcards: {vcard_count:2} | JSON: {has_json} | Modal: {has_modal}")
        if status != 200 or vcard_count == 0 or not has_json or not has_modal:
            all_ok = False
    except Exception as e:
        print(f"{r:35} -> FAILED: {e}")
        all_ok = False

print("=" * 70)
print("ALL ROUTES VERIFIED SUCCESSFULLY!" if all_ok else "SOME ROUTES HAD ISSUES!")
print("=" * 70)
