import streamlit as st
import pandas as pd
from PIL import Image


# Dashboard Layout
st.title("Airline Passenger Satisfaction Dashboard")

with st.container():
    st.subheader("Distribution")
    col1, col2, col3 = st.columns(3)

         # Age Group Distribution (Bar Plot)
    with col1:
        st.subheader("Age Group Distribution")
        image1 = Image.open("age_group_distribution.png")
        st.image(image1, caption="Age Group Distribution", use_column_width=True)

    # Satisfaction Breakdown (Pie Chart)
    with col2:
        st.subheader("Satisfaction Breakdown")
        image2 = Image.open("satisfaction_percentage.png")
        st.image(image2, caption="Satisfaction Breakdown", use_column_width=True)

    #Customer Distribution by Customer Type
    with col3:    
        st.subheader("Customer Distribution by Customer Type")
        image3 = Image.open("customer_distribution.png")
        st.image(image3, caption="Customer Distribution by Customer Type", use_column_width=True)



with st.container():
    st.subheader("Distribution")
    col4, col5, col6 = st.columns(3)

         #Customer Distribution by Travel Type
    with col4:
        st.subheader("Customer Distribution by Travel Type")
        image1 = Image.open("cus_distribution_travel.png")
        st.image(image1, caption="Customer Distribution by Travel Type", use_column_width=True)

    # Passengers Distribution by Class
    with col5:
        st.subheader("Passengers Distribution by Class")
        image2 = Image.open("passenger_distribution.png")
        st.image(image2, caption="Passengers Distribution by Class", use_column_width=True)

    #Average Departure and Arrival Delays by Satisfaction Level
    with col6:    
        st.subheader("Average Departure and Arrival Delays by Satisfaction Level")
        image3 = Image.open("average_departure_and_arrival_delay.png")
        st.image(image3, caption="Average Departure and Arrival Delays by Satisfaction Level", use_column_width=True)


with st.container():
    st.subheader("Satisfaction Rate")
    col7, col8, col9 = st.columns(3)

         #Age Group and Class Combinations by Passenger Count
    with col7:
        st.subheader("Age Group and Class Combinations by Passenger Count")
        image1 = Image.open("Agegroup_class.png")
        st.image(image1, caption="Age Group and Class Combinations by Passenger Count", use_column_width=True)

    # Satisfaction Rate by Age Group and Satisfaction Level
    with col8:
        st.subheader("Satisfaction Rate by Age Group and Satisfaction Level")
        image2 = Image.open("satisfaction_rate_age.png")
        st.image(image2, caption="Satisfaction Rate by Age Group and Satisfaction Level", use_column_width=True)

    #Satisfaction Rate by Type of Travel and Satisfaction Level
    with col9:    
        st.subheader("Satisfaction Rate by Type of Travel and Satisfaction Level")
        image3 = Image.open("satisfaction_rate_travel.png")
        st.image(image3, caption="Satisfaction Rate by Type of Travel and Satisfaction Level", use_column_width=True)


with st.container():
    st.subheader("Satisfaction Rate")
    col10, col11 = st.columns(2)

         #Satisfaction Rate by Customer Type and Satisfaction Level
    with col10:
        st.subheader("Satisfaction Rate by Customer Type and Satisfaction Level")
        image1 = Image.open("satisfaction_rate_customer.png")
        st.image(image1, caption="Satisfaction Rate by Customer Type and Satisfaction Level", use_column_width=True)

    #Satisfaction Rate by Class and Satisfaction Level
    with col11:
        st.subheader("Satisfaction Rate by Class and Satisfaction Level")
        image1 = Image.open("satisfaction_rate_class.png")
        st.image(image1, caption="Satisfaction Rate by Class and Satisfaction Level", use_column_width=True)
        

with st.container():
    st.subheader("Satisfaction Correlation")
    col12, col13 = st.columns(2)


    #Satisfaction Correlation between Age Groups and Various Variables
    with col12:
        st.subheader("Satisfaction Correlation between Age Groups and Various Variables")
        image3 = Image.open("satisfaction_correlation_age.png")
        st.image(image3, caption="Satisfaction Correlation between Age Groups and Various Variables", use_column_width=True)


    #Satisfaction Correlation between Travel Class and Various Variables
    with col13:
        st.subheader("Satisfaction Correlation between Travel Class and Various Variables")
        image3 = Image.open("satisfaction_correlation_class.png")
        st.image(image3, caption="Satisfaction Correlation between Travel Class and Various Variables", use_column_width=True)


with st.container():
    st.subheader("Satisfaction Correlation")
    col14, col15 = st.columns(2)


    #Satisfaction Correlation between Travel Type and Various Variables
    with col14:
        st.subheader("Satisfaction Correlation between Travel Type and Various Variables")
        image3 = Image.open("satisfaction_correlation_type.png")
        st.image(image3, caption="Satisfaction Correlation between Travel Type and Various Variables", use_column_width=True)


    #Satisfaction Correlation between Customer Type and Various Variables
    with col15:
        st.subheader("Satisfaction Correlation between Customer Type and Various Variables")
        image3 = Image.open("satisfaction_correlation_customer.png")
        st.image(image3, caption="Satisfaction Correlation between Customer Type and Various Variables", use_column_width=True)