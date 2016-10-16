from bottle import *

app = Bottle()

@app.get('/<name>')
@view('template/index.html')
def hi(name=''):
    return {'name': name}

@app.get('/')
@view('template/index.html')
def root():
    return {'name': 'Guest'}
