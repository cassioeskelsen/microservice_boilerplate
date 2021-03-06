#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, sys
import urllib.request
from datetime import datetime, timedelta

from utils.logger import logger

from app.broker.broker_consumer import BrokerConsumer


class QueueConsumerWorker():
    
    def __init__(self):
        self.broker = BrokerConsumer()
     
    
    def run(self) -> bool:
        try:
            message, method = self.broker.get_next_message()
            if message is not None:
                logger.info(f"New message:{message}")
                self.broker.ack_message(method)
            
            # time.sleep(0.2)
            return 0
        except Exception as err:
            logger.error(str(err))
            return 1  # return cause


class Coordinator():
    HEALTH_CHECK_PERIOD = 5000  # milliseconds
    
    def __init__(self):
        self.consumer = QueueConsumerWorker()
        self.consumer.name = "nome teste"
        self.can_execute = 0
        self.last_health_check = datetime.now() - timedelta(
            milliseconds=self.HEALTH_CHECK_PERIOD + 1)  # force first Healthcheck
    
    def health_checks(self):
        if not self.health_check_api_1():
            self.can_execute = 1  # set error and reason
            logger.info("Stop consuming...")
        else:
            if self.can_execute > 0:
                self.can_execute = 0
                logger.info("Resuming consuming...")
            
            # self.health_check_api_2()
            # self.health_check_api_nn()
    
    def health_check_api_1(self) -> bool:
        return True
        #try:
        #    f = urllib.request.urlopen("http://127.0.0.1:5002/api/whatever")
        #    if f.status == 200:
        #        return True
        #    else:
        #       return False
        #except Exception as err:
        #    logger.error("Can't connect to API")
        #    return False
    
    # def health_check_api_2(self) -> bool:
    # pass
    
    def run_tasks(self):
        while True:  # with the try/except below run virtually eternally
            currentMillis = datetime.now()
            if (currentMillis - self.last_health_check).total_seconds() * 1000 >= self.HEALTH_CHECK_PERIOD:
                logger.debug("Health check time....")
                self.health_checks()
                self.last_health_check = datetime.now()
            try:
                if self.can_execute < 1:
                    self.can_execute = self.consumer.run()
                else:
                    pass
            except Exception as err:
                logger.critical(str(err))


