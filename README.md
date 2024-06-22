
# Password Generator Application

Cette application est un générateur de mots de passe web simple développé en Python utilisant Flask.

## Prérequis

- Python 3.7 ou supérieur
- Pip (le gestionnaire de paquets Python)

## Installation

1. Clonez le dépôt ou téléchargez les fichiers source.

2. Naviguez vers le répertoire du projet :


    ```sh
    cd chemin/vers/passwordgen.py
    ```

3. Créez un environnement virtuel et activez-le :


    ```sh
    python -m venv venv
    # Pour Windows
    venv\Scripts\activate
    # Pour macOS/Linux
    source venv/bin/activate
    ```

4. Installez les dépendances nécessaires :
    ```sh
    pip install Flask
    ```

## Exécution de l'application

1. Assurez-vous que l'environnement virtuel est activé.

2. Exécutez l'application Flask :


    ```sh
    python app.py
    ```

3. Ouvrez votre navigateur et allez à l'adresse :


    ```
    http://127.0.0.1:5000
    ```

## Structure du projet

- `app.py`: Le fichier principal de l'application.
- `static/`: Contient les fichiers statiques (CSS, JavaScript, images).
- `templates/`: Contient les fichiers de modèles HTML.

## Fonctionnalités

- Génération de mots de passe sécurisés.
- Interface web simple et intuitive.
