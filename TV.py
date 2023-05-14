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

        