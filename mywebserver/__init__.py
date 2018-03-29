from flask import Flask
import logging
 
def main() :
    logging.basicConfig(filename='mywebserver.log', level=logging.INFO)
    app = Flask(__name__)
 
    @app.route('/', methods=['GET'])
    def index():
        return '<h1>this is the index page</h1>'
 
    app.run(host='0.0.0.0', port=8080)
 
if __name__ == '__main__':
    main()
