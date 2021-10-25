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
