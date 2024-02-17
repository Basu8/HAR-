import numpy as np
from flask import Flask, request, jsonify ,render_template
from PIL import Image
from keras.models import load_model

app = Flask(__name__, template_folder='templates')
model = load_model('efficientnet_model.h5')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return 'No image uploaded', 400

    image = request.files['image']
    img = Image.open(image)
    img = img.resize((160, 160))  # Resize the image to match model input size
   
    class_names = ['Sitting', 'Using laptop', 'Hugging', 'Sleeping', 'Drinking', 'Clapping', 'Dancing', 'Cycling', 'Calling', 'Laughing', 'Eating', 'Fighting', 'Listening to music', 'Running', 'Texting', 'Drinking', 'Laughing']
    result = model.predict(np.asarray([img]))

    itemindex = np.where(result==np.max(result))    #
    prediction = itemindex[1][0]
    #print("probability: "+str(np.max(result)*100) + "%\nPredicted class : ", prediction)
    print(class_names[prediction])
    predicted_class = class_names[prediction-1]

    

    return jsonify(predicted_class)

if __name__ == '__main__':
    app.run(debug=True)
