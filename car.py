from dotenv import load_dotenv
import datetime
import os

class Car():
    load_dotenv()

    def __init__(self):    #constractor
        self.feul = int(os.getenv('feul'))
        self.feulco =  float(os.getenv('feulco'))
        self.money =   int(os.getenv('money'))
        self.gear =    int(os.getenv('gear'))
        self.speed =   int(os.getenv('speed'))
        self.status = int(os.getenv('status'))

    def start(self):
        '''
        :name : artium
        : date : 23.1
        :desc : the func start the car and do ->  gear up from 0 to 1
        :return : car status 1/0
        '''
        if  self.status ==0 :
            if self.feul > 0:
                self.status = 1
                self.gear  = 0
                return self.status
        else:
            return 'car alredy driven  '


    def close(self):
        '''
        :name : artium brovarnik
        date : 23.1.23
        desc : the func close the car -> gear,speed,status = 0
        :return: car status
        '''
        if self.status !=0:
            self.gear = 0
            self.speed = 0
            self.status = 0
            return self.status
        else :
            return 'the car alredy in turned off'


    def get_speed(self,gear):
        '''
        :name : artium brovarnik
        :date : 24.1.23
        :param gear:
        :return: speed of the car
        '''
        x = os.getenv(f'max_gear')
        if (gear>int(os.getenv('max_gear')) or gear < 0):
            raise ValueError(x.format(os.getenv('error_value_range')))

        else:
            self.speed = gear * int(os.getenv('mph'))
            return self.speed


    def how_much_liter_to_destination(self,destination):
        '''
        : desc : the func culc how much liters feul we need by distans
        :param destination
        :return: liters by km
        '''
        return destination / int(os.getenv('feulco'))


    def drive(self,km):
        '''
        :desc : the func get km and culc how much fuel you have after driving
        :param km that you want drive:
        :return: feul amount after drive
        '''
        if  self.status ==0:
            self.start()
        if self.feul > self.how_much_liter_to_destination(km):
            self.feul= self.feul- self.how_much_liter_to_destination(km)
        elif self.feul < self.how_much_liter_to_destination(km):
            self.feul_for_drive(km)
        else:
            raise OverflowError( os.getenv('er_feu'))


    def feul_for_drive(self,km):
        '''
        :name artium brovarnik
        :data 23.1.23
        desc: calc if you have feul to this distance , if not buy and update your money
        :param km
        :return: money after buying
        '''
        if (self.feul< self.how_much_liter_to_destination(km)):

            liter_ineed_buy = self.how_much_liter_to_destination(km) - self.feul
            if (self.money>= liter_ineed_buy*int(os.getenv('liter_price'))):
                self.buy_benzin(liter_ineed_buy)
                return self.money
            else:
                raise(os.getenv('error_value_money'))
        else:
            self.feul = self.feul- self.how_much_liter_to_destination(km)
            return self.money


    def buy_benzin(self,liter):
        '''
        :name: artium brovarnik
        :date : 23.1.23
        :desc: calc how much money i have after buying fuel , check that you have this sum of money
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
        :return: your gear level
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
        : name : artium brovarnik
        : date : 23.1.23
        decs : the func add 1 to gear , check that cannot up from level 6
        :return: gear level
        '''
        if self.gear ==int(os.getenv('max_gear')):
            x = os.getenv(f'error_value_maxGear')
            raise OverflowError(x.format(int(os.getenv('max_gear'))))
        else:
            if (self.status==1):
                self.gear = self.gear+1
                self.speed = self.speed +int(os.getenv('mph'))
                return self.gear
            else: raise ValueError(os.getenv('error_value_startcar'))


    def write_to_log_file(self,str):
        """
        : name : artium brovarnik
        :date : 23.1.23
        :desc : write all test result Pass / Fail  in log file
        :param str :string that describe the error
        :return: new line in log file
        """
        f= open('logfsfile.txt', 'a')
        f.write(f"{str}, {datetime.datetime.now()}, \n")
        f.close()
