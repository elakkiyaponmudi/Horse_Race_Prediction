import streamlit as st
import pandas as pd
import pickle

# Load the trained model (Random Forest)
model = pickle.load(open(r"C:\Users\Elakkiya\Downloads\horse_race_prediction_rf_model.pkl", 'rb'))

# Load the CSV file containing input data with the appropriate encoding
csv_file_path = r"C:\Users\Elakkiya\Downloads\Horse Race Prediction\processed_horse_race_data_filtered.csv"
input_df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')  # Change the encoding if necessary

# Streamlit UI
st.title("Horse Race Position Prediction")

# Show the input data
st.write("Input Data:")
st.write(input_df)

# Function to get user input from the displayed data
def get_user_input():
    # Collect user inputs for the relevant features
    title = float(st.text_input("Title", value="0.0"))
    winning_time = float(st.text_input("Winning Time", value="0.0"))
    prize = float(st.text_input("Prize", value="0.0"))
    decimal_price = float(st.text_input("Decimal Price", value="0.0"))
    positionL = float(st.text_input("PositionL", value="0.0"))
    dist = float(st.text_input("Dist", value="0.0"))
    RPR = float(st.text_input("RPR", value="0.0"))
    TR = float(st.text_input("TR", value="0.0"))
    OR = float(st.text_input("Official Rating (OR)", value="0.0"))
    runners = float(st.text_input("Runners", value="0.0"))
    res_place = float(st.text_input("Res Place", value="0.0"))
    place_rate = float(st.text_input("Place Rate", value="0.0"))
    average_margin = float(st.text_input("Average Margin", value="0.0"))
    log_prize = float(st.text_input("Log Prize", value="0.0"))

    # Create a DataFrame with the user inputs
    input_data = {
        "title": title,
        "winningTime": winning_time,
        "prize": prize,
        "decimalPrice": decimal_price,
        "positionL": positionL,
        "dist": dist,
        "RPR": RPR,
        "TR": TR,
        "OR": OR,
        "runners": runners,
        "res_place": res_place,
        "place_rate": place_rate,
        "average_margin": average_margin,
        "log_prize": log_prize
    }
    
    input_df = pd.DataFrame(input_data, index=[0])
    return input_df

# Main function to predict the result
def predict_position(input_df):
    # Predict the position using the trained model
    prediction = model.predict(input_df)
    return prediction

# Get user input
input_df = get_user_input()

# Show the entered data
st.write("Entered Data:")
st.write(input_df)

# Button to predict the position
if st.button("Predict Position"):
    # Predict the position based on user input
    predicted_position = predict_position(input_df)
    
    # Display the predicted position
    st.write(f"Predicted Position: {predicted_position[0]}")