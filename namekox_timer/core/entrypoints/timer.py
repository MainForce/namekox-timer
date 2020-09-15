#! -*- coding: utf-8 -*-

# author: forcemain@163.com


import time


from itertools import count
from eventlet import Timeout
from logging import getLogger
from eventlet.event import Event
from namekox_core.core.service.entrypoint import Entrypoint


logger = getLogger(__name__)


class Timer(Entrypoint):
    def __init__(self, interval, eager=True, **kwargs):
        self.gt = None
        self.eager = eager
        self.interval = interval
        self.stopping_event = Event()
        self.finished_event = Event()
        super(Timer, self).__init__(**kwargs)
    
    def start(self):
        self.gt = self.container.spawn_manage_thread(self._run)
    
    def stop(self):
        self.stopping_event.send(True)
        self.gt.wait()
    
    def kill(self):
        self.gt.kill()
    
    def _run(self):
        def gen_interval():
            start_time = time.time()
            start = 1 if self.eager else 0
            for n in count(start=start):
                i = max(start_time + n * self.interval - time.time(), 0)
                yield i
        interval = gen_interval()
        to_sleep = next(interval)
        while True:
            with Timeout(to_sleep, exception=False):
                self.stopping_event.wait()
                break
            self.container.spawn_worker_thread(self, (), {}, res_handler=self._res_handler)
            self.finished_event.wait()
            self.finished_event.reset()
            to_sleep = next(interval)
    
    def _res_handler(self, result, exc_info):
        self.finished_event.send(True)
        return result, exc_info


timer = Timer.decorator
