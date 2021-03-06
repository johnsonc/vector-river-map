#!/usr/bin/env python

"""A very simple test + benchmark for serving vector tiles"""

import requests, time, grequests

urlbase = 'http://127.0.0.1:8000'
url = 'rivers/8/41/98.json'

# Try a single request
start = time.time()
r = requests.get("{}/{}".format(urlbase, url))
end = time.time()

assert r.status_code == 200
j = r.json()
assert j["type"] == "FeatureCollection"
assert len(j["features"]) > 0

print("Single request took {:.0f} ms".format(1000 * (end-start)))


# Try a batch of requests all at once
batch = ('rivers/8/42/99.json',
        'rivers/8/43/98.json',
        'rivers/8/41/99.json',
        'rivers/8/42/98.json',
        'rivers/8/42/97.json',
        'rivers/8/41/98.json',
        'rivers/8/40/99.json',
        'rivers/8/41/100.json',
        'rivers/8/42/100.json',
        'rivers/8/40/98.json',
        'rivers/8/43/97.json',
        'rivers/8/43/99.json',
        'rivers/8/40/100.json',
        'rivers/8/44/99.json',
        'rivers/8/44/98.json',
        'rivers/8/39/98.json',
        'rivers/8/39/99.json',
        'rivers/8/44/97.json',
        'rivers/8/39/100.json',
        'rivers/8/43/100.json',
        'rivers/8/39/97.json',
        'rivers/8/40/97.json',
        'rivers/8/44/100.json',
        'rivers/8/41/97.json')
urls = ("{}/{}".format(urlbase, url) for url in batch)
reqs = (grequests.get(u) for u in urls)
start = time.time()
resps = grequests.map(reqs)
end = time.time()

for r in resps:
    assert r.status_code == 200

print "{} requests in {:.0f}ms".format(len(batch), 1000 * (end-start))
