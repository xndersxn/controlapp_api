from flask import Flask
from flask_cors import CORS
import persons
import objects

app = Flask(__name__)
CORS(app)

# Rutas
app.register_blueprint(persons.bp, url_prefix="/persons")
app.register_blueprint(objects.bp, url_prefix="/objects")

@app.route("/")
def home():
    return {"message": "API REST ControlApp funcionando!"}

if __name__ == "__main__":
    app.run(debug=True, port=5000)
