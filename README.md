##async-orchestrator

A generic asynchronous tasks orchestrator. Designed to run once in a while, check queue statuses according to configurable policy, and act accordingly.


run with `python3`

example env vars:

```
REDIS_HOST=localhost
LOGSTASH_HOST=localhost
CONSUL_CONNECTION=localhost
REDIS_DB_NUM=1
NOMAD_URL=http://127.0.0.1:4646
REDIS_PORT=6379
LOGSTASH_TIMEOUT=0.01
LOGSTASH_PORT=5960
CONFIG_KEY=a
```


example of toml as the consul value:
you can override resque values for specific queues.

```
[resque]
redis_host = 'localhost'
redis_port = 6379
redis_db_num = 1
threshold = 3
plus = 1
sleep = 20

[resque.queue1]
threshold = 6

[resque.queue2]
plus = 3
sleep = 300

```
