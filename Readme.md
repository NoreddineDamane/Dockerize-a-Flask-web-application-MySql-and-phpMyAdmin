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
3.	Créer un répertoire de travail dans lequel requirements.txt et app.py seront copiés, nous avons besoin que nos dépendances (Flask et mysql-connector) soient installées.
4. 4.	Installer les librairies nécessaires et lancer l'application.
![](https://github.com/NoreddineDamane/Dockerize-a-Flask-web-application-MySql-and-phpMyAdmin/blob/main/impecr/4.png)
Nous pourrons créer l’images docker pour notre application en exécutant le docerkfile. Cependant nous ne pourrons pas l’utiliser car elle dépend de MySQL. Pour cela Nous utiliserons docker-compose pour faciliter l’orchestration des conteneurs indépendants en une seule application de travail.

## Création du docker-compose.yml
Nous utilisons trois services, 
*	Un conteneur qui expose l’API REST (app), 
*	Un conteneur qui contient la base de données (db)
*	Un conteneur phpMyAdmin pour gérer les serveurs de bases de données MySQL.
                                ![](https://github.com/NoreddineDamane/Dockerize-a-Flask-web-application-MySql-and-phpMyAdmin/blob/main/impecr/5.png)
             
             
Nous utilisons trois services, l’un est un conteneur qui expose l’API REST (app), et l’autre contient la base de données (db).
1.	Service app :
build : spécifie le répertoire qui contient le Dockerfile contenant les instructions de création de ce service
links : relie ce service à un autre conteneur. Cela nous permettra également d’utiliser le nom du service au lieu d’avoir à trouver l’adresse IP du conteneur de base de données.
ports : mappage des ports <Host>:<Container>.
2.	Service db :
image: Comme l’instruction FROM du Dockerfile. Au lieu d’écrire un nouveau Dockerfile, nous utilisons une image existante.
environnement : ajoutez des variables d’environnement.
ports: Comme j’ai déjà une instance mysql en cours d’exécution sur mon hôte à l’aide de ce port, je la mappe à une autre. Le mappage se fait uniquement d’un hôte à l’autre, de sorte que notre conteneur App Service utilisera toujours le port 3306 pour se connecter à la base de données.
volumes: puisque nous voulons que le conteneur soit initialisé avec notre schéma, pour cela nous connectons le répertoire contenant notre script .sql au point d'entrée de ce conteneur.
3.	Service phpmyadmin
depends_on : exprime une dépendance aux services. l'image docker est utilisée pour le container PHPMyAdmin. 
environnement : ajoutez des variables d’environnement (mappé  ports et la variable d'environnement est spécifiée db pour connecter le conteneur).
 
 
## Exécution du docker-compose
Afin d’exécuter notre application dockerisée, nous exécuterons la commande suivante à partir du terminal: docker-compose up
![](https://github.com/NoreddineDamane/Dockerize-a-Flask-web-application-MySql-and-phpMyAdmin/blob/main/impecr/6.png)
### Exécution de l’application web
Nous pouvons vérifier que l’application web fonctionne en  tapant URL suivant dans un navigateur : 127.0.0.1:5000 et en recevant la réponse suivante:
![](https://github.com/NoreddineDamane/Dockerize-a-Flask-web-application-MySql-and-phpMyAdmin/blob/main/impecr/7.png)
### Démarrage du serveur MySQL et des services phpMyAdmin
Pour accéder à phpMyAdmin en tapant URL suivant dans un navigateur : http://localhost:8080, « n suite doit être chargé dans votre navigateur Web.
                    ![](https://github.com/NoreddineDamane/Dockerize-a-Flask-web-application-MySql-and-phpMyAdmin/blob/main/impecr/8.png)
 

