#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mongoengine import connect
from app.settings.mongo_settings import MongoSettings

from app.models.meeting_room_reservation import RoomReservation


class MeetingRoomService():
    
    @staticmethod
    def connect():
        connect(host=MongoSettings.MONGODB_URI, authentication_source="admin")
    
    def __init__(self):
        pass
    
    
    def NewReservation(self, room_name, datetime):
        reservation = RoomReservation()
        reservation.room.name = "Yoda"
        reservation.employeer.name = "José"
        reservation.datehour = datetime
        reservation.save()