from dotenv import load_dotenv
import datetime
import os

class Car():
    load_dotenv()

    def __init__(self):
        self.feul = int(os.getenv('feul'))
        self.feulco =  float(os.getenv('feulco'))
        self.money =   int(os.getenv('money'))
        self.gear =    int(os.getenv('gear'))
        self.speed =   int(os.getenv('speed'))

    def start(self):
        '''
        :name : artium
        : date : 23.1
        :desc : the func start the car and do ->  gear up from 0 to 1
        :return : gear level
        '''
        if self.gear == 0:
            if self.feul > 0:
                self.gear  = 0
                return self.gear
        else:
            return 'car alredy in drive '



    def close(self):
        '''
        desc : the func close the car -> gear = 0
        :return:
        '''
        if self.gear !=0:
            self.gear = 0
            self.speed = 0
            return self.gear
        else :
            return 'the car alredy in stop status'


    def get_speed(self,gear):
        '''
        :param gear:
        :return: speed of the car
        '''
        if (gear>int(os.getenv('max_gear')) or gear < 0):
            raise ValueError(os.getenv('error_value_range'))
        else:
            self.speed = gear * int(os.getenv('mph'))
            return self.speed


    def how_much_liter_to_destination(self,destination):
        '''
        : desc : the func culc how much liters feul we need by distans
        :param destination
        :return: liters by km
        '''
        return destination // int(os.getenv('feulco'))


    def drive(self,km):
        '''
        :desc : the func get km and culc how much feul you have after
        :param km - you want drive:
        :return: feul status after drive
        '''
        if not self.start():
            self.start()
        if self.feul > (km/int(os.getenv('feulco'))):
            self.feul= self.feul- (km//int(os.getenv('feulco')))
            return self.feul
        else:
            raise OverflowError( os.getenv('er_feu'))


    def feul_for_drive(self,km):
        '''
        :name artium brovarnik
        :data 23.1.23
        desc: calc if you have feul to this distance , if not buy and update your money
        :param liter
        :return: money after buying
        '''
        if (self.feul< km/int(os.getenv('fuelco'))):

            liter_ineed = km/int(os.getenv('fuelco')) - self.feul
            if (self.money>= liter_ineed*int(os.getenv('liter_price'))):
                self.buy_benzin(liter_ineed)
                return self.money
            else:
                raise(os.getenv('error_value_money'))
        else:
            self.feul = self.feul- km/int(os.getenv('fuelco'))
            return self.money





    def buy_benzin(self,liter):
        '''
        desc: calc how much money i have after buying fuel , check that you have this sum of money
        :param liter
        :return: money after buying
        '''
        money_i_need = liter*int(os.getenv('liter_price'))
        if self.money >= money_i_need:
            self.money = self.money - money_i_need
            return self.money
        else:
            raise ValueError(os.getenv('error_value_money'))


    def get_gear_by_speed(self,sp):
        '''
        desc: func return your gear by speed
        :param sp:
        :return: yout gear level
        '''

        if sp<=0:
            raise ValueError(os.getenv('error_value_speed'))
        elif sp > 0 and sp<30:
            return 1
        elif sp>30 and sp<=60:
            return 2
        elif sp>60 and sp<=90:
            return 3
        elif sp>90 and sp<=120:
            return 4
        elif sp>120 and sp<=150:
            return 5
        else: os.getenv('max_gear')

    def gear_up(self):
        '''
        decs : the func add 1 to gear , check that cannot up from level 6
        :return: gear level
        '''

        if self.gear ==int(os.getenv('max_gear')):
            x = os.getenv(f'error_value_maxGear')
            raise OverflowError(x.format(int(os.getenv('max_gear'))))
        else:
            self.gear = self.gear+1
            self.speed = self.speed +int(os.getenv('mph'))
            return self.gear



    def write_to_log_file(self,str):
        """
            :desc : write all exceptions to log file
            :param str :string that describe the error
            :return: new line in log file
        """
        f= open('D:/pythonProject/class/logfsfile.txt', 'a')
        f.write(f"{str}, {datetime.datetime.now()}, \n")
        f.close()
