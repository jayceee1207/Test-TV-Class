#John Carlo Ablay
#Test TV Class
#May 13, 2023



from TV import TV


class TVTest:

    def __init__ (self):

        self.tv1 = TV()
        self.tv2 = TV()

    def result(self):
        print ("tv1's channel is", self.tv1.get_tv_channel(), "and volume level is", self.tv1.get_tv_volume())
        print ("tv2's channel is", self.tv2.get_tv_channel(), "and volume level is", self.tv2.get_tv_volume())




