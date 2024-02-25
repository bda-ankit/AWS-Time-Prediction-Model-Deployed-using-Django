
# AWS Document Uploading Time Pridiction Model and Deployment using Django

AWS Document Uploading Time prediction Model is widely use to make prediction of document uploading time.

Here, I have created this model based on realtime data.

## Model Acknowledgement

Data Preprocessing:
Load your dataset (data.csv) containing features.
Preprocess the data if necessary (e.g., handling missing values, scaling features).

Model Training:
Split the data into training and testing sets.
I have tried various models but perfect fit model is Gragient Boosting Regressor. Train a Gradient Boosting Regressor model on the training data.

Evaluation:
Evaluate the trained model's performance on the testing data using appropriate metrics (e.g., Mean Absolute Error, Mean Squared Error, R-squared).

Export Trained Model:
Once you are satisfied with the model's performance, export it using joblib.

Django Integration:
Create a Django web application.
Set up a view to handle document uploading and prediction.
Load the trained model within the Django application.
Use the loaded model to predict document uploading time based on the input features.

I have used html page to take responses and as per response model predict total time taken to upload all documents.
## Deployment

I have deployed Django app to Vercel. Vercel is free hosting site to deploy our Django app at free of cost.

## Demo

https://awsmodel.vercel.app/

## Authors

- [@bda-ankit](https://www.github.com/bda-ankit)
