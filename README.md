# Desafio_2_Django_API

<i>Desafio Tech 2 (Automação)</i>  |  [BD - Arquivo XLSX - para verificação](https://github.com/renatamoon/Desafio_2_Django_API/blob/workpc/app_usuario_202111271205.xls)<br>

<hr>
<p align="center">
  <a href="#desafio">Sobre o desafio</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#tecnologias">Tecnologias utilizadas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#instalacao">Como Executar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;  
  <a href="#imagens">Algumas Imagens</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
  <a href="#links_apps">Links Úteis</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>
<hr>

## <a id="projeto"> 💻 SOBRE O DESAFIO </a><br>

- Cadastrar usuário, fornecendo o login, senha e data de nascimento
- Baixar todos os usuários cadastrados em XLSX.
- Enviar no formato .zip

> 🟩 Status do projeto: FINALIZADO <br>
<hr>
  
  ## <a id="tecnologias"> 🧪 TECNOLOGIAS UTILIZADAS </a>

-Desenvolvimento do Front-End:

![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

-Desenvolvimento do Back-End:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)

-Desenvolvimento em:

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

<hr>

## <a id="instalacao"> 🔴 PASSO A PASSO DE COMO EXECUTAR A APLICAÇÃO </a> 

*No Windows:

<b>-Clone o repositório com o camando:</b> `https://github.com/renatamoon/Desafio_1_Cadastro_Django.git` <br>
<b>-Criando virtual environment:</b> `python -m venv venv`<br>
<b>-Ativando o virtual environment: </b>`. venv\Scripts\Activate.ps1`<br>
<b>Obs: Caso ocorra um erro na ativação:</b> entre no powershell e digite o seguinte comando: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`<br>
<b>-Execução do arquivo requirements: </b>`pip install -r requirements.txt`<br>

*No Linux:

<b>-Baixe o repositorio<br>
<b>-Criando virtual environment:</b> `virtualenv venv`<br>
<b>-Ativando o virtual environment:</b> `. venv/bin/activate`<br>
<b>-Execução do arquivo requirements e instalar dependencias:</b> `pip install -r requirements.txt`<br>
  
 <hr> 
  
*Alterar as configurações do DataBase no arquivo <b>`settings.py`</b> <br>

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'host_bd',
        'PORT': 'porta_bd',
        'NAME': 'desafio_2',
        'USER': 'usuario_bd',
        'PASSWORD': 'senha_bd'    
    }
}
```

-Migre o banco de dados com: `python manage.py migrate` <br>
-Execute o servidor: `python manage.py runserver` <br>
  
<hr>

## <a id="imagens"> 🔴 IMAGENS FINAIS: </a> 

Visual da Página Inicial<br>
<br>
<br>
-Formulário de cadastro de usuários:
<br>
<br>
![image](https://user-images.githubusercontent.com/87100340/143606786-0bec63c6-f9f9-4137-aec1-145157f89521.png)
<br>
<br>
-Ao cadastrar o usuário já inclui na lista de usuários dentro na própria página inicial:
<br>
<br>
![image](https://user-images.githubusercontent.com/87100340/143606970-b4fc97de-180b-4b0c-a6d3-4b6c5a15f2f3.png)
<br>
<br>
-No card com o Nome e Login, há um botão de acesso para a página do Perfil de Usuário:
<br>
<br>
![image](https://user-images.githubusercontent.com/87100340/143607002-ff445406-1fe7-4185-bb1c-364af997e433.png)
<br>
<br>
-Há um botão para voltar à página de cadastro:
<br>
<br>
![image](https://user-images.githubusercontent.com/87100340/143607041-4cc4b055-471a-41e5-bb9c-331bb25f8714.png)
<br>

<hr>
  
## <a id="links_apps"> 🔴 LINKS ÚTEIS </a> 

*USANDO MYSQL WORKBENCH PARA EXPORTAÇÃO DOS DADOS EM XML:
<br>
<br>
https://help.umbler.com/hc/pt-br/articles/202385865-MySQL-Importando-Exportando-um-banco-de-dados - documentação para exportação de dados do MYSQL<br>

