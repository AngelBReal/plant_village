from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import base64
import io
from PIL import Image

app = Flask(__name__)

# Cargar modelo TFLite para plant leaves
interpreter = tf.lite.Interpreter(model_path="models\h5\plant_leaves_classifier_expert.tflite")
interpreter.allocate_tensors()

# Obtener info de entrada/salida
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Define your class names (copy this list from your training script!)
raw_class_names = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Blueberry___healthy', 'Cherry___healthy', 'Cherry___Powdery_mildew',
    'Corn___Cercospora_leaf_spot Gray_leaf_spot', 'Corn___Common_rust', 'Corn___healthy',
    'Corn___Northern_Leaf_Blight', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)',
    'Grape___healthy', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
    'Potato___healthy', 'Potato___Late_blight', 'Raspberry___healthy', 'Soybean___healthy',
    'Squash___Powdery_mildew', 'Strawberry___healthy', 'Strawberry___Leaf_scorch',
    'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___healthy',
    'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
    'Tomato___Tomato_mosaic_virus', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus'
]

class_names = []

for name in raw_class_names:
    if '___' in name:
        species, condition = name.split('___')
    else:
        species, condition = name, ''
    
    species = species.replace('_', ' ').replace(',', '').title()
    condition = condition.replace('_', ' ').replace(',', '').title()
    
    if condition == 'Healthy':
        label = f"{species} (Healthy)"
    else:
        label = f"{species} - {condition}"
    
    class_names.append(label)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    image_data = data["image"]

    # Decode image
    _, encoded = image_data.split(",", 1)
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded)).convert("RGB")
    image = image.resize((224, 224))  # Use 224x224 for MobileNetV2

    arr = np.array(image).astype("float32") / 255.0
    arr = np.expand_dims(arr, axis=0)

    # Run inference
    interpreter.set_tensor(input_details[0]['index'], arr)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])[0]

    # Get predicted class and confidence
    predicted_index = np.argmax(output)
    confidence = float(output[predicted_index])
    label = class_names[predicted_index]

    return jsonify({
        "resultado": label,
        "confianza": round(confidence, 3)
    })

if __name__ == "__main__":
    app.run(debug=True)
