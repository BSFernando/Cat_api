# API_cat CRUD

A API disponibilizidade no link "https://api-cat.herokuapp.com/"

## Métodos
Requisições para a API devem seguir os padrões:
| Método | Descrição |
|---|---|
| `GET` | Retorna informações de um ou mais registros. |
| `POST` | Utilizado para criar um novo registro. |
| `PUT` | Atualiza ou altera dados de um registro. |
| `PATCH` | Atualiza ou altera parcialmente dados de um registro. |
| `DELETE` | Remove um registro do banco de dados. |


## Respostas
| Código | Descrição |
|---|---|
| `200` | Requisição executada com sucesso.|
| `201` | Registro criado com sucesso.|
| `202` | Requisição aceita com sucesso.|
| `400` | Erros de validação ou os campos informados não existem no sistema.|
| `422` | Dados informados estão fora do escopo definido para o campo.|

## POST

* Corpo da requisição deve conter uma lista com três registros
```python
import requests

incluir_tres = requests.post('https://api-cat.herokuapp.com/include-three', json=[
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
            "breed": "gato3",
            "location_of_origin": "RS",
            "coat_length": 7.5,
            "body_type": "medium",
            "pattern": "pattern3"
        }
        ])
```

* Corpo da requisição deve conter apenas um registro
```python
import requests

incluir_um = requests.post('https://api-cat.herokuapp.com/include', json=
        {
        "breed": "gato4",
        "location_of_origin": "RS",
        "coat_length": 6.5,
        "body_type": "small",
        "pattern": "pattern1"
        })
```

## GET

* /cats?limit=5 para limitar busca a apenas 5 itens
* /cats?sort=breed ou -breed para ordenar de forma crescente ou descrescente
```python
import requests

buscar_todos = requests.get('https://api-cat.herokuapp.com/cats')
```

* /filter-cats?limit=5 para limitar busca a apenas 5 itens
* /filter-cats?sort=breed ou -breed para ordenar de forma crescente ou descrescente
* /filter-cats?breed=gato1 seleciona apenas registros com breed==gato1
```python
import requests

buscar_parametro = requests.get('https://api-cat.herokuapp.com/filter-cats?breed=gato1&sort=-coat_length')
```

## PUT

* altera todos os parametros de acordo com o id 
```python
import requests
alterar_um = requests.put('https://api-cat.herokuapp.com/change?id=1', json={
        "breed": "gato10",
        "location_of_origin": "RS",
        "coat_length": 12.5,
        "body_type": "small",
        "pattern": "pattern2"
    })
```

## PATCH

* altera o parametro de todos os registros independente do id 
```python
import requests
alterar_parametros = requests.patch('https://api-cat.herokuapp.com/change-parameters', json={
        "item": {
            "location_of_origin": "RS"
        },
        "mudar": {
            "location_of_origin": "SC"
        }})
```

## DELETE

* deleta registro de acordo com o id 
```python
import requests
deletar_id = requests.delete('https://api-cat.herokuapp.com/delete-id?id=1')
```

* deleta todos os registros independente do id 
```python
import requests
deletar_parametros = requests.delete('https://api-cat.herokuapp.com/delete?pattern=pattern1&location_of_origin=SC')
```

# Instalar e testar (local)

* Clone o repositório  cat_api localmente

```bash
/git init
```
```bash
/git clone https://github.com/BSFernando/cat_api.git
```

* Execute requirements.txt

```bash
/pip install -r requirements.txt
```

* Executar a api localmente

```bash
/main.py
```

* Executar teste

```bash
/pytest test_api.py
```