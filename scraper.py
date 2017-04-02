import requests

for i in range(1, 8200):
    url = "https://tools.ietf.org/rfc/rfc%d.txt" % i
    print url
    r = requests.get(url)
    text = r.text
    if "tls" in text or "TLS" in text:
        with open("rfc%d.txt" % i, "w") as fh:
            fh.write(text)
        print "HIT"
    
