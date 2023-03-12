class Rooms:
    def __init__(self, room_num, capacity, playlist):
        self.room_num = room_num
        self.capacity = capacity
        self.playlist = playlist

    def room_has_num(self):
        return self.room_num
    
    def check_in_guest(self):
        self.capacity -= 1
        return self.capacity
    
    def add_song(self, song):
        self.playlist.append(song)
 
