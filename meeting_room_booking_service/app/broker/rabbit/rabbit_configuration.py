#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


class RabbitConfiguration(object):
  
    HOST = os.environ.get('RABBIT_MQ_HOST')
    PORT = os.environ.get('RABBIT_MQ_PORT')
    USERNAME = os.environ.get('RABBIT_MQ_USERNAME')
    PASSWORD = os.environ.get('RABBIT_MQ_PASSWORD')
