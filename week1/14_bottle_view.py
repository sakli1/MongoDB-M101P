import bottle

@bottle.route('/')
def home_page():
    mythings = ['apple','orange','banana','peach']
    return bottle.template('14_bottle_view', username="Mike", things=mythings)

bottle.debug(True)
bottle.run(host='localhost',port=8080)

#URL: http://localhost:8080/

