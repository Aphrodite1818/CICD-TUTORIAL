

from main import get_weather, make_payment
from main import add , divide
from main import Usermanager
from main import PostgresDataBase , NotFoundErr
from main import is_even
from main import charge_account
import pytest



def test_get_weather() -> None:
    assert get_weather(21) == "cold" 
    assert get_weather(35) == "hot" 
    assert get_weather(20) == "cold" 


def test_divide():
    assert divide(1 , 2 ) == 0.5
    with pytest.raises(ZeroDivisionError) as ext:
        divide(1 , 0 ) 
    assert str(ext.value) == "cannot divide by zero"


def test_add() -> None:
    assert add(1 , 2) == 3
    assert add(1 , 2) != 4


# @pytest.fixture
# def user_manager() -> Usermanager:
#     """creates a fresh instance of UserManager before each test"""
#     return Usermanager()

@pytest.fixture
def user_manager() -> Usermanager:
    return Usermanager()

def test_add_user(user_manager) -> None:
    assert user_manager.add_users("john_doe" , "john@example.gmail.com") == True
    assert user_manager.get_user("john_doe" ) == "john@example.gmail.com"


def test_add_duplicate_user(user_manager):
    user_manager.add_users("jbola" , "john@example.com")
    with pytest.raises(ValueError) as ext:
        user_manager.add_users("jbola" , "another@example.com")
    assert str(ext.value) == "username already taken"




@pytest.fixture
def database() -> PostgresDataBase:
    return PostgresDataBase()



def test_add_user_data(database) -> None:
    assert database.add_user(1 , "Taiwo") == True

    with pytest.raises(ValueError) as err:
        database.add_user(1 , "Kehinde")
    assert str(err.value) == "user_id already exists"



def test_get_users(database):
    database.add_user(20 , "kehinde")
    database.add_user(10 , "ola")

    assert database.get_user(20) == "kehinde"

    
    user_id = 30
    with pytest.raises(NotFoundErr) as exc:
        database.get_user(user_id)
    assert str(exc.value) == f"user with this id {user_id} does not exist"



def test_delete_user(database):
    database.add_user(1 , "ola")
    assert database.delete_user(1) == True
    with pytest.raises(NotFoundErr) as err:
        database.delete_user(2)
    assert str(err.value) == "user with this id 2 does not exist"



@pytest.mark.parametrize("n, expected", [
    (2,"even"),
    (4 , "even"),
    (3 , "odd"),
    (8,"even"),
    (25, "odd")

])
def test_is_even(n, expected):
    assert is_even(n) == expected
    print("passed")





def test_make_payment(mocker):
    mock_charge = mocker.patch("main.charge_account" ,return_value ="completed")
    assert make_payment(100 , "uba") == "payment made"
    mock_charge.assert_called_once_with(100 , "uba")
   