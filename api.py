from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model

# Sauvegarder le modèle
# model.save("modele")
type_of_disease = ["Bengin cases", "Malignant cases", "Normal cases"]
# Charger l'image à classifier
pathfilee = pathfilee = (
    "C:/Users/MohammedElouafi/Desktop/WhatsApp Image 2024-02-21 à 00.49.22_eea6542e.jpg"
)

img_path = pathfilee
img = image.load_img(img_path, target_size=(150, 150))

# Convertir l'image en tableau numpy
img_array = image.img_to_array(img)

# Élargir les dimensions de l'image (ajouter la dimension du batch)
img_array = np.expand_dims(img_array, axis=0)

# Normaliser les valeurs des pixels de l'image
img_array /= 255.0
# Charger le modèle sauvegardé
loaded_model = load_model("modele")

# Utiliser le modèle chargé pour prédire la classe d'une nouvelle image
predictions = loaded_model.predict(img_array)

# Obtenir l'indice de la classe prédite
predicted_class_index = np.argmax(predictions)

# Obtenir le nom de la classe prédite à partir de l'indice
predicted_class = type_of_disease[predicted_class_index]

print("La classe prédite pour cette image est :", predicted_class)
