import requests
# import re

# def getFilename_fromCd(cd):

#     if not cd:
#         return None
#     fname = re.findall('filename=(.+)', cd)
#     if len(fname) == 0:
#         return None
#     return fname[0]
from requests.auth import HTTPBasicAuth

url1 = 'https://httpbin.org/basic-auth/user/pass'
r = requests.get(url1, allow_redirects=True, auth=HTTPBasicAuth("user", "pass"))
#print(r.status_code)
print(r)
# filename = getFilename_fromCd(r.headers.get('content-disposition'))
# open(filename, 'wb').write(r.content)

filename = r.url[url1.rfind('/')+1:]