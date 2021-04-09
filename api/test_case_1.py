import pytest
def factorial(n):
        return 1 if (n==1 or n==0) else n * factorial(n - 1)
@pytest.mark.four
def test_module_4():
    assert factorial(0)==1

@pytest.mark.five
def test_module_5():
    assert factorial(1)==1

@pytest.mark.six
def test_module_6():
    assert factorial(5)==120    