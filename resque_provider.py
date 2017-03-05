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

    # Prioritizing specific queue settings
    if queue_len > ((args.get(queue_name) and args.get(queue_name).get('threshold')) or args.get('threshold')):
      action_handler.add_workers(queue_name, ((args.get(queue_name) and args.get(queue_name).get('plus')) or args.get('plus')))
