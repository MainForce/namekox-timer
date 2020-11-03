# Install
```shell script
pip install -U namekox-timer
```

# Example
> ping.py
```python
#! -*- coding: utf-8 -*-

# author: forcemain@163.com


from logging import getLogger
from namekox_timer.core.entrypoints.timer import timer


logger = getLogger(__name__)


class Ping(object):
    name = 'ping'

    @timer(5)
    def ping(self):
        logger.debug('pong')
```

# Running
> namekox run ping
```shell script
2020-09-19 11:16:17,800 DEBUG load service classes from ping
2020-09-19 11:16:17,804 DEBUG load container class from namekox_core.core.service.container:ServiceContainer
2020-09-19 11:16:17,804 DEBUG starting services ['ping']
2020-09-19 11:16:17,804 DEBUG starting service ping entrypoints [ping:namekox_timer.core.entrypoints.timer.Timer:ping]
2020-09-19 11:16:17,805 DEBUG spawn manage thread handle ping:namekox_timer.core.entrypoints.timer:_run(args=(), kwargs={}, tid=_run)
2020-09-19 11:16:17,805 DEBUG service ping entrypoints [ping:namekox_timer.core.entrypoints.timer.Timer:ping] started
2020-09-19 11:16:17,805 DEBUG starting service ping dependencies []
2020-09-19 11:16:17,805 DEBUG service ping dependencies [] started
2020-09-19 11:16:17,806 DEBUG services ['ping'] started
2020-09-19 11:16:22,807 DEBUG spawn worker thread handle ping:ping(args=(), kwargs={}, context=None)
2020-09-19 11:16:22,808 DEBUG pong
2020-09-19 11:16:27,806 DEBUG spawn worker thread handle ping:ping(args=(), kwargs={}, context=None)
2020-09-19 11:16:27,806 DEBUG pong
2020-09-19 11:16:32,809 DEBUG spawn worker thread handle ping:ping(args=(), kwargs={}, context=None)
2020-09-19 11:16:32,810 DEBUG pong
2020-09-19 11:16:34,500 DEBUG stopping services ['ping']
2020-09-19 11:16:34,500 DEBUG stopping service ping entrypoints [ping:namekox_timer.core.entrypoints.timer.Timer:ping]
2020-09-19 11:16:34,501 DEBUG wait service ping entrypoints [ping:namekox_timer.core.entrypoints.timer.Timer:ping] stop
2020-09-19 11:16:34,501 DEBUG service ping entrypoints [ping:namekox_timer.core.entrypoints.timer.Timer:ping] stopped
2020-09-19 11:16:34,501 DEBUG stopping service ping dependencies []
2020-09-19 11:16:34,501 DEBUG service ping dependencies [] stopped
2020-09-19 11:16:34,502 DEBUG services ['ping'] stopped
2020-09-19 11:16:34,502 DEBUG killing services ['ping']
2020-09-19 11:16:34,502 DEBUG service ping already stopped
2020-09-19 11:16:34,502 DEBUG services ['ping'] killed
```
