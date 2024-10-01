from flask import Flask, render_template, jsonify
from db_class import AircraftModels, Manufacturer
from db_manager import Session

app = Flask(__name__)


@app.route('/')
def index():
    session = Session()
    manufacturers = session.query(Manufacturer).all()
    return render_template('index.html', manufacturers=manufacturers)


@app.route('/models/<int:manufacturer_id>')
def models(manufacturer_id):
    session = Session()
    models = session.query(AircraftModels).filter_by(manufacturer_id=manufacturer_id).all()
    model_list = [{'id': model.id, 'code': model.model_code, 'description': model.model_description} for model in models]
    return jsonify(model_list)


if __name__ == '__main__':
    app.run(debug=True)
