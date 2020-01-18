from chalice import Chalice
from chalicelib import hello



#####
# chalice app configuration
#####
app = Chalice(app_name='CapstoneBoilerplate')
#app.debug = True 

@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/Matt', cors = True)
def greetMatt():
    greeting = hello.Hello("Matt")
    return greeting.hello() 

@app.route('/Seann', cors = True)
def greetSeann():
    greeting = hello.Hello("Seann")
    return greeting.hello()

@app.route('/Isaac', cors = True)
def greetIsaac():
    greeting = hello.Hello("Isaac")
    return greeting.hello()