# coding: latin1

import pycurl
try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode
try:
    # Python 3
    from io import BytesIO
except ImportError:
    # Python 2
    from StringIO import StringIO as BytesIO
from bs4 import BeautifulSoup

import time
from datetime import datetime, timedelta

now = datetime.now()

delta = timedelta(minutes=8)
#print(delta)

now = now + delta
now_tuple = now.timetuple()

date_num_train = str(now_tuple[0]) + '|' + str(now_tuple[1]).zfill(2) + '|' + str(now_tuple[2]).zfill(2)
#print(date_num_train)

station = 'gare de Antibes'
stationCode = 'OCE87757674'
sens = '1' 

next_horaire = str(now_tuple[3]).zfill(2) + '|' + str(now_tuple[4]).zfill(2)
#print(next_horaire)

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://www.infolignes.com/recherche.php')
c.setopt(c.WRITEDATA, buffer)

post_data = {'date_num_train': date_num_train, 'station': station, 'stationCode': stationCode, 'next_horaire': next_horaire, 'sens': sens}
# Form data must be provided already urlencoded.
postfields = urlencode(post_data)
# Sets request method to POST,
# Content-Type header to application/x-www-form-urlencoded
# and data to send in request body.
c.setopt(c.POSTFIELDS, postfields)

print(postfields)
c.perform()
c.close()

body = buffer.getvalue().decode('utf-8')
# Body is a byte string.
# We have to know_tuple the encoding in order to print it to a text file
# such as standard output.
#print(body)

soup = BeautifulSoup(body)
resultats = soup.find_all(id="resultat")

print(resultats[0])
