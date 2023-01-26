from car import Car
import pytest

@pytest.fixture()
def car():
    return Car()


def test_feul_for_drive(car):
    try:
        car.feul_for_drive(1500)
        assert car.money == 250
        car.write_to_log_file(f'Passed (test_drive) params : {1500} ')
    except AssertionError as error:
        car.write_to_log_file(f'Failed (test_drive) params : {100} , {error} ')


def test_drive(car):
    '''
    :name : artium brovarnik
    date: 23.1.23
    desc: the test check if feul level down after drive
    '''
    try:
        car.drive(2000)
        assert car.money ==10
        car.write_to_log_file(f'Passed (test_drive) params : {100} ')
    except AssertionError as ae:
        car.write_to_log_file(f'Failed (test_drive) params : {100} , {ae} ')


def test_buy_feul_positive(car):
    '''
    :name : artium brovarnik
    date: 23.1.23
    desc: the test check if your money amount after buying feul is correct
    '''
    try:
        car.buy_benzin(10)
        assert car.money == 400
        car.write_to_log_file(f'Passed (test_buy_feul_positive) params : {10} ')
    except AssertionError as ae:
        car.write_to_log_file(f'Failed (test_buy_feul_positive) {ae} ')


def test_buy_feul_negative(car):
    '''
    :name : artium brovarnik
    date: 23.1.23
    desc: the test sure that your money amount after buying feul is incorrect
    '''
    try:
        car.money = 1000
        with pytest.raises(ValueError):
            car.buy_benzin(101)
            car.write_to_log_file(f'Passed test_buy_feul_negative:params: {101})')
    except AssertionError as ae :
        car.write_to_log_file(f'Failed test_buy_feul_negative, {ae}:')


def test_get_speed_by_gear_positive(car):
    '''
    :name : artium brovarnik
    date: 23.1.23
    desc: the test check if your speed correct by gear
    '''
    try:
        assert car.get_speed(5)==150
        car.write_to_log_file(f'Passed test_get_speed_by_gear_positive. params: {5})')
    except AssertionError as error:
        car.write_to_log_file(f'Failed test_get_speed_by_gear_positive) {error}')


def test_speed_by_gear(car):
    '''
    :name : artium brovarnik
    date: 23.1.23
    desc: the test sure that you cannot enter negative gear
     '''
    with pytest.raises(ValueError):
        car.get_speed(-1)
    car.write_to_log_file(f'Passed (speed_by_gear test)')


def test_close_car(car):
    '''
    :name : artium brovarnik
    date: 23.1.23
    desc: the test check if func close_car work -> gear =0
    '''
    try:
        car.gear = 6
        car.close()
        assert car.gear == 1
        car.write_to_log_file(f'Passed (test_close_car)')
    except  AssertionError as error:
        car.write_to_log_file(f'Failed test_close_car {error}')


def test_gear_not_in_range(car):
    '''
    :name : artium brovarnik
    date: 23.1.23
     desc: the test sure that max level gear is max 6 and cannot get number more 6
     '''
    with pytest.raises(ValueError):
        car.get_speed(7)
    car.write_to_log_file('PASS test_gear_not_in_range ')


def test_gear_by_speed_negative(car):
    '''
    :name : artium brovarnik
    date: 23.1.23
    desc : the func sure if you get error  by speed
    '''
    with pytest.raises(ValueError):
        car.get_gear_by_speed(0)
    car.write_to_log_file(f'Passed (gear_by_speed_negative test)')


def test_gear_by_speed_positive(car):
    '''
    :name : artium brovarnik
    date: 23.1.23
    desc : the func test if you get currect gear by speed
    '''
    try:
        assert  car.get_gear_by_speed(95)==4
        assert  car.get_gear_by_speed(35)==2
        assert  car.get_gear_by_speed(1)== 1
        car.write_to_log_file(f'Passed (test_gear_by_speed_positive)')
    except AssertionError as error:
        car.write_to_log_file(f'Failed (test_gear_by_speed_positive) {error}')


def test_gear_up(car):
    '''
    :name : artium brovarnik
    date: 23.1.23
    desc : the func test if the gear is up -> +1
    '''
    try:
        car.start()
        car.gear = 5
        car.gear_up()
        assert car.gear == 6
        car.write_to_log_file(f'Passed (test_gear_up)')
    except AssertionError as error:
        car.write_to_log_file(f'Failed (test_gear_up) {error}')


def test_gear_up_negative(car):
    '''
    :name : artium brovarnik
    date: 23.1.23
    desc : the func sure if you get error when you try up gear more than max_gear
    '''
    with pytest.raises(OverflowError):
        car.start()
        car.gear = 6
        car.gear_up()
    car.write_to_log_file('pass ,test_gear_up_negative')


def test_start_car(car):
    '''
    name: artium brovarnik
    date: 23.1.23
    desc : the func check if start car change status from 0 to 1
    :return: status 1\0
    '''
    try:
        car.start()
        assert car.status == 1
        car.write_to_log_file(f'Passed (test start_car)')
    except AssertionError as error:
        car.write_to_log_file(f'Failed (test_start_car) {error}')


def test_turned_off_car(car):
    '''
    name: artium brovarnik
    date: 23.1.23
    desc : the func check if torn off car change status from 1 to 0 and speed / gear = 0
    :return: status 1\0
    '''
    try:
        car.status = 1
        car.speed = 100
        car.close()
        assert car.status == 0
        assert  car.speed == 0
        car.write_to_log_file(f'Passed (turned_off_car)')
    except AssertionError as error:
        car.write_to_log_file(f'Failed (turned_off_car) {error}')


def test_how_much_liter_by_distance(car):
    '''
    name: artium brovarnik
    date: 23.1.23
    desc : the func check if A correct calculation of the fuel amount by km
    :return: status fuel liters
    '''
    try:
        assert car.how_much_liter_to_destination(100)==5
        car.write_to_log_file(f'Passed (how_much_liter_by_distance)')
    except AssertionError as error:
        car.write_to_log_file(f'Failed (how_much_liter_by_distance) {error}')








