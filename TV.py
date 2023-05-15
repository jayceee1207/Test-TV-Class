#Make a class named Class TV

class TV:
    #Inside a function are the objects. The default of channel and volume is 1 and the default boolean expression
    #is False that indicates that the TV is off.
    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.on = False

    #This function returns a boolean expression True if the TV is on.
    def turn_on_tv(self):
        self.on = True
    
    #This function returns a boolean expression False if the TV is on.
    def turn_off_tv(self):
        self.off = False    
    
    #This function returns the channel of TV.
    def get_tv_channel(self):
        return self.channel
    #This means that the current channel will be changed if new channel is within the range 1-120
    def change_tv_channel (self, channel):
        if self.turn_on_tv and 1 <= channel <= 120:
            self.channel = channel

    #This function increment the channel by one. If previous channel is 23, the new channel will be 24.
    def channel_tv_up(self, channel):
        if self.turn_on_tv and 1 <= channel <= 120:
            self.channel += 1
    
    #This function decrement the channel by one. If previous channel is 23, the new channel will be 22.
    def channel_tv_down(self, channel):
        if self.turn_on_tv and 1 <= channel <= 120:
            self.channel -= 1

    #This means that the current volume will be changed if new volume is within the range 1-7
    def get_tv_volume(self):
        return self.get_tv_volume
    def change_tv_volume(self, volume_level):
        if self.turn_on_tv and 1 <= volume_level <=7:
            self.volume_level = volume_level
    
    #This function increment the channel by one. If previous volume is 3, the new channel will be 4.
    def tv_volume_up(self, volume):
        if self.turn_on_tv and 1 <= volume >= 7:
            self.get_tv_volume += 1
    
    #This function decrement the channel by one. If previous volume is 3, the new channel will be 2.
    def tv_volume_down(self, volume):
        if self.turn_on_tv and 1 <= volume >= 7:
            self.get_tv_volume -= 1
    





        