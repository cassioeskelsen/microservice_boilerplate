#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


class MongoSettings:
    """ MONGODB Settings
    """
    MONGODB_URI = os.environ.get('MONGODB_URI')
    #MONGO_DATABASE = os.environ.get('MONGODB_DATABASE_BOOKING_SERVICE', default="meeting_room_booking_service")
