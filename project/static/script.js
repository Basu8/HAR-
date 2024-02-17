function predict() {
    const fileUpload = document.getElementById('fileUpload');
    const resultDiv = document.getElementById('result');
    const uploadedImage = document.getElementById('uploadedImage');
    const file = fileUpload.files[0];
    const formData = new FormData();
    formData.append('image', file);

    // Display the uploaded image
    const reader = new FileReader();
    reader.onload = function(event) {
        uploadedImage.src = event.target.result;
        uploadedImage.style.display = 'block'; // Show the image
    }
    reader.readAsDataURL(file);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(prediction => {
        resultDiv.innerText ='Prediction'+prediction; // Add a semicolon at the end of the line
    })
    .catch(error => {
        console.error('Error predicting:', error);
    });
}