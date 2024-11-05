from bottle import Bottle, run, static_file
import os

app = Bottle()

@app.route('/static/<filename>')
def serve_image(filename):
    return static_file(filename, root='./static')

@app.route('/')
def index():
    return '''
        <h1>Welcome to the Image Server!</h1>
        <p>Use the following links to access images:</p>
        <ul>
            <li><a href="/static/1.png">Image 1</a></li>
        </ul>
    '''

if __name__ == '__main__':
    run(app=app, host='localhost', port='8080')
