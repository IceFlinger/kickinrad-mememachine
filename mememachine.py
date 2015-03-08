#!/usr/bin/python2.7
#KRAD FLAG MEME MACHINE
import os
import requests
from PIL import Image, ImageOps
count = 0

username = ""
password = ""

s = requests.Session()
upload = False
print "Logging into Krad..."
try:
	login = s.post("http://www.kickinrad.tv/member.php",
	data={
		"action": "do_login",
		"url": "http://www.kickinrad.tv/index.php",
		"quick_login": "1",
		"quick_username": username,
		"quick_password": password,
		"submit": "Login"
		})
	print "Logged in!"
	upload = True
except:
	print "Couldn't log in"
		
		
for i in os.listdir("./input"):
	img_in = Image.open(("./input/" + i))
	img_in.save('./unconverted/%s' % i)
	print "Backed up " + i + " to unconverted"
	img_out = img_in.resize((498, 190), Image.ANTIALIAS)		# best down-sizing filter
	img_out = ImageOps.expand(img_out,border=1,fill='black')
	img_out.save('./output/flag-%s' % i)
	print "Saved flag-" + i
	os.remove("./input/" + i)
	print "Removed " + i + " from input folder"
	
	if upload:
		print "Attempting to upload flag..."
		try:
			file_upload = [('file', (('./output/flag-' + i),open(('./output/flag-' + i), "rb"), ('image/' + str(img_out.format))))]
			r = s.post("http://www.kickinrad.tv/flagupload.php",
				data={
					"MAX_FILE_SIZE": "512000",
					"uid": "",
					"submit": "DO IT"
				},
				files=file_upload
			)
			print "flag uploaded!"
		except:
			print "flag not uploaded"
	count += 1
print "Done, converted " + str(count) + " flags"



