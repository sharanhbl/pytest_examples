
import pytest


"""
Parameterizing of a test is done to run the test against multiple sets of inputs. We can do this by using the following marker −

@pytest.mark.parametrize
"""

@pytest.mark.parametrize("num1, num2, expected", [(1,1,1), (2,2,4), (3,4,12), (2,6,12), (4,4,16)])
def test_multiplication(num1, num2, expected):
    assert num1 * num2 == expected


# parametrized fixture
# A parametrized fixture runs every test that uses it once per parameter. You define the values with params=[...]
# and read the current one from request.param

@pytest.fixture(params=["mysql", "postgresql", "sqlite"])
def connect_db(request):
    return request.param

def test_run_query(connect_db):
    print(f"\nconnected to {connect_db}")

