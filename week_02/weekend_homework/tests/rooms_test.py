import unittest

from src.rooms import Rooms
from src.songs import Songs


class RoomsTest(unittest.TestCase):

    def setUp(self):
         self.room = Rooms("Room_3", 10, [])
         self.song = Songs("It was a good day")

    
    def test_room_has_num(self):
         self.assertEqual("Room_3", self.room.room_has_num())

    def test_check_in_guest(self):
         self.assertEqual(9, self.room.check_in_guest())

    def test_add_song(self):
         self.room.add_song(self.song)
         self.assertEqual("It was a good day", self.room.playlist[0])