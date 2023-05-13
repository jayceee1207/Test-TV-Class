#John Carlo Ablay
#Test TV Class
#May 13, 2023

#Create class named TV
class Television:
    def __init__(self, turn_on):
        self.turn_on = turn_on

#Test Driver program TestTV
television_1 = Television('On')

print(television_1.turn_on)
