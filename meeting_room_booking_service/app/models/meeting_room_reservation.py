#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mongoengine import EmbeddedDocument, StringField, Document, EmailField, EmbeddedDocumentField, DateTimeField

class Room(EmbeddedDocument):
    name = StringField()

class Employeer(EmbeddedDocument):
    name = StringField()

class RoomReservation(Document):
    
    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.employeer = Employeer()
        self.room = Room()

    datehour = DateTimeField()
    employer = EmbeddedDocumentField(Employeer)
    room = EmbeddedDocumentField(Room)
    
    meta = {
        'collection' : 'room_reservations'
    }
