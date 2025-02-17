# CRUD API com Django

Este projeto implementa uma API RESTful para operações CRUD (Create, Read, Update, Delete) utilizando Django e Django REST Framework. Ele serve como base para aplicações que necessitam de gerenciamento de dados via API.

## Tecnologias Utilizadas

- **Django** (Framework Web em Python)
- **Django REST Framework** (DRF - Para criação de APIs RESTful)
- **django-cors-headers** (Para permitir requisições de diferentes origens - CORS)

## Instalação e Execução

### Pré-requisitos

Certifique-se de ter o **Python** instalado em sua máquina. Recomendamos o uso de um ambiente virtual (venv) para gerenciar dependências.

### Passos para instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seuusuario/crud-api-django.git
   cd crud-api-django
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. Instale as dependências do projeto:
   ```sh
   pip install -r requirements.txt
   ```

4. Execute as migrações do banco de dados:
   ```sh
   python manage.py migrate
   ```

5. Inicie o servidor local:
   ```sh
   python manage.py runserver
   ```

A API estará disponível em `http://127.0.0.1:8000/`.

## Endpoints Principais

| Método  | Endpoint  | Descrição |
|---------|----------|-----------|
| `GET`   | `/api/`  | Lista todos os registros |
| `POST`  | `/api/data/`  | Cria um novo registro |
| `GET`   | `/api/data/?user={user_nickname}/` | Obtém um registro específico |
| `PUT`   | `/api/data/?user={user_nickname}/` | Atualiza um registro específico |
| `DELETE` | `/api/data/?user={user_nickname}/` | Exclui um registro específico |

## Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.
