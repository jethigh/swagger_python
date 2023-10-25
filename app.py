import flask
from flask import Flask
from flask_restx import Api, Namespace, Resource, fields

app = flask.Flask(__name__)

api = Api(doc='/api/doc/')
api.init_app(app, title='dot-ldap-api', description='First, test swagger UI in Python')
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
app.config.SWAGGER_UI_OPERATION_ID = True
app.config.SWAGGER_UI_REQUEST_DURATION = True

@app.route("/hello")
def hello_world():
  return "Hello, World!"

@app.route("/hello/<name>")
def hello_name(name):
    return "Hello " + name


@api.route('/hello')
@api.doc(description="Hello world a co? ")
class hello(Resource):
    def get(self):
        return {}

    def post(self, id):
        api.abort(403)

@api.route('/hello/<name>')
@api.doc(params={'name': 'Name to say hello'}, description='Returns greetings')
class name(Resource):
    def get(self):
        return {}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
