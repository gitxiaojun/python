#!/bin/bash
TIME=`date +%F`
APPpath=/data/app
MAPPpath=/data/app
WEIXINpath=/data/app
BACKpro=/data/app/backpro
Back=/home/ap
project=/home/app
config=/home/app

function checkapp(){
        count=`ps -ef |grep ap |grep -v grep |wc -l`
        if [ 0 -eq $count ];then
             echo no app process
         else
              /etc/init.d/ap  stop
              if [ $? -eq 0 ];then
                 echo app tomcat has stopped
              else
                ps -ef|grep ap|grep -v grep|awk   '{print $2}'|xargs kill -9
              fi


         fi
}


function checkmapp(){
        count=`ps -ef |grep ma |grep -v grep |wc -l`
        if [ 0 -eq $count ];then
             echo no ma process
         else
              /etc/init.d/ma stop
              if [ $? -eq 0 ];then
                 echo ma tomcat has stopped
              else
                ps -ef|grep ma|grep -v grep|awk   '{print $2}'|xargs kill -9
              fi


         fi
}

function checkwe(){
        count=`ps -ef |grep weixin |grep -v grep |wc -l`
        if [ 0 -eq $count ];then
             echo no wei process
         else
              /etc/init.d/wei  stop
              if [ $? -eq 0 ];then
                 echo wei tomcat has stopped
              else
                ps -ef|grep wei|grep -v grep|awk   '{print $2}'|xargs kill -9
              fi


         fi
}


  function APP1() {
              checkapp
              cp $APPpath/webapps/ROOT.war   $Back/$TIME-app.war
              sleep 3s
              rm -rf $APPpath/webapps/*
                cp $project/ap.war  $APPpath/webapps/ROOT.war
                /etc/init.d/app  start
                sleep 5s
              checkapp
              rm -rf $APPpath/webapps/ROOT/WEB-INF/classes/appli && cp /home/app/scripts/app/appli   $APPpath/webapps/ROOT/WEB-INF/classes/ && echo 'weiyin'  >/$APPpath/webapps/ROOT/test.html  &&  rm -f /data/app/app-1/webapps/ROOT/WEB-INF/classes/redis.properties && cp /home/app/scripts/redis.properties  /data/app/app-1/webapps/ROOT/WEB-INF/classes/
               /etc/init.d/app  start
             }


  function MAPP1() {
              checkmapp
              cd /data/app/mapp/webapps/  && tar zcf  /home/app/backup/$TIME-mapp.tar.gz  mapp
              sleep 3s
              rm -rf $MAPPpath/webapps/mapp/*
                unzip -q $project/mapp.war  -d $MAPPpath/webapps/mapp
                /etc/init.d/mapp start
                sleep 5s
                   checkmapp
                    rm -rf  $MAPPpath/webapps/mapp/WEB-INF/classes/config/config.properties
              \cp $config/mapp/config.properties   $MAPPpath/webapps/mapp/WEB-INF/classes/config/  && rm -f /data/app/mapp/webapps/mapp/WEB-INF/views/include/global.jsp && cp $config/global.jsp  /data/app/mapp/webapps/mapp/WEB-INF/views/include/
                    rm -rf  $MAPPpath/webapps/mapp/WEB-INF/classes/config/redis.properties
                \cp $config/redis.properties   $MAPPpath/webapps/mapp/WEB-INF/classes/config/
                  /etc/init.d/mapp start
             }

function WEIXIN() {
              checkweixin
              cp $WEIXINpath/webapps/ROOT.war   $Back/$TIME-weixin.war
              sleep 3s
              rm -rf $WEIXINpath/webapps/*
                cp $project/wx.war  $WEIXINpath/webapps/ROOT.war
                /etc/init.d/weixin  start
                sleep 5s
              checkweixin
              rm -rf $WEIXINpath/webapps/ROOT/WEB-INF/classes/application.properties && cp /home/app/scripts/weixin/application.properties   $WEIXINpath/webapps/ROOT/WEB-INF/classes/ && rm-f /data/app/weixin/webapps/ROOT/WEB-INF/classes/redis.properties && cp /home/app/scripts/redis.properties  /data/app/weixin/webapps/ROOT/WEB-INF/classes/ && rm -f /data/app/weixin/webapps/ROOT/WEB-INF/views/themes/default/include/global.jsp
              cp /home/app/scripts/global.jsp  /data/app/weixin/webapps/ROOT/WEB-INF/views/themes/default/include/
              /etc/init.d/weixin  start
}

 case $1 in
        ap)
        AP
        ;;
        mapp)
        MAPP1
        ;;
        wei)
        WEI
        ;;
        all)
        AP
        MG
        MAP
        BACKPRO
        ;;
        *)
        echo "you input error!"
        ;;
esac
