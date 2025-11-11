from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from flask_cors import CORS

# -----------------------------
# 1. Initialisation du serveur
# -----------------------------
app = Flask(__name__)
CORS(app)  # Autorise React à faire des requêtes

# -----------------------------
# 2. Charger le modèle (compile=False)
# -----------------------------
model = load_model("model_Eg.h5", compile=False)

# -----------------------------
# 3. Fonction Eg théorique (optionnelle)
# -----------------------------
def Eg_theorique(x, y):
    return 1.35 + 0.668*x - 1.068*y + 0.758*x**2 + 0.078*y**2 - 0.069*x*y - 0.322*x**2*y + 0.03*x*y**2

# -----------------------------
# 4. Route de prédiction
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    x = float(data["x"])
    y = float(data["y"])

    Eg_pred = model.predict(np.array([[x, y]]))[0][0]
    Eg_true = Eg_theorique(x, y)

    return jsonify({
        "Eg_pred": round(float(Eg_pred), 4),
        "Eg_true": round(float(Eg_true), 4)
    })

# -----------------------------
# 5. Lancement du serveur
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
