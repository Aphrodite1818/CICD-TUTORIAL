
from ast import Delete
from typing import Literal
from typing import Any
from colorama import Fore , init

init(autoreset = True)
def get_weather(Temp : float) -> Literal['hot'] | Literal['cold']:
    if Temp > 30 :
        print(Fore.RED + "the weather is hot")
        return "hot"
    

    print(Fore.BLUE + "cold")
    return "cold"




def add(a : int , b : int) -> int:
    print(Fore.GREEN + "Number added successfully")
    return (a + b)



def divide(a : int , b : int) -> float:
    try:
        result = a / b
        print(Fore.GREEN + "number divided successfully")
        return result
    except:
        print(Fore.RED + "error ")
        raise ZeroDivisionError("cannot divide by zero")
    


class Usermanager:
    def __init__(self):
        self.users = {}

   
    def add_users(self, username : str , email : str):
        if username in self.users:
            raise ValueError("username already taken")
        
        self.users[username] = email
        return True
    
    def get_user(self , username)-> Any | None:
        return self.users.get(username)



class NotFoundErr(Exception):
    pass

class PostgresDataBase:
    """simulates a basic user database"""

    def __init__(self) -> None:
        self.data = {}


    def add_user(self , user_id : int, name : str) -> bool:
        if user_id in self.data:
            raise ValueError("user_id already exists")
        
        self.data[user_id] = name
        return True


    def get_user(self , user_id)-> Any | None:
        if user_id not in self.data:
            raise NotFoundErr(f"user with this id {user_id} does not exist")
        

        result = self.data.get(user_id)
        return result
    

    def delete_user(self , user_id) -> bool:
        if user_id not in self.data:
            raise NotFoundErr(f"user with this id {user_id} does not exist")
        

        del self.data[user_id]
        return True
    



def is_even(n) -> Literal['even'] | Literal['odd']:
    if n % 2 ==0:
        return "even"
    return "odd"





def charge_account(amount , bank) -> Literal['completed']:
    return "completed"

def make_payment(amount , bank):
    charge_account(amount , bank)

    return "payment made"

