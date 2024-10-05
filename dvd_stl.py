import streamlit as st


# Streamlit app title
st.title("DVD Rental Amount Prediction")

# Show MSE for the trained model
st.write(f"Model Mean Squared Error: {MSE:.2f}")

# Input fields for user to make predictions

st.header("Enter Rental Details")

rental_duration = st.slider("Rental Duration (days)", min_value=1, max_value=7, value=5)
rental_rate = st.slider("Rental Rate ($)", min_value=1.0, max_value=5.0, value=3.0)
length = st.slider("Film Length (minutes)", min_value=50, max_value=200, value=100)
replacement_cost = st.slider("Replacement Cost ($)", min_value=10.0, max_value=30.0, value=20.0)

rating = st.selectbox("Film Rating", df['rating'].unique())
category = st.selectbox("Film Category", df['category'].unique())
language = st.selectbox("Film Language", df['language'].unique())
store_id = st.selectbox("Store ID", df['store_id'].unique())

# Make a prediction
if st.button("Predict Amount"):
    user_data = pd.DataFrame({
        'rental_duration': [rental_duration],
        'rental_rate': [rental_rate],
        'length': [length],
        'replacement_cost': [replacement_cost],
        'rating': [rating],
        'category': [category],
        'language': [language],
        'store_id': [store_id]
    })
    
    predicted_amount = new_model.predict(user_data)[0]
    
    st.write(f"Predicted Rental Amount: ${predicted_amount:.2f}")
