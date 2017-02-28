import consul
import toml
import os
import providers

c = consul.Consul(os.environ.get('CONSUL_CONNECTION'))

_, consul_dict = c.kv.get(os.environ.get('CONFIG_KEY'))

config = toml.loads(consul_dict['Value'].decode('utf8'))

print('got config: {}'.format(config))

for name, args in config.items():
  providers.providers[name].provider(args)
