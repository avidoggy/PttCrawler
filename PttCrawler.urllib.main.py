#!/usr/bin/python
#!/usr/bin/env python
# encoding=UTF-8

import urllib.request as request
import urllib.response
import json
import sys

GossipingIndexUrl = "https://www.ptt.cc/bbs/Gossiping/index.html"

#httpsConOpener = urllib.request.build_opener()
#response = httpsConOpener.open(GossipingIndexUrl)
response = urllib.request.urlopen(GossipingIndexUrl)

resp_url = response.geturl()
#resp_info = response.info()
#resp_content = response.read().decode("UTF-8")

#print(resp_url)
#print(resp_info)
#print(resp_content)

if "ask/over18" in resp_url:
	print("ooops")
	post_req =request.Request(resp_url, b"yes:yes")
	response = request.urlopen(post_req)
	print(response.geturl())
	print(response.info())
	print(response.read())

print("end")
