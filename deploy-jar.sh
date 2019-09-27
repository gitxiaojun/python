#!/bin/bash
Data=`date +%F`

file='/data/wei'
back='/home/backup'
scr='/home/ource'


PID=$(cat /data//wei-service.pid)
kill -9 $PID
cd $file
#tar zcvf $back/$Data-weiyin.tar.gz weiyin-pay-service.jar
mv wei-service.jar  $back/$Data-wei.tar
rm -f $file/wei-service.jar
cp /home/wei-service.jar  $file/
#nohup  java -jar /data/wei-service.jar >>/data/wei.txt 2>1&
nohup  java -jar -Dspring.config.location=/data/pa
