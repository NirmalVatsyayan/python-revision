def check_division(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Sorry cannot divide")
         return False

      return func(a,b)
   return inner

@check_division
def divide(a,b):
    return a/b

'''
DRY - don't repeat yourself
'''

print(divide(100, 0))
