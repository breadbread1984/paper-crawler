#!/usr/bin/python3

from wos import WosClient
import wos.utils

with WosClient('User', 'Password') as client:
  wos.utils.query(client, 'CNT dispersant')
  wos.utils.query(client, 'carbon nanotube dispersion')

