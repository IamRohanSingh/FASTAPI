import pytest
def fibonacci(number):

        if number<0:
            print("invalid")
        elif number==0:
            return 0
        elif number==1 :
            return 1
        else:
            return (fibonacci(number-1) + fibonacci(number-2))

@pytest.mark.one
def test_module_1():
    assert fibonacci(0)==0

@pytest.mark.two
def test_module_2():
    assert fibonacci(1)==1
@pytest.mark.three
def test_module_3():
    assert fibonacci(9)==34        

