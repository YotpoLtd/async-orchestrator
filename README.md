run with python3

example env vars:

LOGSTASH_HOST=localhost

CONSUL_CONNECTION=localhost

LOGSTASH_TIMEOUT=0.01

LOGSTASH_PORT=5960

CONFIG_KEY=a

NOMAD_URL=http://localhost:4646


example of toml as the consul value:

[resque]
redis_host = 'localhost'
redis_port = 6379
redis_db_num = 1
threshold = 3
plus = 1
