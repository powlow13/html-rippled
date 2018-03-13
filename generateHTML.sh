#!/bin/bash

/home/powlow/ripple/html-rippled/getPeers.py > /tmp/peers.txt
/home/powlow/ripple/html-rippled/averageValidators.py > /tmp/validators.txt
sleep 3
echo "<html><head><title>data.rippled.fr</title></head><body>" > /tmp/index.html
echo "<h1>data.rippled.fr</h1>" >> /tmp/index.html

echo "<h2>Verified rippled validators average agreement</h2>" >> /tmp/index.html
echo "<pre><code>" >> /tmp/index.html
cat /tmp/validators.txt >> /tmp/index.html
echo "</code></pre><br>" >> /tmp/index.html

echo "<h2>Rippled peers with PTR records</h2>" >> /tmp/index.html
echo "<pre><code>" >> /tmp/index.html
cat /tmp/peers.txt >> /tmp/index.html
echo "</code></pre><br>" >> /tmp/index.html

echo "</body></html>" >> /tmp/index.html

