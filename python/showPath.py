#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://www.cnblogs.com/dreamer-fish/p/3820625.html
import os
# 显示当前目录下所有文件、文件夹
path ="." 
def gci(filepath):
# 遍历filePath目录下的所有文件、文件夹，包括子目录
  files = os.listdir(filepath)
  for fi in files:
    fi_d = os.path.join(filepath,fi)
    if os.path.isdir(fi_d):
    # 递归调用子目录
      gci(fi_d) 
    else:
      print os.path.join(filepath,fi_d)
# 调用目录
gci(path)