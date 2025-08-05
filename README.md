# fastapi

## Configuração
Para rodar o projeto localmente compie o arquivo .env.example para .env e configure as variáveis de ambiente.
```bash
cp .env.example .env
```
crie um virtualenv e ative-o:
```bash
python -m venv .venv
source .venv/bin/activate
```
e instale as dependências com o comando:
```bash
pip install -r requirements.txt
```

#### configuração do banco de dados
se o banco de dados não estiver configurado, inicie o container com o comando:
```bash
docker-compose up -d
```

rode as migrations com o comando:
```bash
alembic upgrade head
```

Inicie o projeto com o comando, por padrão ele irá iniciar na porta 8000:
```bash
uvicorn app.main:app --reload --port 8000
```

A documentação do projeto irá iniciar na porta 8000:

[http://localhost:8000/docs](http://localhost:8000/docs)

