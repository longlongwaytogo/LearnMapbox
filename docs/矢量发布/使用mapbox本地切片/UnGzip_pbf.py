#!/usr/bin/python
#-*- coding: utf-8 -*-
import os,sys,gzip
parm =sys.argv[1]
if parm == "help" or parm =="-h" or parm == "h":
  print "usage: UnGzip_pbf.py Gziped_dir UnGzip_dir extesion[pdf]"
  sys.exit(0)

argc = len(sys.argv)
# print "parm len:{0}".format(argc)
if  argc < 3 :
  print "param is not enough,\n \
  usage: \n \
       UnGzip_pbf.py Gziped_dir UnGzip_dir extesion[pdf]\n"
  sys.exit(0)
  
src_dir = sys.argv[1]
dst_dir = sys.argv[2]
file_extern = "pbf"
if argc >= 4:
   file_extern = sys.argv[3]
   print "extension is set:.{0}".format(file_extern)
   #sys.exit(0)
   
  
#for fpathe,dirs,fs in os.walk(src_dir):
#  for f in fs:
#    print os.path.join(fpathe,f)

def UnGzipPBF(src, dst):
# 遍历filePath目录下的所有文件、文件夹，包括子目录
  if not os.path.exists(dst):
    os.makedirs(dst)
  print "src file path:{0}".format(src)
  print "dst file path:{0}".format(dst)
  
  files = os.listdir(src)
  for fi in files:
    fi_d = os.path.join(src,fi)
    print "file name:{0}".format(fi_d)
    if os.path.isdir(fi_d):
      # 递归调用子目录
      basename = os.path.basename(fi_d)
      #print "baseName:{0}".format(basename)
      dst_dirname = os.path.join(dst,basename)
      print "dst path: {0}".format(dst_dirname)
      print "fi_d: {0}".format(fi_d)
     
      UnGzipPBF(fi_d,dst_dirname) 
    else:
      #filename = os.path.join(src,fi_d)
      filename =fi_d
      basefilename = os.path.basename(filename)
      src_ext = os.path.splitext(basefilename)[-1]
      src_name = os.path.splitext(basefilename)[0]
      dst_filename = src_name + '.' + file_extern 
      uncompressname = os.path.join(dst,dst_filename)
      #print src
      #print fi_d
      print filename
      print uncompressname
      # open pbf and UnGzip to mvt or pbf
     
      if src_ext == '.pbf': 
        f_in = gzip.open(filename,'rb')
        f_out = open(uncompressname,'wb')
        f_out.writelines(f_in)
        f_out.close()
        f_in.close()

# call 
UnGzipPBF(src_dir,dst_dir)

