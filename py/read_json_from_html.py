#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# file:    read_json_from_http.py
# author:  rbw
# date:    Mon  5 Dec 00:55:04 UTC 2016
# purpose: pull PiAware data from local http server
#
# todo:    do this without creating JSON file
########################################################################
import sys, os
import time, re
import urllib
import tempfile
import json

def read_json_from_html(url, out_file):
	urllib.urlretrieve(url, out_file)

	print "writing JSON to \"%s\"" % out_file
	with open(out_file, "r") as jfile:
		data_json = ""
		for line in jfile.readlines():
			data_json += line

	print "DATA:"
	print ">>>" + data_json + "<<<"
	data = json.loads(data_json)
	print ""

	d1 = data['aircraft']
	print "D1:"
	print d1
	print ""

	#d2 = d1[0]
	#print "D2"
	#print d2
	#print ""

	for item in d1:
		print item
	print ""

if __name__ == '__main__':

	url = "http://localhost:8080/data/aircraft.json"

	#out_file = "/tmp/out.json"
	tf = tempfile.NamedTemporaryFile()
	out_file = tf.name
	read_json_from_html(url, out_file)
	print "removing file \"%s\"" % out_file	
	#os.remove(out_file)


	sys.exit(0)


