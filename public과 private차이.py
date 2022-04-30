class cTest1():# public
    __test_var__ ='public'
    def __init__(self):
        print('Create public')

class cTest2(): # private
    __test_var  = 'private'
    def __init__(self):
        print('Create private')
    def change_var(self, **extra_datas):
        

class cTest3(): # protected
    _test_var  = 'protected'
    def __init__(self):
        print('Create protected3')

if __name__ == '__main__':
    t1 = cTest1()
    t2 = cTest2()
    t3 = cTest3()

    print(t1.__test_var__)
    print(t3._test_var) # protected
    print(t2.__test_var) # private 변수를 뺏으므로 오류
