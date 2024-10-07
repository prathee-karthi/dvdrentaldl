import streamlit as st
import pandas as pd
import numpy as np

from tensorflow.keras.models import load_model




st.set_page_config(
    page_title="Predicting Customer Behavior in DVD Rental Using Deep Learning with AWS deployment",
    page_icon='dl.png'
)



model = load_model('dl_relu.h5')

# Set page configuration


# Apply CSS styling
st.markdown("""
<style>
h1 {
    color:	#black; /* Change to your desired color */
    font-size: 34px;
}
</style>
""", unsafe_allow_html=True)


def main():
    option = st.sidebar.radio("Navigation", ["Home", "App Page"])
    if option == "Home":
        st.title("DVD Rental - Postgre SQL - Deep Learning")
        st.write("""
        The DVD rental dataset provides a comprehensive view of rental transactions for a fictional DVD rental company. It includes various details such as the DVD title, rental duration, rental rate, film category, customer information, and transaction dates.
        This dataset offers rich insights into rental patterns, customer preferences, and film popularity.

        By leveraging this dataset, we can build predictive models using deep learning techniques to address key business problems. For instance, demand forecasting can help predict future rental trends based on historical data, while a recommendation system could suggest personalized DVD titles to customers based on their past behavior. Additionally, churn prediction models can identify customers at risk of discontinuing the service, enabling proactive retention strategies.

        In this application, we will train a deep learning model (e.g., a neural network or an LSTM) using this dataset and deploy it to AWS to serve predictions in real time. AWS services like SageMaker will be used to train, optimize, and deploy the model at scale, while AWS Lambda or EC2 can be used for handling requests and inference.
        This combination of AWS and Streamlit provides an efficient and scalable way to deploy deep learning models while keeping the user interface simple and interactive.

        """)
    
    elif option == "App Page":
        st.title("Final Project - DVD Rental Deep Learning")
        
        
        rental_duration = st.selectbox("Rental Duration",["Select Rental Duration"]+[3,4,5,6,7])
        rental_rate =st.slider("Rental_rate", min_value=0, max_value=10)
        length = st.slider("Length of the movie", min_value = 45, max_value=185)
        replacement_cost = st.selectbox("Replacement Cost",["Select Replacement Cost"]+[9.99, 10.99, 11.99, 12.99, 13.99, 14.99, 15.99, 16.99, 17.99, 18.99, 19.99, 20.99, 21.99, 22.99, 23.99, 24.99, 25.99, 26.99, 27.99, 28.99, 29.99])
        rating = st.selectbox("Rating",["Select Rating"]+['PG-13','NC-17','PG','R','G'])
        category = st.selectbox("Category",['Select Category']+['Horror', 'Documentary', 'New', 'Classics', 'Games', 'Sci-Fi',
       'Foreign', 'Family', 'Travel', 'Music', 'Sports', 'Comedy',
       'Drama', 'Action', 'Children', 'Animation'])
        active = st.selectbox("Status",['Select Status']+['Active','Not Active'])
        # rental_month = st.selectbox("Rental_month",['Select Rental Month']+[6,7,8])
        # rental_day = st.slider("Rental Day", min_value = 1, max_value=31)
        # return_month = st.selectbox("Return_month",['Select Return Month']+[6,7,8])
        rental_actual_duration = st.slider("Rental_actual_duraton", min_value = 1, max_value=100)
        

        details1 = []
        
        
        if rental_duration != "Rental Duration":
            details1.append(float(rental_duration))
        else:
            st.warning("Please choose correct any option in body type box")
        if rental_rate:
            details1.append(float(rental_rate))
        if length:
            details1.append(float(length))    
        if replacement_cost != "Select Replacement Cost":
            details1.append(float(replacement_cost))
        else:
            st.warning("Please choose Rental Duration")
        if rating != "Select Rating":
            rating_array = ['PG-13','NC-17','PG','R','G']
            num_rating = rating_array.index(rating)
            details1.append(float(num_rating))
        else:
            st.warning("Please choose Rating")

        if category != "Select Category":
            array = ['Horror', 'Documentary', 'New', 'Classics', 'Games', 'Sci-Fi',
            'Foreign', 'Family', 'Travel', 'Music', 'Sports', 'Comedy',
            'Drama', 'Action', 'Children', 'Animation']
            num = array.index(category)
            details1.append(float(num))
        else:
            st.warning("Please Select Category")           
        if active != 'Select Status':
            status = ['Active','Not Active']
            num_stat = status.index(active)
            details1.append(float(num_stat))
        else:
            st.warning("Please Select Status")
        if rental_actual_duration:
            details1.append(float(rental_actual_duration))
    

        if st.button("Estimate Price"):
            dvd_amount = model.predict(np.array([details1]))
            st.success(f"Estimated Price: {round(dvd_amount[0][0], 2)}")

if __name__ == "__main__":
    main()