import bottle
import json

'''
get
post
patch
'''


@bottle.route('/')
def home_page():
    mythings = ['apple', 'orange', 'banana', 'peach']
    # return bottle.template('hello_world', username='Andrew', things=mythings)
    return bottle.template('hello_world', {'username':"Nirmal", 'things':mythings})

@bottle.post('/favorite_fruit')
def favorite_fruit():
    fruit = bottle.request.forms.get("fruit")
    if (fruit == None or fruit == ""):
        fruit="No fruit selected"

    return bottle.template('fruit_selection.tpl', {'fruit': fruit})


@bottle.get("/get_fruits")
def get_fruits():
    mythings = {"fruits" : ['apple', 'orange', 'banana', 'peach']}
    return mythings



bottle.debug(True)
bottle.run(host='localhost', port=7777)
