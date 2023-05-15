#Make a class named Class TV

class TV:


    def __init__(self):
        #Inside a function are the objects. The default of channel and volume is 1 and the default boolean expression
        #is False that indicates that the TV is off.
        self.is_on = False
        self.channel_list = range(120)
        self.number_channel = len(self.channel_list)
        self.channel_index = 0
        self.volume_minimum = 0
        self.volume_maximum = 7
        self.volume = 0

    #This function returns a boolean expression True if the TV is on.
    def turn_on(self):
        self.is_on = not self.is_on
    
    #This function returns a boolean expression False if the TV is on.
    def turn_off_tv(self):
        self.off = False    
    
    #This function returns the channel of TV.

    #This means that the current channel will be changed if new channel is within the range 1-120
    def set_channel(self, new_channel):
        if new_channel in self.channel_list:
            self.channel_index = self.channel_list.index(new_channel)

    #This function increment the channel by one. If previous channel is 23, the new channel will be 24.
    def channel_up(self):
        if not self.is_on:
            return
        self.channel_index += 1
        if self.channel_index > self.number_channel:
            self.channel_index = 0
    
    #This function decrement the channel by one. If previous channel is 23, the new channel will be 22.
    def channel_up(self):
        if not self.is_on:
            return
        self.channel_index -= 1
        if self.channel_index < self.number_channel:
            self.channel_index = self.number_channel - 1

    #This means that the current volume will be changed if new volume is within the range 1-7
   
    
    #This function increment the channel by one. If previous volume is 3, the new channel will be 4.
    def volume_up(self):
        if not self.is_on:
            return
        if self.volume < self.volume_maximum:
            self.volume += 1
    
    #This function decrement the channel by one. If previous volume is 3, the new channel will be 2.
    def volume_down(self):
        if not self.is_on:
            return
        if self.volume > self.volume_maximum:
            self.volume -= 1

    def display_result(self):
            print("TV's channel is", self.channel_list[self.channel_index], 
            "and volume level is", self.volume)



        