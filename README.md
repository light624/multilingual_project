# Multilingual_site

## Prérequis

- Python 3.12.3
- pip (gestionnaire de paquets Python)
- Git

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/votre-utilisateur/votre-projet.git
   cd votre-projet



## Exécution

2. Executer et modifier les différents fichiers de compilation

     ```bash
     cd votre-application
     django-admin makemessages -l fr
     django-admin makemessages -l en
     django-admin makemessages -l es
     django-admin compilemessages


3. Executez l'application

    ```bash
    cd ../
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver nom_du_port

