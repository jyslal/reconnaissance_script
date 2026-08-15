# Reconnaissance.py

Petit outil de reconnaissance réseau écrit en Python.

Il permet de vérifier si une machine est joignable, puis de lancer un scan de ports TCP (SYN scan) si elle répond.

## Fonctionnalités

- Vérification des droits root au démarrage
- Demande d'une adresse IP cible
- Validation basique de l'adresse IP
- Test de joignabilité avec `ping`
- Scan de ports avec `nmap -sS` (si la machine est joignable)
- Affichage des ports TCP ouverts

## Prérequis

- Avoir linux
- Python 3
- `nmap` installé sur la machine
- Droits root (le script doit être lancé avec `sudo`)

### Installation de nmap (si besoin)

```bash
sudo apt update
sudo apt install nmap
