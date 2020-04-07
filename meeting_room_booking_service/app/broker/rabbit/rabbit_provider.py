#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from meeting_room_booking_service.app.broker.broker_provider import BrokerProvider


class RabbitMQProvider(BrokerProvider):
    
    def connect(self):
        pass
        
    def disconnect(self):
        pass
        
    def get_next_message(self):
        pass
    
    def declare_channels(self, channel_names):
        pass
    
    def send_message(self, topic, message):
        pass
    
    def send_message(self, topic, routing_key, message):
        pass