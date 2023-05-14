#Make a class named Class TV

class TV:


    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.on = False

    def turn_on_tv(self):
        self.on = True
    
    def turn_off_tv(self):
        self.off = False    
    
    def get_tv_channel(self):
        return self.channel
    
    #This means that the current channel will be changed if new channel is within the range 1-120
    def change_channel_tv (self, channel):
        if 1 <= channel <= 120:
            self.channel = channel

    def get_tv_volume(self):
        return self.get_tv_volume
    
    #This means that the current volume will be changed if new channel is within the range 1-7
    def tv_volume_up(self, volume):
        if 1 <= volume >= 7:
            self.get_tv_volume = volume
    




        