# coding=UTF8

import requests, json

root = "http://localhost:5000"
headers = {'Accept': 'application/json', 'Content-type': 'application/json'}
s = requests.Session()
# s.auth = ('iolivie@rielcano.org', 'iolivie@rielcano.org')

data = {
    "email": "iolivie@rielcano.org",
    "password": "iolivie@rielcano.org"
}

r = s.post(root+"/user/login", data=json.dumps(data), headers=headers)

print(r.json())
print(r.cookies["session"])

# headers["Cookie"] = r.cookies["session"]

print(headers)



r = s.get(root+"/label/en", headers=headers)

print(r.json())




files = {'file': open('backend/test/sample.pdf', 'rb')}

r = s.post(root+"/document/upload_pdf", files=files)

print(r.text)
