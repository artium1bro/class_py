import unittest
from car import Car


class test_car(unittest.TestCase):

    def setUp(self):
        self.x = Car()


    def test_get_speed(self):
        '''
        :name artium broavrnik
        :date 32.1.2023
        :desc- th func culc your speed by gear
        : params - gear
        :return: - speed
        '''
        try:
            self.assertEqual(self.x.get_speed(1), 30)
            self.x.write_to_log_file(f'Passed (test_get_speed): params ,{30}')
        except AssertionError as error:
            self.x.write_to_log_file(f'Failed (test_get_speed):{error}')


    def test_speed(self):
        '''
        :name artium brovarnik
        :desc- th func culc your speed by gear
        : params - gear
        :return: - speed
        '''
        try:
            self.assertEqual(self.x.get_speed(3) ,90)
            self.x.write_to_log_file(f'Passed (test_speed : params {90}')
        except AssertionError as error:
            self.x.write_to_log_file(f'Failed (test_speed):{error}')


    def test_start_drive(self):
        '''
        name : artium brovarnik
        date : 23.1.2023
        desc : check if func - start set - gear and speed 0 | check if exist feul
        '''

        try:
            self.x.speed = 60
            self.assertEqual(self.x.start(), 0)
            self.x.write_to_log_file(f'Passed (test_start_drive')
        except AssertionError as error:
            self.x.write_to_log_file(f'Failed (test_start_drive):{error}')


    def test_close(self):
        '''
        name : artium brovarnik
        date : 23.1.2023
        desc : check if  close func set gear = 0
        '''
        try:
            self.x.gear = 2
            self.x.close()
            self.assertEqual(self.x.gear,0)
            self.x.write_to_log_file(f'Passed (test_close)')
        except AssertionError as ass:
            self.x.write_to_log_file(f'Failed (test_close): {ass}')

    def test_how_much_liter_to_destination(self):
        '''
        name : artium brovarnik
        date : 23.1.2023
        desc : check if func culc liters by km
        '''
        try:
            self.assertEqual(self.x.how_much_liter_to_destination(100),5)
            self.x.write_to_log_file(f'Passed (test_how_much_liter_to_destination)')
        except AssertionError as ass:
            self.x.write_to_log_file(f'Failed (test_how_much_liter_to_destination): {ass}')


    def test_money_after_buying_fuel(self):
        '''
        name : artium brovarnik
        date : 23.1.2023
        desc : check if func money status after buying feul
        '''
        try:
            self.assertEqual(self.x.buy_benzin(10),400)
            self.x.write_to_log_file(f'Passed (test_money_after_buying_fuel params: {10})')
        except AssertionError as ass:
            self.x.write_to_log_file(f'Fail (test_money_after_buying_fuel: {ass}')


    def test_gear_by_speed(self):
        '''
        name : artium brovarnik
        date : 23.1.2023
        desc : check if func return  gear by get speed
        '''
        try:
            self.assertEqual(self.x.get_gear_by_speed(200),6)
            self.x.write_to_log_file(f'Passed test_gear_by_speed: {200})')
        except AssertionError as ass:
            self.x.write_to_log_file(f'Fail test_gear_by_speed: {ass}')

    def test_fuel_to_drive(self):
        '''
        :name artium brovarnik
        :data 23.1.23
        desc: check if you can drive some distanse , if not buy benzin and check money amount
        '''
        try:
            self.assertEqual(self.x.feul_for_drive(2000),0)
            self.x.write_to_log_file(f'Passed test_gear_by_speed: {1500})')
        except AssertionError as ass:
            self.x.write_to_log_file(f'Fail test_gear_by_speed: {ass}')




if __name__ == '__main__':
    unittest.main()
