#Make a class named Class TV

class TV:


    def __init__(self):
        #Inside a function are the objects. The default of channel and volume is 1 and the default boolean expression
        #is False that indicates that the TV is off.
        self.isOn = False
        self.channel_list = [1,	2,	3,	4,	5,	6,	7,	8,	9, 10,  11,	12,	13,	14,	15,	16,	17,	18,	19, 20,
                            21,	22,	23,	24,	25,	26,	27,	28,	29, 30,	31,	32,	33,	34,	35,	36,	37,	38,	39, 40,
                            41,	42,	43,	44,	45,	46,	47,	48,	49, 50,	51,	52,	53,	54,	55,	56,	57,	58,	59, 60,
                            61,	62,	63,	64,	65,	66,	67,	68,	69, 70,	71,	72,	73,	74,	75,	76,	77,	78,	79, 80,
                            81,	82,	83,	84,	85,	86,	87,	88,	89, 90,	91,	92,	93,	94,	95,	96,	97,	98,	99, 100,
                            101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
                            117, 118, 119, 120]
        self.number_channel = len(self.channel_list)
        self.channel_index = 0
        self.volume_minimum = 0
        self.volume_maximum = 7
        self.volume = 0

    #This function returns a boolean expression True if the TV is on.
    def turn_on(self):
        self.isOn = not self.isOn
    
    #This function returns a boolean expression False if the TV is on.
    def turn_off_tv(self):
        self.off = False    
    
    #This function returns the channel of TV.

    #This means that the current channel will be changed if new channel is within the range 1-120
    def setChannel(self, new_channel):
        if new_channel in self.channel_list:
            self.channel_index = self.channel_list.index(new_channel)

    #This function increment the channel by one. If previous channel is 23, the new channel will be 24.
    def channel_up(self):
        if not self.isOn:
            return
        self.channel_index += 1
        if self.channel_index > self.number_channel:
            self.channel_index = 0
    
    #This function decrement the channel by one. If previous channel is 23, the new channel will be 22.
    def channel_up(self):
        if not self.isOn:
            return
        self.channel_index -= 1
        if self.channel_index < self.number_channel:
            self.channel_index = self.number_channel - 1

    #This means that the current volume will be changed if new volume is within the range 1-7
   
    
    #This function increment the channel by one. If previous volume is 3, the new channel will be 4.
    def volume_up(self):
        if not self.isOn:
            return
        if self.volume < self.volume_maximum:
            self.volume += 1
    
    #This function decrement the channel by one. If previous volume is 3, the new channel will be 2.
    def volume_down(self):
        if not self.isOn:
            return
        if self.volume > self.volume_maximum:
            self.volume -= 1





        