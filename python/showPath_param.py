#!/usr/bin/python
#-*- coding: utf-8 -*-
import os,sys
parm =sys.argv[1]
if parm == "help" or parm =="-h" or parm == "h":
  print "usage: showPath_param.py dir"
  sys.exit(0)
path = parm
for fpathe,dirs,fs in os.walk(path):
  for f in fs:
    print os.path.join(fpathe,f)


