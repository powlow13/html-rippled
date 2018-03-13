#!/usr/bin/env python
# coding: utf-8
import time
import json, requests, pprint
import whois
from threading import Thread
from statistics import mean

class fetch_validator(Thread):
  def __init__(self, val, dom):
      Thread.__init__(self)
      self.val = val
      self.dom = dom

  def run(self):
     agree = []
     validator_url = 'https://data.ripple.com/v2/network/validators/' + self.val + '/reports'
     data = requests.get(url=validator_url)
     binary = data.content
     validator_output = json.loads(binary)
     if 'reports' in validator_output:
        for reports in validator_output['reports']:
          agree.append(float(reports['main_net_agreement']))
        str = (self.dom).replace('/', '-')
        validStat[str] = mean(agree)

start_time = time.time()

url = 'https://data.ripple.com/v2/network/validators/'

myThread =[]

validStat = {}

data = requests.get(url=url)
binary = data.content
output = json.loads(binary)

# test to see if the request was valid
#print output['result']

if 'validators' in output:
   for validators in output['validators']:
     if 'domain' in validators:
        if 'validation_public_key' in validators:
           myThread.append(fetch_validator(validators['validation_public_key'], validators['domain']))


for threads in myThread:
  threads.start()
for threads in myThread:
  threads.join()

end_time = time.time() 

for key, value in sorted(validStat.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print "%30s : <b>%.4f</b>" % (key, round(value,4))


print("\nExec time: %ssecs" % (end_time - start_time))


