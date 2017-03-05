import consul
import toml
import os
import providers
import logger
import logger
import sys


def main():
  sys.excepthook = logger.sys_excepthook
  c = consul.Consul(os.environ.get('CONSUL_CONNECTION'))
  _, consul_dict = c.kv.get(os.environ.get('CONFIG_KEY'))
  config = toml.loads(consul_dict['Value'].decode('utf8'))
  logger.debug({'config': config, 'type': 'config'})

  for name, args in config.items():
    providers.providers[name].run(args)


if __name__ == '__main__':
    main()
