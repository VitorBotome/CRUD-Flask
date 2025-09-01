import pytest
import requests

BASE_URL ='http://127.0.0.1:5000'

tasks = []

def test_create():
    new_task_data = {
        "title": "nova tarefa",
        "description": "descrição nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)  # transformando a resposta em json

    assert response.status_code == 200 # Se voltar 200 OK
    response_json = response.json() #transformando em uma lista em python
    assert "message" in response_json # verifica se tem a chave dentro de response_json
    assert "id" in response_json
    tasks.append(response_json['id'])

def test_get_tasks():
    # requests envia uma requisiçao http do tipo get
    response = requests.get(f"{BASE_URL}/tasks") # url de destino

    assert response.status_code == 200

    response_json = response.json()

    assert "tasks" in response_json
    
def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}") # url de destino
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json['id']

def test_update_taska():
    if tasks:
        task_id = tasks[0]

        payload = {
            "title": "Novo  titulo",
            "description": "Nova descriçao",
            "completed": True
        }

        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload) # url de destino
        response_json = response.json()

        assert response.status_code == 200
        assert "message" in response_json

        response = requests.get(f"{BASE_URL}/tasks/{task_id}") # url de destino
        response_json_get = response.json()
        assert response.status_code == 200

        assert response_json_get['title'] == payload['title']
        assert response_json_get['description'] == payload['description']
        assert response_json_get['completed'] == payload['completed']

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        response.status_code == 200

        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        response.status_code == 404



