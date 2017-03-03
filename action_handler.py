import json
import logger
import requests
import os
nomad_url = os.environ['NOMAD_URL']


def add_workers(queue_name, num_of_workers):
  logger.debug({'action': 'adding_workers', 'queue_name': queue_name, 'num_of_workers': num_of_workers})
  with open("example.json") as fh:
    job = requests.get('{}/v1/job/example'.format(nomad_url)).json()
    logger.debug({'type': 'get_job', 'response': job})
    job['TaskGroups'][0]['Count'] += num_of_workers
    logger.debug({'type': 'update_job', 'response': requests.post('{}/v1/job/example'.format(nomad_url),
                                                                  json={'Job': job}).json()})
