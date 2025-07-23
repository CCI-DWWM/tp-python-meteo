# tp-pyhton-meteo

## Description

Ce projet est une application web développée avec FastAPI et Jinja2 permettant de saisir un code postal et d'afficher la commune correspondante ainsi que les informations météo actuelles pour cette localisation.

L'application utilise un formulaire pour récupérer le code postal, puis interroge un modèle local (ou une base de données) pour récupérer la commune et les coordonnées géographiques, avant d'afficher la météo grâce à une API météo.

## installation
Création de l'environnement virtuel
```bash
py -m venv .venv
```
Activation de l'environnement virtuel
```bash
.venv\Scripts\Activate.ps1
 ```

Installation des librairies
```bash
pip install -r requirements.txt
```

## Execution du serveur
```bash
fastapi dev main.py
```
