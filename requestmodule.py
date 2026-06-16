# Requests Module for HTTPS Requests:---------------------------------


import requests

r = requests.get("https://pypi.org/project/requests/")
print(r.text)

url = "https://www.google.com/search?gs_ssp=eJzj4tTP1TdIsSw0zzJg9GJOL04CACXRBHg&q=gsb&rlz=1C1GCEA_enIN1064IN1064&oq=ghsbh&gs_lcrp=EgZjaHJvbWUqDAgBEC4YDRixAxiABDIGCAAQRRg5MgwIARAuGA0YsQMYgAQyCQgCEAAYDRiABDIMCAMQLhgNGIAEGOUEMg8IBBAuGA0YrwEYxwEYgAQyCQgFEAAYDRiABDIPCAYQLhgNGK8BGMcBGIAEMgkIBxAAGA0YgAQyCQgIEAAYDRiABNIBCDI4MDlqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8"
data = {
    "name": 4,
    "name1":5
}
r2 = requests.post(url=url, data=data)
print(r2.text)

