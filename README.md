![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![TailwindCss](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)

![](https://img.shields.io/badge/Epitech_Benin-blue)

  
## Project Infos
### Time : 4 Days (14/08/2024 - 15/08/2024)
 ____________________________


# Get Started with OAuth2 in Django

OAuth is an open standard for access delegation, commonly used as a way for Internet users to grant websites or applications access to their information on other websites but without giving them the passwords.  
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. 
``` bash
   
```

## Install Django with python3

``` bash
    # make sure you've already install python3 and pip before this
   python3 -m pip install Django
```
``` bash
   # check if django is successfully installed
    django-admin --version
```

## Create and activate a python virtual environnement

``` bash
    # install venv
      sudo apt install python3.10-venv
    #create your virtual environnement
      python3 -m venv <venv_name>
    # activate your virtual environnement
      source <venv_name>/bin/activate
    #in the case you want to deativate it just write the command "deactivate" in your terminal
    #but you should know that your venv should always be activate if you want to perform any actions
```

## Create a new django project

``` bash
    django-admin startproject my_project
    cd my_project
    python3 manage.py runserver
```
## Create a new app

``` bash
    python3 manage.py startapp my_app #create an app
```
For any installation, don't forget to add them in the "INSTALLED APPS" part in your settings.py file located in your project directory.

## Create initial migration for your app

``` bash
    python3 manage.py makemigrations
    python3 manage.py migrate
```

## Use Django admin login to make things easier

``` bash
    #create a superuser
      python3 manage.py createsuperuser  
    #install allauth library 
      pip install django-allauth
```

### If you want to go futher by adding styles to your django views...
Follow the link [https://dev.to/vincod/django-tailwind-css-3b5i]

# Project actions

* Clone the repository
* Move to the project Directory
``` bash
    cd Back-end/my_app
```
* Run the server
``` bash
    # activate the virtual environnement
      source oauth_venv/bin/activate
    # run server
      python3 -m venv oauth_venv
```
* Load styles
``` bash
    # move to resources directory
      cd resources
    # load styles
      npm run build
```
#### Epitech Benin
