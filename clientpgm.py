from http.server import requests
payload = {'payload':'0x38 0x39 0x20 0x35 0x30 0x20 0x37 0x30 0x20 0x34 0x38'}
r = requests.POST('http://localhost:7878/post', data=json.dumps(payload))
r= message_bytes.decode('ascii')

print(r.text)
