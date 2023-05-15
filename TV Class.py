#John Carlo Ablay
#Test TV Class
#May 13, 2023



from TV import TV



def main():
    
    tv_1 = TV()
    tv_1.turn_on_tv()
    tv_1.get_tv_channel(23)
    tv_1.get_tv_channel(5)

    tv_2 = TV()
    tv_2.turn_on_tv()
    tv_2.get_tv_channel(102)
    tv_2.get_tv_channel(7)

    print ("tv1's channel is", tv_1.get_tv_channel(), "and volume level is", tv_1.get_tv_volume())
    print ("tv2's channel is", tv_2.get_tv_channel(), "and volume level is", tv_2.get_tv_volume())


    
