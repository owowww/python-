import requests
r = requests.post("https://portal.oit.edu.tw/index.php?sid=CosQuery&QueryMode=O", data={'cos_smtr': '1081', 'cos_deptType': '1', 'cos_dept': 'GA3', 'cos_optionalType':'E'})
print(r)
print(r.status_code, r.reason)