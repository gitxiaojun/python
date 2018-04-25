×°ÊÎÆ÷Á·Ï°


import time

def timer(func):
    def deco():
        start_time=time.time()
        func()
        stop_time = time.time()
        print('the func run time is %s' %(stop_time - start_time))
    return deco

@timer
def test1():
    time.sleep(3)
    print('in the test1')

@timer
def test2():
    time.sleep(3)
    print('in the test2')

test1()
test2()



×°ÊÎÆ÷´«²Î
import time

def timer(func):
    def deco(*args, **kwargs):
        start_time=time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print('the func run time is %s' %(stop_time - start_time))
    return deco

@timer
def test1():
    time.sleep(3)
    print('in the test1')

@timer
def test2(name,age):
    time.sleep(3)
    print('in the test2', name,age)

test1()
test2('zhangsan', 30)



×°ÊÎÆ÷Éý¼¶°æ
import time

user,passwd = 'zhangsan','abc'
def auth(auth_type):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            if auth_type == 'local':
                username = input('Username:').strip()
                password = input('Password:').strip()
                if user == username and passwd == password:
                    print('\033[32;1mUser has passwd authentication\033[0m')
                    res = func(*args, **kwargs)
                    print('---after authenticaion')
                    return res
                else:
                    exit('\033[31;1mInvalid username or passwd \033[0m')
            elif auth_type == 'ldap':
                print('no ldap')
        return wrapper
    return outer_wrapper
# @auth()
def index():
    print('welcome to index page')
    return 'from index'

@auth(auth_type="local")
def home():
    print('welocme to home page')

@auth(auth_type="ldap")
def bbs():
    print('welcome to bbs page')

index()
print(home())
bbs()