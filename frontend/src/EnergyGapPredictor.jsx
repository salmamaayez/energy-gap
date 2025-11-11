import React, { useState } from "react";
import axios from "axios";

export default function EnergyGapPredictor() {
  const [x, setX] = useState("");
  const [y, setY] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    if (x === "" || y === "") return alert("Veuillez entrer x et y !");
    setLoading(true);
    setResult(null);

    try {
      const res = await axios.post("http://127.0.0.1:5000/predict", { x, y });
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Erreur lors de la prédiction !");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <div className="bg-white p-8 rounded-2xl shadow-lg w-96">
        <h1 className="text-2xl font-bold mb-6 text-center text-blue-700">
          Prédiction du gap d’énergie Eg(x,y)
        </h1>

        <label className="block mb-2 font-semibold">x :</label>
        <input
          type="number"
          value={x}
          onChange={(e) => setX(e.target.value)}
          className="border rounded-lg p-2 w-full mb-4"
        />

        <label className="block mb-2 font-semibold">y :</label>
        <input
          type="number"
          value={y}
          onChange={(e) => setY(e.target.value)}
          className="border rounded-lg p-2 w-full mb-6"
        />

        <button
          onClick={handlePredict}
          disabled={loading}
          className="bg-blue-600 text-white w-full rounded-lg py-2 font-semibold hover:bg-blue-700 disabled:opacity-50"
        >
          {loading ? "Calcul en cours..." : "Prédire Eg(x,y)"}
        </button>

        {result && (
          <div className="mt-6 text-center">
            <p className="text-lg font-semibold text-green-700">
              Eg_prédit = {result.Eg_pred}
            </p>
            <p className="text-sm text-gray-600">
              (Eg_théorique = {result.Eg_true})
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
