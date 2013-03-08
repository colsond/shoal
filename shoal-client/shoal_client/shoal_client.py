"""
  Very simple client script used to get nearest squid server using the RESTful API.
"""

import urllib2
import sys
import json
import logging
import config

from urllib2 import urlopen

config.setup()
url = config.shoal_server_url

try:
    f = urlopen(url)
    data = f.read()
except urllib2.URLError as e:
    logging.error("Unable to open url. %s" % e)
    sys.exit(1)

if data:
    data = json.loads(data)
    for i in data:
        print '{0} Squid {1} {0}'.format('='*25, i)
        print 'Public IP:', data[i]['public_ip']
        print 'Private IP:', data[i]['private_ip']