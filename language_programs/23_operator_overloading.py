
class Test(object):
    def __init__(self, value):
        self.value = value
    
    def __lt__(self, other):
        if self.value  < other.value:
            return True
        else:
            return False
    

t1 = Test(10)
t2 = Test(20)

print(t1 < t2)
