from flask import Flask, request, jsonify ,render_template
import numpy as np , pandas as pd
import pickle

# --- Configuration et Chargement du Pipeline ---

application = Flask(__name__)
app = application

# Chemin du Pipeline optimisé (contient le scaler et le modèle)
PIPELINE_PATH = "model/model.pkl" 

try:
    # Charger le Pipeline complet
    pipeline_model = pickle.load(open(PIPELINE_PATH, "rb"))
    print("Pipeline de modélisation chargé avec succès.")
except FileNotFoundError:
    print(f"Erreur: Le fichier du pipeline {PIPELINE_PATH} est introuvable.")
    pipeline_model = None
except Exception as e:
    print(f"Erreur lors du chargement du pipeline: {e}")
    pipeline_model = None


# --- Définition des Routes ---

@app.route('/')
def index():
    """Charge le formulaire de saisie des données."""
    return render_template('index.html')

@app.route('/predictdata', methods=['POST'])
def predict_data():
    """Reçoit les données du formulaire, les traite via le Pipeline, et retourne la prédiction."""
    if pipeline_model is None:
        return render_template('index.html', prediction_text="Erreur: Pipeline de modélisation non chargé.")

    try:
        # 1. Récupération des 11 caractéristiques
        # Les noms ici doivent correspondre aux attributs 'name' du HTML (ex: 'RH', 'FFMC')
        
        Temp_val = float(request.form.get('Temperature'))
        RH_val = float(request.form.get('RH'))  # Récupère 'RH' du HTML
        Ws_val = float(request.form.get('Ws')) 
        Rain_val = float(request.form.get('Rain'))
        FFMC_val = float(request.form.get('FFMC')) # Récupère 'FFMC' du HTML
        DMC_val = float(request.form.get('DMC')) 
        DC_val = float(request.form.get('DC')) 
        ISI_val = float(request.form.get('ISI')) 
        BUI_val = float(request.form.get('BUI')) 
        Classes_val = float(request.form.get('Classes')) 
        Region_val = float(request.form.get('Region'))

        # 2. Création du tableau NumPy
        # CET ORDRE DOIT CORRESPONDRE STRICTEMENT À L'ORDRE DES COLONNES X_train :
        # ['Temperature', 'Rh', 'Ws', 'Rain', 'Ffmc', 'Dmc', 'Dc', 'Isi', 'Bui', 'Classes', 'Region']
        
        new_data = np.array([
            [Temp_val, RH_val, Ws_val, Rain_val, FFMC_val, DMC_val, DC_val, ISI_val, BUI_val, Classes_val, Region_val]
        ])

        # 3. Prédiction via le Pipeline
        result = pipeline_model.predict(new_data)

        # 4. Formatage de la sortie
        prediction_output = f"L'indice de gravité (FWI ou autre) prédit est: {result[0]:.2f}"
        
        return render_template('index.html', prediction_text=prediction_output)

    except ValueError:
        return render_template('index.html', prediction_text="Erreur de saisie : Veuillez vérifier que toutes les valeurs sont numériques et correctement formatées.")
    except Exception as e:
        # Ceci peut capturer des erreurs si le nombre de features ne correspond pas au pipeline
        return render_template('index.html', prediction_text=f"Une erreur interne s'est produite lors de la prédiction: {e}")


# --- Point d'Entrée ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)