# prediction.py

Accident_severity_dict = {
    0: 'Minor',
    1: 'Moderate',
    2: 'Severe'
}

def get_prediction(model, input_df):
    prediction = model.predict(input_df)[0]
    print("DEBUG: Prediction value from model =", prediction)
    return Accident_severity_dict[prediction]
