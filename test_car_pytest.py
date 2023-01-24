from car import Car
import pytest

@pytest.fixture()
def car():
    return Car()


def test_feul_for_drive(car):

    car.feul_for_drive(1500)
    assert car.money == 250



def test_drive(car):
    '''
    :name : artium brovarnik
    date: 23.1.23
    desc: the test check if feul level down after drive
    '''
    try:
        car.drive(20)
        assert car.feul ==49
        car.write_to_log_file(f'Passed (test_drive) params : {20} ')
    except AssertionError as ae:
        car.write_to_log_file(f'Failed (test_drive) params : {20} , {ae} ')


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


def test_gear_by_speed_negative(car):
    '''
    :name : artium brovarnik
    date: 23.1.23
    desc : the func sure if you get error  by speed
    '''

    with pytest.raises(ValueError):
        car.get_gear_by_speed(0)


def test_gear_by_speed_positive(car):
    '''
    :name : artium brovarnik
    date: 23.1.23
    desc : the func test if you get currect gear by speed
    '''
    try:
        assert  car.get_gear_by_speed(95)==4
        assert  car.get_gear_by_speed(200) ==6
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
        car.gear = 1
        car.gear_up()
        assert car.gear == 2
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
        car.gear = 6
        car.gear_up()







