#!/usr/bin/python
#-*- coding: utf-8 -*-
import os,sys,gzip
filename = sys.argv[1]
uncompressname = sys.argv[2]
f_in = gzip.open(filename,'rb')
f_out = open(uncompressname,'wb')
f_out.writelines(f_in)
f_in.close()
f_out.close()
