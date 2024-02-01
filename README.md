# soat-order-status

**Criando Ambiente Virtual**
```
$python3 -m venv .env
$python3 -m venv .venv
```

**Ativando Ambiente Virtual**
```
$source .venv/bin/activate
export PYTHONPATH=$PWD/app

# deprecated
$. .env/bin/activate
```

**Desativando Ambiente Virtual**
```
$deactivate
```

***RUN SOAT-ORDER-FOOD***
```
.venv/bin/python app/main.py 
```

**TESTS**
```
# padrao relatorio tela coverage
pytest --cov=app/src/core/usecase/ app/tests/

# gera relatorio
pytest --junitxml=tests/test-results.xml --cov=./app/tests/ --cov-report=xml --cov-report=html

# simples
pytest -cov=codigo app/tests/


```

**Dependencias Instalando**
- **fastapi** lib de framework REST
- **gunvicorn e uvicorn** lib de webservers 
- **sql** lib de mapeamento de dominio
- **sqlalchemy** lib ORM para mapeamento e filtro SQL
- **mysql-connector-python** lib de conexão para MySQL
- **asyncmy** lib ORM para conexao async para MySQL
- **greenlet** lib dependencia do asyncmy para MySQL

```
$pip install fastapi gunicorn uvicorn
$pip install sql
$pip install sqlalchemy
#$pip install mysql-connector-python
$pip install asyncmy
pip install jwt
$pip freeze > requirements.txt
$pip install -r requirements.txt
```

**comandos**
- **remover __pycache__**: find . -type d -name __pycache__ -exec rm -r {} \+
- **desabilitar __pycache__**: export PYTHONDONTWRITEBYTECODE=1
- **desinstalar todas libs**: pip freeze | xargs pip uninstall -y
