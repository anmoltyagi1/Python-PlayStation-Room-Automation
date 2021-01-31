import sys
import subprocess
import os
from decouple import config
from lights import *




IP_NETWORK = config('IP_NETWORK')
IP_DEVICE = config('IP_DEVICE')


proc = subprocess.Popen(["ping", IP_NETWORK],stdout=subprocess.PIPE)
while True:
    try:
      if subprocess.check_output(["ping", "-c", "1", IP_DEVICE]):
          print("Connected")
          connect()

          break
    except:

        print("Not Connected")