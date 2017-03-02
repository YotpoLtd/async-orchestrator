import json
import socket
import os

timeout = float(os.environ.get('LOGSTASH_TIMEOUT'))
host = os.environ.get('LOGSTASH_HOST')
port = int(os.environ.get('LOGSTASH_PORT'))


def netcat(content):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(timeout)
  s.connect((host, port))
  s.sendall(content.encode())
  s.shutdown(socket.SHUT_WR)
  s.close()


def log(level, content):
  log = {'app_name': 'async-orchestrator',
         'severity': level,
         'msg': content}

  try:
    netcat(json.dumps(log))
  except Exception as e:
    print('failed to log: {}'.format(e))


def debug(content):
  log(level='DEBUG', content=content)


def info(content):
  log(level='INFO', content=content)


def error(content):
  log(level='ERROR', content=content)
