import pytest
from app import app, db, Record
from config.settings import TestConfig

@pytest.fixture
def client():
    app.config.from_object(TestConfig)  # Use TestConfig for testing
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.rollback()
            db.drop_all()

def test_home_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Success!'

def test_create_record_endpoint(client):
    data = {'name': 'John', 'age': 30}
    response = client.post('/records', json=data)
    assert response.status_code == 201

    record = Record.query.filter_by(name='John').first()
    assert record is not None
    assert record.age == 30

def test_retrieve_record_endpoint(client):
    record = Record(name='Test', age=25)
    db.session.add(record)
    db.session.commit()

    response = client.get(f'/records/{record.id}')
    assert response.status_code == 200

    data = response.get_json()
    assert data['name'] == 'Test'
    assert data['age'] == 25

def test_update_record_endpoint(client):
    record = Record(name='Old Name', age=35)
    db.session.add(record)
    db.session.commit()

    updated_data = {'name': 'New Name', 'age': 40}
    response = client.put(f'/records/{record.id}', json=updated_data)
    assert response.status_code == 200

    updated_record = Record.query.get(record.id)
    assert updated_record.name == 'New Name'
    assert updated_record.age == 40

def test_delete_record_endpoint(client):
    record = Record(name='To be deleted', age=50)
    db.session.add(record)
    db.session.commit()

    response = client.delete(f'/records/{record.id}')
    assert response.status_code == 200

    deleted_record = Record.query.get(record.id)
    assert deleted_record is None
