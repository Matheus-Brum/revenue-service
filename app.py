from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from api.routes.routes import health
from swagger_ui import api_doc
from handler.revenueServiceHandler import Revenues, Revenue

app_url_prefix: str = '/v1'
app: Flask = Flask(__name__)
api: Api = Api(app, prefix=app_url_prefix)
CORS(app)

app.register_blueprint(health, url_prefix=app_url_prefix)
api.add_resource(Revenues, '/revenues')
api.add_resource(Revenue, '/revenues/<revenue_id>')
api_doc(app, config_path='./docs/openapi/revenueApiDefinition.yaml',
        url_prefix=app_url_prefix + '/api/doc', title='API doc')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
