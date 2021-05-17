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

```python
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


incluir_um = requests.post('https://api-cat.herokuapp.com/include', json=
        {
        "breed": "gato4",
        "location_of_origin": "RS",
        "coat_length": 6.5,
        "body_type": "small",
        "pattern": "pattern1"
        })
```
