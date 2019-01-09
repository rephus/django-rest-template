import os
import logging

from django.db import connection
from django.core.management import call_command
from django.conf import settings
from io import StringIO
from todo import wsgi

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] - %(message)s')



logging.info("Performing migrations")
call_command('migrate', '--no-input')

logging.info("Initializing fixtures")
call_command('loaddata', 'initial_data.json')
