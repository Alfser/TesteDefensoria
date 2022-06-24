


::Esse script instalará as dependências do python e executará o site Django.


:: Apenas mudando a cor do cmd
COLOR A

:: Desativando a echo dos comandos.
ECHO OFF

ECHO Configurando o ambiente python para rodar o Django.


ECHO *******************************************************

ECHO - Antes de rodar o script crie um banco de dados no POSTGRES com o nome 'db.people'
ECHO - se colocar outro nome irá ter que alterar em settings.py 
ECHO - e coloque a senha do banco de dados em ./core/settings.py na linha 85
ECHO - No desenvolvimento foi usado a versão 3.9 do PYTHON.
ECHO - Isso poderá influênciar na criação do ambiente virtual.

ECHO *******************************************************

ECHO A sua versão instalada do Python é:
:: Checando a versão do python instalada.
python --version

:: Dando uma pause para a leitura. Apos apertar uma tecla irá seguir adiante.
PAUSE

::Ativando o echo novamente.
ECHO ON

:: Criando um ambiente virtual para rodar o script python
python -m venv venv


:: Instalando as dependências.
.\venv\Scripts\pip.exe install -r requirements.txt

:: Realizando a criação do banco de dados pelo modelo.
.\venv\Scripts\python.exe manage.py migrate

:: Executando o browser padrão
start http://localhost:8000

ECHO OFF
ECHO *******************************************************
ECHO INSTALAÇÂO FINALIZADA
ECHO *******************************************************

:: executando o programa python.
.\venv\Scripts\python.exe .\manage.py runserver
