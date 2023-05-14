#John Carlo Ablay
#Test TV Class
#May 13, 2023



from TV import TV


class TVTest:

    def __init__ (self):

        self.tv1 = TV()
        self.tv2 = TV()

        self.tv1.get_tv_channel(23)
        self.tv1.get_tv_channel(5)

        self.tv2.get_tv_channel(110)
        self.tv2.get_tv_channel(7)

    def result(self):
        print ("tv1's channel is", self.tv1.get_tv_channel(), "and volume level is", self.tv1.get_tv_volume())
        print ("tv2's channel is", self.tv2.get_tv_channel(), "and volume level is", self.tv2.get_tv_volume())




