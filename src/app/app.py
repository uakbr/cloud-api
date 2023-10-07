```python
# src/app/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Initialize Flask application
app = Flask(__name__)

# Set configuration from Config class
app.config.from_object(Config)

# Initialize SQLAlchemy with app
db = SQLAlchemy(app)

# Import and register blueprints
from .controllers import api_controller, auth_controller

app.register_blueprint(api_controller.bp)
app.register_blueprint(auth_controller.bp)

if __name__ == "__main__":
    app.run(host=Config.APP_HOST, port=Config.APP_PORT)
```
