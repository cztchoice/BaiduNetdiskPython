#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BaiduOpenAPI.BaiduOauth2 import OauthClient

from BaiduOpenAPI.BaiduNetdisk import BaiduNetdisk

import os
import json

token_data = None
if not os.path.isfile("token_data.txt"):
	oauth = OauthClient("O0Kh2O3HQ4EXyfCvuEGINXAS", "cfj5ZBL6d1Gnmt330Mtc9XuybMg3nL6X", "oob")

	print("temp")
	print(oauth.get_authorize_url(scope="basic netdisk"))
	code = raw_input("input:")

	token_data = oauth.get_access_token_by_authorization_code(code)
	
	f =open("token_data.txt","w")
	json.dump(token_data, f)
	f.flush()
	f.close()
else:
	fr = open("token_data.txt")
	token_data = json.load(fr)
	fr.close()

#print(token_data)
pan = BaiduNetdisk(token_data[u"access_token"])
#fa = open("Desert.jpg")
fn = "a.txt"
print(pan.upload_single_file("/apps/netdisk/a.txt", fn))

