import pytest

"""
Fixture scopes

The scope argument controls how long a fixture instance lives, meaning how often setup runs.

Scope Setup runs once per...
function (default):  each test function
class: 	             test class
module:	             .py file
package:	         package (directory with tests)
session:             entire test run
"""
@pytest.fixture(scope="function") # default behaviour, runs for every test function.
def setup_db():
    print("\nsetting up db.. done")
    yield
    print("\nclosing db.. done")

def test_a(setup_db):
    print("\ntest a .. done")
    assert True

def test_b(setup_db):
    print("\ntest b .. done")
    assert True

@pytest.fixture(scope="class") # runs only once per test class
def setup_api():
    print("\nsetting up api.. done")
    yield
    print("\nclosing api.. done")

class TestAPI:
    def test_a(self, setup_api):
        print("\ntest a .. done")
        assert True

    def test_b(self, setup_api):
        print("\ntest b .. done")
        assert True


@pytest.fixture(scope="module") # once only once per module:: setup config once and clears config only after all test runs
def setup_config():
    print("\nsetting up config.. done")
    yield
    print("\nclearing config.. done")