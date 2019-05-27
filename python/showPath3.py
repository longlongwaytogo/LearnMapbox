#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
path='.'
for fpathe,dirs,fs in os.walk(path):
  for f in fs:
    print os.path.join(fpathe,f)
