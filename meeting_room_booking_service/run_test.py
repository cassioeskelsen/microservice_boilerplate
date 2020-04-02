#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from app.meeting_room_service import MeetingRoomService

MeetingRoomService.connect()
t = MeetingRoomService()
t.NewReservation("yoda",datetime.now())
