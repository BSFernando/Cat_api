from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_main():
    value_main = client.get('/')
    assert value_main.status_code == 200

def test_post_three():
    value_post_three = client.post('/include-three', json=[
        {
            "breed": "gato1",
            "location_of_origin": "RS",
            "coat_length": 12.5,
            "body_type": "large",
            "pattern": "pattern1"
        },
        {
            "breed": "gato2",
            "location_of_origin": "RS",
            "coat_length": 23.5,
            "body_type": "medium",
            "pattern": "pattern2"
        },
        {
            "breed": "gato2",
            "location_of_origin": "RS",
            "coat_length": 7.5,
            "body_type": "medium",
            "pattern": "pattern3"
        }
        ])
    assert value_post_three.status_code == 201

def test_post_one():
    value_post_one = client.post('/include', json=
        {
        "breed": "gato4",
        "location_of_origin": "RS",
        "coat_length": 6.5,
        "body_type": "small",
        "pattern": "pattern1"
        })
    assert value_post_one.status_code == 201

def test_search_all():
    value_all = client.get('/cats')
    assert value_all.status_code == 202

def test_filter():
    value_filter = client.get('/filter-cats?breed=gato1&sort=-coat_length')
    assert value_filter.status_code == 202

def test_update():
    value_filter = client.put('/change?id=1', json={
        "breed": "gato2",
        "location_of_origin": "RS",
        "coat_length": 12.5,
        "body_type": "small",
        "pattern": "pattern2"
    })
    assert value_filter.status_code == 202

def test_patch():
    value_filter = client.put('/change-parameters', json={
        "item": {
            "location_of_origin": "RS"
        },
        "mudar": {
            "location_of_origin": "SC",
        }})

def test_delete_id():
    value_delete = client.delete('/delete-id?id=1')
    assert value_delete.status_code == 200

def test_delete_by_par():
    value_delete_par = client.delete('/delete?pattern=pattern1&location_of_origin=RS')
    assert value_delete_par.status_code == 200
    
def test_delete_by_par_one():
    value_delete_par_one = client.delete('/delete?location_of_origin=RS')
    assert value_delete_par_one.status_code == 200