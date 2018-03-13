#!/usr/bin/env python
# coding: utf-8
import time
import json, requests, pprint
import socket
import operator
from threading import Thread
from statistics import mean
from operator import itemgetter

def lookup(addr):
    try:
        name, alias, addresslist = socket.gethostbyaddr(addr)
        return name
    except socket.herror:
        return None


class fetch_peer(Thread):
  def __init__(self, ip, ver):
      Thread.__init__(self)
      self.ip = ip
      self.ver = ver

  def run(self):
     topology = []
     host = lookup(self.ip)
     if host is not None:
        peerList[host] = self.ver


start_time = time.time()

url = 'https://data.ripple.com/v2/network/topology'

myThread =[]

peerList = {}
peerList_sort = {}

bigList = []

totalPeer = 0

data = requests.get(url=url)
binary = data.content
output = json.loads(binary)

# test to see if the request was valid
#print output['result']

for peer in output['nodes']:
    if 'ip' in peer:
      if 'version' in peer:
        myThread.append(fetch_peer(peer['ip'], peer['version']))


for threads in myThread:
  threads.start()
for threads in myThread:
  threads.join(10)

end_time = time.time() 


for key in sorted(peerList.iterkeys()):
    entry = {}
    entry['domain'] = key.split(".")[-2]
    entry['tld'] = key.split(".")[-1]
    entry['host'] = key
    entry['version'] = peerList[key]
    bigList.append(entry)

sortedList = sorted(bigList, key=itemgetter('tld', 'domain'))

for peer in sortedList:
    host = peer['domain'] + ".<b>" + peer['tld'] + "</b>"
    print "%30s %60s : %s" % (host, peer['host'], peer['version'])
    totalPeer += 1

print "\nTotal peers = " + str(totalPeer)

print("\nExec time: %ssecs" % (end_time - start_time))


