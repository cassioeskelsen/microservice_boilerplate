#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app.broker.broker_base import BrokerBase


class BrokerConsumer(BrokerBase):
    
    def __init__(self, channels):
        super(self, BrokerBase).__init__()
        # TODO: terminar
        #self.broker.declare_channels()
        #self.channel.queue_declare(queue=self.QUEUE_NAME)
        