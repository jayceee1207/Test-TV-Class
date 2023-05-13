#John Carlo Ablay
#Test TV Class
#May 13, 2023

#Create class named TV
class TV:
    def __init__(self, get_channel, volume_level, turn_on, turn_off, set_channel, get_volume, set_volume,
                 channel_up, channel_down, volume_up, volume_down):
        self.get_channel = get_channel
        self.volume_level = volume_level
        self.turn_on = turn_on
        self.turn_off = turn_off
        self.set_channel = set_channel
        self.get_volume = get_volume
        self.set_volume = set_volume
        self.channel_up = channel_up
        self.channel_down = channel_down
        self.volume_up = volume_up
        self.volume_down = volume_down
        
#Test Driver program TestTV
television_1 = TV(57, 5, True, False, 49, 6, 7, 4, 6,6,5) 
print(television_1())



