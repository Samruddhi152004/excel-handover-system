from flask import Flask
from flask_cors import CORS
from config import Config
from models.handover import db
from routes.records import records_bp
from routes.dashboard import dashboard_bp
from routes.export import export_bp

app=Flask(__name__)
app.config.from_object(Config)
CORS(app)
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(records_bp,url_prefix='/api')
app.register_blueprint(dashboard_bp,url_prefix='/api')
app.register_blueprint(export_bp,url_prefix='/api')

if __name__=='__main__':
    app.run(debug=True)

@app.route("/")
def home():
    return{
        "message" : "Handover Backend Running Successfully"
    }