#!/usr/bin/env python
#-*-coding:UTF-8-*-
# Description:nginx日志切割脚本
import os
import glob
import time
import shutil
#日志路径
path = '/opt/openresty/nginx/logs'
#切割后日志路径
cut_path = '/data/logs/app2/'
#nginx pid
nginx_pid = '/opt/openresty/nginx/logs/nginx.pid'

#删除之前一个月的日志目录
year = int(time.strftime("%Y", time.localtime()))
month = int(time.strftime("%m", time.localtime()))
if (month == 1):
    year = year - 1
    month = 12
else:
    month = month - 1

year = str(year)
month = str(month)
if (len(month) == 1):
    month = '0' + month

olddir = cut_path +'/' + year + month
if os.path.exists(olddir):
    shutil.rmtree(olddir)

#创建目录
cut_path = cut_path + '/' + str(time.strftime("%Y%m", time.localtime())) + '/'
if not os.path.exists(cut_path):
        os.makedirs(cut_path)

#切割日志目录下的日志
files = glob.glob("%s/*.log"%(path))
for sfile in files:
        filearr = sfile.split('.')
        filename = filearr[0]
        filename = filename.split(path)
        filename = filename[1].replace('/', '')
        newfilename = cut_path + filename + '_' + str(time.strftime("%Y%m%d", time.localtime())) + '.log'
        #print newfilename
        os.system("mv %s %s"%(sfile,newfilename))

#重新打开日志文件
os.system("kill -s USR1 `cat %s`"%(nginx_pid))
os.system("chown app.app %s"%(path))
