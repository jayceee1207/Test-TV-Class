#John Carlo Ablay
#Test TV Class
#May 13, 2023

#Create class named TV
class TV:
    def set_channel(self, set_channel):
        self.set_channel = set_channel
    def set_volume_level(self, set_volume_level):
        self.set_volume_level = set_volume_level
    def show_channel(self):
        return self.set_channel
    def show_volume_level(self):
        return self.show_volume_level
        
television_1 = TV()
television_1.set_channel(49)
television_1.set_volume_level(46)
television_1.show_channel()
television_1.show_volume_level()
print(television_1.show_channel)


        




