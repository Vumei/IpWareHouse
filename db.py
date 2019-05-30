#-*- coding:utf-8 -*-
# !/usr/bin/python
#date:190306


import pymysql
import os
import time

#Initialize variables
curtime = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
my_file = "/root/arp_status/arp.txt"
list_IP = []
list_MAC = []

#Read each line of data
with open(my_file, 'r',1024) as ins:
        list_IP = []
        ctx = 0
        for line in ins:
                if ctx%2==0:
                        list_IP.append(line.strip('\n'))
                else:
                        list_MAC.append(line.strip('\n'))
                ctx = ctx + 1;

print(curtime,"The number of inserted is  " + str(len(list_IP)))

#Create a table
conn = pymysql.connect(host='localhost', port=3306, user='root', 
passwd='***', db='arp_status',charset='utf8',use_unicode=True)
cur = conn.cursor()


#Connect to MySQL
for i in range(0,len(list_IP)):
        cur.execute("insert arp (IP,MAC) values (%s,%s)",(list_IP[i],list_MAC[i]))
conn.commit()

#Close the connection
cur.close()
conn.close()


if os.path.exists(my_file):
	os.remove(my_file)
else:
	print("no such file!")
	    






