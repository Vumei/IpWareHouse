# !/bin/bash

for i in $(cat /root/arp_status/host.txt)
    do snmpwalk -v 2c -c *****\!\@\# $i 1.3.6.1.4.1.2011.5.25.123.1.17.1.11 | grep -Eo '(192|172|10)+\.+[0-9]{1,}+\.+[0-9]{1,}+\.[0-9]{1,}|([A-Z0-9]{2} ){6}|STRING:\s\"' >> /root/arp_status/arp.txt
    echo $(date) $i inserted OK !
done
