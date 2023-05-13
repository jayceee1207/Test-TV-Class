#John Carlo Ablay
#Test TV Class
#May 13, 2023

#Create class named TV
class TV:
    def __init__(self, turn_on, volume_level):
        self.turn_on = turn_on
        self.volume_level = volume_level

#Test Driver program TestTV
television_1 = TV('On')

print(television_1.turn_on)
