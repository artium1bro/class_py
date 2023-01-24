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

        x.get_speed(6)

        x.buy_benzin(10)

        print(x.get_gear_by_speed(50))




except ValueError as e:
    print(e)
    x.write_to_log_file(e)

except TypeError as e:
    print(e)
    x.write_to_log_file(e)

except Exception as e:
    x.write_to_log_file(e)


