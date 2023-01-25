from car import Car


if __name__ == '__main__':

    x = Car()

try:
        print ("hii your car is off")
        x.start()
        print(f'now your car is started , the gear is :{x.gear} and the speed is {x.speed}')

        benz = x.how_much_liter_to_destination(100)
        print(f'if we want drive 100 km , we need {benz} liters')


        s = x.drive(120)
        print(f'we already drived 120 km , the fuel now is : {x.feul}')

        speed = x.get_speed(3)
        print(f'for example , if you drive in thirt gear , your speed is : {speed}')

        s1 = x.get_speed(6)
        print(f'if you gear is {6} , your speed is' , s1)

        m=x.buy_benzin(10)
        print(f'if you have 500 shekels and you buy {10} liter fuel , your corrent money amount is :', m )

except ValueError as e:
    print(e)
    x.write_to_log_file(e)

except TypeError as e:
    print(e)
    x.write_to_log_file(e)

except Exception as e:
    x.write_to_log_file(e)


