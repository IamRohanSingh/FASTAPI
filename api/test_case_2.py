import pytest
def string_cal_lenght(my_string):
        count = 0
        for _ in my_string:
            count += 1
        return count
@pytest.mark.seven
def test_module_7():
    assert string_cal_lenght("rohan")==5

def generate_string(lenght):
        string = ''
        while lenght>0:
            string += input()
            lenght -= 1
        return string
@pytest.mark.eight
def test_module_8():
    assert generate_string(5) =='rohan'                  