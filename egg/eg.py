import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.metrics import MeanAbsoluteError

# -----------------------------
# 1. Fonction Eg(x,y)
# -----------------------------
def Eg(x, y):
    return 1.35 + 0.668*x - 1.068*y + 0.758*x**2 + 0.078*y**2 - 0.069*x*y - 0.322*x**2*y + 0.03*x*y**2

# -----------------------------
# 2. Génération du jeu de données
# -----------------------------
N = 5000
x = np.random.uniform(0, 1, N)
y = np.random.uniform(0, 1, N)
Eg_values = Eg(x, y)

X = np.column_stack((x, y))
Y = Eg_values.reshape(-1, 1)

# -----------------------------
# 3. Définition du modèle
# -----------------------------
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(2,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
])

# -----------------------------
# 4. Compilation et entraînement
# -----------------------------
model.compile(optimizer='adam', loss='mse', metrics=[MeanAbsoluteError()])
history = model.fit(X, Y, epochs=100, batch_size=32, verbose=1, validation_split=0.2)

# -----------------------------
# 5. Évaluation
# -----------------------------
loss, mae = model.evaluate(X, Y, verbose=0)
print(f"\nErreur absolue moyenne (MAE) : {mae:.4f}")

# -----------------------------
# 6. Sauvegarde du modèle
# -----------------------------
model.save("model_Eg.h5")
print("✅ Modèle sauvegardé dans model_Eg.h5")
