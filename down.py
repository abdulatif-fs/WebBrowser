import requests
# import re

# def getFilename_fromCd(cd):

#     if not cd:
#         return None
#     fname = re.findall('filename=(.+)', cd)
#     if len(fname) == 0:
#         return None
#     return fname[0]


url1 = 'http://google.com/favicon.ico'
r = requests.get(url1, allow_redirects=True)
print(r.status_code)
# filename = getFilename_fromCd(r.headers.get('content-disposition'))
# open(filename, 'wb').write(r.content)

filename = r.url[url1.rfind('/')+1:]