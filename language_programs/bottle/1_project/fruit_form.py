import bottle

#https://bottlepy.org/docs/dev/

@bottle.route('/')
def home_page():
    mythings = ['apple', 'orange', 'banana', 'peach']
    return bottle.template('hello_world', {'username':"Nirmal", 'things':mythings})

@bottle.post('/favorite_fruit')
def favorite_fruit():
    fruit = bottle.request.forms.get("fruit")
    if (fruit == None or fruit == ""):
        fruit="No fruit selected"

    bottle.redirect("/show_fruit")

@bottle.route('/show_fruit')
def show_fruit():
    fruit = bottle.request.get_cookie("fruit")

    return bottle.template('fruit_selection.tpl', {'fruit':fruit})

#bottle.debug(True)
bottle.run(host='localhost', port=7777)
