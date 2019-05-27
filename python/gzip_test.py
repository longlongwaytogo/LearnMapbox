#!/usr/bin/python
#-*- coding: utf-8 -*-
# create gzip
import os,sys,gzip

print "create gzip file"
filename = sys.argv[1]
# open file
f_in = open(filename,'rb')
# compress
compressname = filename + ".gz"
f_out = gzip.open(compressname,'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()
