#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This service don't require a Class

For each model, create a function with this operations:
- open connection with broker
- send message
- close connection with broker

Best practice to send messages to broker is open the connection as late as possible and close it as soon as possible

'''

def send_user_to_broker(user_data):
    topic_name = 'TOPIC/USER_IN'   #TODO: get from config file
    # open broker connection
    # send message
    # close broker connection
    print("user sended to broker")
    