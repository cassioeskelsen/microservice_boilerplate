#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

from meeting_room_booking_service.app.broker.broker_base import BrokerBase


class BrokerProducer(BrokerBase):

    def send_message(self, topic, message):
        self.broker.send_message(topic,message)
    