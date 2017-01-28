'''
helps implementing callback
it is a function which returns another function
'''
'''
def greet(name):
   return "Hello " + name 

def call_func(func):
    other_name = "John"
    return func(other_name)  

print(call_func(greet))

def p_decorate(func):
   def func_wrapper(name):
       print("inside function wrapper ",name)
       print(func(name))
       return "<p>{0}</p>".format(func(name))
   print("going to return")
   return func_wrapper

@p_decorate
def get_text(name):
   print("inside get_text ",name)
   return "lorem ipsum, {0} dolor sit amet".format(name)

print(get_text("John"))
'''
def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   print("inside p_decorate")
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    print("inside strong_decorate")
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    print("inside div_decorate")
    return func_wrapper
    
@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print(get_text("John"))
