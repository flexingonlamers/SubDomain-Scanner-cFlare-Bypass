#!/usr/bin/python
import os
import socket
import threading
import random
import sys

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan

print(''+C+'')

print '''
   Created By FlexingOnLamers
   Type oof to begin you thot

'''

choice = raw_input(''+C+'('+P+'AWS'+C+')> '+R+'')


if choice == 'oof':


        subdomains = ["dc", "api", "irc", "irix", "fileserver", "backup", "agent", "c2c", "login", "mssql", "mysql", "localhost", "nameserver", "netstats", "mobile", "mobil",  "ftp", "webadmin", "uploads", "transfer", "tmp", "support", "smtp0#", "smtp#", "smtp", "sms", "shopping", "sandbox", "proxy", "manager", "cpanel", "webmail", "forum", "driect- connect", "vb", "forums", "pop#", "pop", "home", "direct", "mail", "access", "admin", "oracle", "monitor", "administrator", "email", "downloads", "ssh", "webmin", "paralel", "parallels", "www0", "www", "www1", "www2", "www3", "www4", "www5", "autoconfig.admin", "autoconfig", "autodiscover.admin", "autodiscover", "sip", "msoid", "lyncdiscover"]
        url = raw_input(''+C+'Enter Hostname Retard:'+P+':')
        print(''+C+'')

        for cso in subdomains:
                try:
                        host = str(cso) + "." + str(url)
                        ip = socket.gethostbyname(str(host))
                        print 'Callback: ' + host + ' | ' + ip
                except:
                        pass


