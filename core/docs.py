import json
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint


def register_swagger_routes(app):
    # get file name without the forward slash
    json_file_name = app.config['API_DOCS_URL'][1:]

    # regenerate swagger.json every time we start the server
    swag = swagger(app)
    swag['info']['version'] = "1.0.0"
    swag['info']['title'] = "Key-Value storage API"
    swag['servers'] = {
        'url': ['/']
    }

    with open(json_file_name, 'w') as swagger_file:
        json.dump(swag, swagger_file)

    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        app.config['SWAGGER_URL'],
        app.config['API_DOCS_URL'],
        config={
            'app_name': "Documentation"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT,
                           url_prefix=app.config['SWAGGER_URL'])
