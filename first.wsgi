#!/usr/bin/python
import site
import os
site.addsitedir(os.path.join(os.path.dirname(__file__),     '/home/ubuntu/.local/lib/python3.6/site-packages/'))
activate_this = '/home/ubuntu/first/env/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(),{'__file__':activate_this})
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/ubuntu/first")

from first import app as application
application.secret_key = '24d522a8904e09b2e71d305f56a9d45398408929b3d72785'


