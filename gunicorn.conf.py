import multiprocessing
import os

DEBUG = os.environ.get('DEBUG_MODE', 'enabled') == 'enabled'

bind = '0.0.0.0:' + os.environ.get('PORT', '8000')
log_level = 'debug' if DEBUG else 'info'
proc_name = 'gunicorn'
workers = multiprocessing.cpu_count() * 2 + 1
keepalive = 120
timeout = 120
worker_class = "gthread"
threads = 3
