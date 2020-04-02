#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app.broker.broker_provider_factory import BrokerProviderFactory


class BrokerBase:
    
    def __init__(self):
        self.broker = BrokerProviderFactory.get_instance()
        