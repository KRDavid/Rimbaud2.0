<!-- PROJECT LOGO -->

# Rimbaud2.0

"C'ETAIT PAS MA GUERRE"

![John Rimbaud](./templates/gif_rambo.gif)

## Contexte du projet  
Vous devez proposer un mini site de construction d'un article afin de faciliter la rédaction des articles d'un écrivain.  

Vous devez lui proposer une interface d'administration CRUD (voir le lien dans les ressources) avec authentification  

Les champs nécessaires pour la rédaction d'un article seront :  

* Titre  
* Description  
* Article (texte seulement)  
* Date limite de parution  
* Article visible par l'administrateur uniquement (boolean)  
* Vous lui proposerez également une page HTML permettant de visualiser tous les articles avec la possibilité de voir l'article sélectionné dans une nouvelle page.  
* L'accès à cet article sera de cette forme domain.tld/article?id=34  

Sur la page des articles insérez un champs de recherche dans lequel l'utilisateur saisira l'ID de l'article (et non du texte)  

Seul les articles ayant une date de validitée supérieure à la date du jour doivent être visible  

Dans le cas où vous affichez une ressource protégée (article visible que par l'admin) faites le nécessaire pour restreindre l'accès (si pas connecté faire une redirection).

<!-- TABLE OF CONTENTS -->

## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Usage](#usage)
* [Sources](#sources)

<!-- ABOUT THE PROJECT -->
## About The Project

## Built With

* [Anaconda](https://www.anaconda.com/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo

    ```sh
    git clone https://github.com/KRDavid/Rimbaud2.0
    ```

2. Create a conda virtual environment with

    ```sh
    conda create --name <env> --file requirements.txt
    ```
    
 3. Perform migrations
 
    ```sh
    python manage.py make migration
    python manage.py migrate
    python manage.py runserver
    ```  
    
  
 4. Usage examples   


* http://localhost:8000/article/homepage page d'acceuil

* http://localhost:8000/article/check voir articles

* http://localhost:8000/article/add ajouter un article 

## Sources

* https://www.youtube.com/watch?v=SjRlmyEVXq4
* https://www.youtube.com/watch?v=ZkE1A2w0MAc
