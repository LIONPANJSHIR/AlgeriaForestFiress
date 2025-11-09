
# 🔥 Algérie Fire Severity Predictor (AFSP)

## Application de Prédiction de la Gravité des Feux de Forêt par Régression Ridge Optimisée

-----

## 📋 Table des Matières

1.  [Aperçu du Projet](https://www.google.com/search?q=%231-aper%C3%A7u-du-projet)
2.  [Fonctionnalités Clés](https://www.google.com/search?q=%232-fonctionnalit%C3%A9s-cl%C3%A9s)
3.  [Structure du Projet](https://www.google.com/search?q=%233-structure-du-projet)
4.  [Installation et Démarrage](https://www.google.com/search?q=%234-installation-et-d%C3%A9marrage)
5.  [Modèle et Caractéristiques (Input Data)](https://www.google.com/search?q=%235-mod%C3%A8le-et-caract%C3%A9ristiques-input-data)
6.  [Dépendances](https://www.google.com/search?q=%236-d%C3%A9pendances)

-----

## 1\. Aperçu du Projet

Ce projet implémente un service web léger utilisant **Flask** pour prédire un indice de gravité des feux de forêt (basé sur le système FWI Canadien) en Algérie.

La prédiction est effectuée par un modèle de **Régression Ridge** encapsulé dans un pipeline Scikit-learn. Ce pipeline applique automatiquement la mise à l'échelle des données d'entrée (`StandardScaler`) avant d'effectuer la prédiction. Les hyperparamètres du modèle ont été optimisés à l'aide de la librairie **Optuna** pour minimiser l'erreur quadratique moyenne (RMSE).

## 2\. Fonctionnalités Clés

  * **Interface Web Interactive** : Formulaire HTML simple pour la saisie des 11 caractéristiques.
  * **Pipeline Robuste** : Utilisation d'un `Pipeline` Scikit-learn pour garantir l'application cohérente de la mise à l'échelle et du modèle.
  * **Modèle Optimisé** : Intégration d'un modèle dont les hyperparamètres (`alpha`, `fit_intercept`, `solver`) ont été réglés par Optuna.
  * **Déploiement Facile** : Architecture Flask simple et efficace.

## 3\. Structure du Projet

Le projet est organisé comme suit :

```
/votre_projet
├── app.py                  # Script principal de l'application Flask
├── README.md               # Ce fichier
├── model/
│   └── model.pkl           # Pipeline Scikit-learn sérialisé (StandardScaler + Ridge)
└── templates/
    └── index.html          # Template HTML pour le formulaire de saisie
```

## 4\. Installation et Démarrage

### Prérequis

Assurez-vous d'avoir Python (3.x recommandé) installé.

### Installation des Dépendances

Installez toutes les bibliothèques requises en utilisant `pip` :

```bash
pip install Flask numpy pandas scikit-learn
```

### Démarrage de l'Application

1.  Assurez-vous que votre fichier `model.pkl` se trouve bien dans le dossier `model/`.
2.  Exécutez le script principal :

<!-- end list -->

```bash
python app.py
```

L'application démarrera généralement à l'adresse `http://0.0.0.0:5000/`.

## 5\. Modèle et Caractéristiques (Input Data)

Le modèle s'attend à recevoir 11 caractéristiques numériques dans un ordre strict. Il est **impératif** que l'ordre des valeurs fournies par le formulaire corresponde à l'ordre d'entraînement de votre `X_train` :

| \# | Nom du Champ (Formulaire) | Nom de Colonne (Modèle Interne) | Description |
| :-: | :---: | :---: | :--- |
| 1 | `Temperature` | `Temperature` | Température en °C |
| 2 | `RH` | `Rh` | Humidité Relative en % |
| 3 | `Ws` | `Ws` | Vitesse du Vent en km/h |
| 4 | `Rain` | `Rain` | Pluie en mm |
| 5 | `FFMC` | `Ffmc` | Fine Fuel Moisture Code |
| 6 | `DMC` | `Dmc` | Duff Moisture Code |
| 7 | `DC` | `Dc` | Drought Code |
| 8 | `ISI` | `Isi` | Initial Spread Index |
| 9 | `BUI` | `Bui` | Build-up Index |
| 10 | `Classes` | `Classes` | Indicateur de classe de feu (0/1) |
| 11 | `Region` | `Region` | Indicateur de région (0/1) |

> **Note importante sur la casse :** Le code `app.py` a été ajusté pour lire les noms en majuscules du formulaire (`RH`, `FFMC`) et les organiser dans l'ordre attendu par le modèle interne (`Rh`, `Ffmc`, etc.). **Ne modifiez pas la casse des noms de champs dans `index.html`.**

## 6\. Dépendances

Ce projet nécessite les bibliothèques Python suivantes :

  * `Flask`
  * `numpy`
  * `pandas`
  * `scikit-learn`
  * `pickle` (intégré à Python)