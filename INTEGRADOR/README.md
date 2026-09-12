# projeto_integrador
# 2. Instalação do ambiente Virtual - WINDOWS

1. ```python --version```
2. ```python -m venv .venv```
3. ```.venv\Scripts\Activate.ps1```
4. ```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser```
    1. O comando acima deve ser utilizado quando PowerShell bloquear o script
5. ```python -m venv .venv```

python -m pip install flask   
pip install mysql-connector-python
---

LINUX:
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install flask

## 2. 1. Verificações sobre a instalação do python 

1. ```python --version```
2. ```where.exe python```
    1. SAÍDA DO COMANDO{.venv\Scripts\python.exe}
3. ```python -m pip install --upgrade pip```


---


## 3. Gerenciamento de Dependências (instala tudo de dependencia do projeto)

1. ```pip install -r requirements.txt```
 
## 3. 1. Salvar novas dependências ("Tira uma foto" do sistema)

1. ```pip freeze > requirements.txt```


---


## 4. COMANDOS FUTUROS

> Se quiser que outros dispositivos da sua rede possam acessar a API

```flask --app main run --host=0.0.0.0 --port=5000```


---


## 5. COMANDOS PARA ACESSAR ARQUIVOS

> img src="{{ url_for('static', filename='img/logo.png') }}"
>  
> link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">;
>
> script src="{{ url_for('static', filename='js/script.js') }}"
>
> As fontes são englobadas aqui!
