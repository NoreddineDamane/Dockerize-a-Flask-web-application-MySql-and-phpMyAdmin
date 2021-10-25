# Dockeriser une application web Flask + MySql et phpMyAdmin
## Introduction

Le but est de coordonner trois conteneurs pour la création d’applications Web basées sur Flask et MySQL.
Pour notre application, nous aurons besoin de trois conteneurs :

  * Un conteneur pour exécuter l'application elle-même.
  * Un conteneur Mysql pour exécuter la base de données.
  * Un conteneur phpMyAdmin pour gérer les serveurs de bases de données MySQL.
Pour cela Nous utiliserons docker-compose pour faciliter l’orchestration des conteneurs
![](https://github.com/NoreddineDamane/Dockerize-a-Flask-web-application-MySql-and-phpMyAdmin/blob/main/impecr/1.png)

## Création d’une image Docker pour notre application
le repertoire
![](https://github.com/NoreddineDamane/Dockerize-a-Flask-web-application-MySql-and-phpMyAdmin/blob/main/impecr/2.png)
* app.py — contient l’application Flask qui se connecte à la base de données et expose un point de terminaison d’API REST
* database.sql — un script SQL pour initialiser la base de données

### Dockerfile
Nous voulons créer une image Docker pour notre application, nous devons donc créer un Dockerfile dans le répertoire app.
Etape de la création du dockerfile :
1.	Image Python 3 comme base 
2.	Exposer le port 5000 (pour Flask)
3.	Créer un répertoire de travail dans lequel requirements.txt et app.py seront copiés, nous avons besoin que nos dépendances (Flask et mysql-connector) soient installées et livrées avec l'image, donc nous devons créer le fichier requirements.txt mentionné ci-dessus :
