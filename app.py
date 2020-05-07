from flask import Flask
from config import ConfigFactory
from core.routes import register_routes
from core.docs import register_swagger_routes
from storage import register_storage

app = Flask(__name__)

# load configuration
configuration = ConfigFactory().get(app.config['ENV'])
app.config.from_object(configuration)

# define data source and create API endpoints
register_storage(app)
register_routes(app)


if app.config['ENV'] != 'testing':
    register_swagger_routes(app)

if __name__ == '__main__':
    app.run()
