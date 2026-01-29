# MongoDB ![docs/leaf.svg](https://github.com/mongodb/mongo/blob/master/docs/leaf.svg)

O MongoDB é um sistema de gerenciamento de banco de dados (SGBD) não relacional de código aberto
que usa documentos flexíveis em vez de tabelas e linhas para processar e armazenar várias formas 
de dados.

Como banco de dados NoSQL, oferece um modelo de armazenamento de dados elástico que permite 
aos usuários armazenar e consultar tipos de dados multivariados com facilidade. Isso simplifica o 
gerenciamento de banco de dados para desenvolvedores e cria um ambiente altamente escalável para 
aplicações e serviços multiplataforma.

Documentos do MongoDB ou coleções de documentos são as unidades básicas de dados. Formatados como 
Binary JSON (JavaScript Object Notation), esses documentos podem armazenar vários tipos de dados 
e ser distribuídos em múltiplos sistemas. Como o MongoDB adota um design de esquema dinâmico, os 
usuários têm flexibilidade incomparável ao criar registros, consultar coleções e analisar grande 
volume de informações.
<a href="https://www.mongodb.com/">https://www.mongodb.com/</a>

# PyMongo 
PyMongo é uma distribuição Python que contém ferramentas para trabalhar com o MongoDB, sendo a
maneira recomendada de trabalhar com o MongoDB a partir do Python. <a href="https://www.mongodb.com/pt-br/docs/languages/python/pymongo-driver/current/">https://www.mongodb.com/pt-br/docs/languages/python/pymongo-driver/current/</a>
<br><br>
## Como executar o aplicativo:

- Clonar repositorio

```
git clone https://github.com/mayconct32/PyMongoDB.git
```
<br>
- Subir container com imagem MongoDB
 
```
docker run -d --name mongo_lhama 
-p 27017:27017 
-e MONGO_INITDB_ROOT_USERNAME=admin 
-e MONGO_INITDB_ROOT_PASSWORD=password 
mongo:4.2
```
<br>
- criar .env na raiz do projeto:

```
touch .env 
```
<br>
- adicionar as variáveis ​​de ambiente no arquivo .env:

```
HOST = "127.0.0.1",
PORT = "27017",
USERNAME = "admin",
PASSWORD = "password",
DB_NAME = "db_name"
```
<br>
- instalar poetry:

```
pip install pipx
pipx install poetry
```
<br>
- ativar ambiente virtual:
  
```
poetry env activate
```
<br>
- instalar dependências(pacotes) do projeto a partit do pyproject.toml:

```
poetry install 
```
<br>
- Por fim, execute o projeto:

```
python3 mongo.py
```





