import sys
sys.path.insert(0, "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages")
import pympler
from pympler import asizeof
class User:
    def __init__(self, _name,_surname,_dob,_email,_password):
        self.name = _name
        self.surname = _surname
        self.dob = _dob
        self.password = _password
        self.email = _email

class reducedUser:
    __slots__ = ["name", "surname", "dob","email","password"]
    def __init__(self,_name,_surname,_dob,_email,_password):
        self.name = _name
        self.surname = _surname
        self.dob = _dob
        self.password = _password
        self.email = _email

users, rusers = [None] * 1000000, [None] * 1000000
for i in range(1000000):
    m = User("", "", "", "", 1234)
    users[i] = m
    r = reducedUser("","","","",1234)
    rusers[i] = r

print(asizeof.asizeof(users))
print(asizeof.asizeof(rusers))


    