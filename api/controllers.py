from flask import jsonify, request
from app import app, db
from api.models import Record
from flasgger import swag_from

@app.route('/', methods=['GET'])
def health_check():
    return "Success!" 

@app.route('/records', methods=['POST'])
def create_record():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    if not name or not age:
        return jsonify({'error': 'Name and age are required'}), 400
    try:
        new_record = Record(name=name, age=age)
        db.session.add(new_record)
        db.session.commit()
        return jsonify({'message': 'Record created successfully', 'id': new_record.id}), 201
    except:
        return jsonify({'error': 'Failed to create record'}), 500

@app.route('/records/<int:id>', methods=['GET'])
def read_record(id):
    record = Record.query.get(id)
    if record:
        return jsonify({'id': record.id, 'name': record.name, 'age': record.age})
    else:
        return jsonify({'error': 'Record not found'}), 404

@app.route('/records/<int:id>', methods=['PUT'])
def update_record(id):
    data = request.json
    name = data.get('name')
    age = data.get('age')
    if not name or not age:
        return jsonify({'error': 'Name and age are required'}), 400
    record = Record.query.get(id)
    if record:
        try:
            record.name = name
            record.age = age
            db.session.commit()
            return jsonify({'message': 'Record updated successfully'})
        except:
            return jsonify({'error': 'Failed to update record'}), 500
    else:
        return jsonify({'error': 'Record not found'}), 404

@app.route('/records/<int:id>', methods=['DELETE'])
def delete_record(id):
    record = Record.query.get(id)
    if record:
        try:
            db.session.delete(record)
            db.session.commit()
            return jsonify({'message': 'Record deleted successfully'})
        except:
            return jsonify({'error': 'Failed to delete record'}), 500
    else:
        return jsonify({'error': 'Record not found'}), 404
