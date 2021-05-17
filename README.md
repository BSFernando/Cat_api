# API_cat CRUD

A API esta disponibilizidade no endereço "https://api-cat.herokuapp.com/"

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

