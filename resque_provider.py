from redis import StrictRedis
import action_handler
import logger


def run(args):
  logger.debug({'run': 'resque', 'args': args})
  redis = StrictRedis(host=args['redis_host'], port=args['redis_port'], db=args['redis_db_num'])
  for queue_name_bytes in redis.smembers('resque:queues'):
    queue_name = queue_name_bytes.decode('utf8')
    queue_len = redis.llen('resque:queue:{}'.format(queue_name))
    logger.debug({'type': 'found_queue', 'queue_name': queue_name, 'queue_len': queue_len})
    if queue_len > args['threshold']:
      action_handler.add_workers(queue_name, args['plus'])
