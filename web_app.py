import streamlit as st
from calculator import Trade_checkpoints

# Create a Streamlit app
st.title("Option Buying Risk Management Calculator.")
st.header("Let's Be Mentally Prepared for Your Potential Loss!!!")
github_link = "[GitHub Repository](https://github.com/skshohaib11/Stoploss_calculator)"
LinkedIn_link = "[LinkedIn](https://www.linkedin.com/in/shaikh-mohammed-shohaib-043317251/)"


# Sidebar
st.sidebar.title("About The Calculator.")
st.sidebar.write("As we know that setting a stoploss is a good practice while trading.")
st.sidebar.write("This will provide an overview of the loss amount and loss percentage, as the exact values will depend on the options greeks and other parameters.")
st.sidebar.write("However this was built to know what will be the potential loss when you enter a trade and set your stoplosses according to your loss bearing capacity.")
st.sidebar.write("The target point on each trade can be set from 5 to 100 points keeping in mind these target values can vary for different indivisual and the profit percentage would vary in different sectors and different option selection.")
st.sidebar.write("Please set your targets as per your strategy and risk to reward ratio.")
st.sidebar.write("Knowing the fact that options are very volatile and at times after you take an entry position you will be calculating your exit point mainly stoploss and due to volatility you may incur more losses in sudden price fluctuations.")
st.sidebar.write("So to save your time in calculation this calculator is mainly focused on setting stoploss by knowing in advance the rough estimate of amount that can be lost in that particular trade and to be prepared for the same.")
st.sidebar.write("You can always utilize this code inorder to set your parameters according to your strategy and risk to reward ratio.")
st.sidebar.write("You can find the code details in my github repository in the given link below.")
st.sidebar.markdown(github_link)
st.sidebar.markdown(LinkedIn_link)
st.sidebar.write('Prepared By: Shohaib Shaikh')

# Input field for selecting the sector
selected_sector = st.selectbox("Select Sector:", ["Nifty", "Sensex", "Bank Nifty", "Finnifty"])

# Create a three-column layout (adjust the layout as needed)
col1, col2, col3 = st.columns(3)

# Input field for Buy Price
buy_price = col1.number_input("Enter Buy Price:", min_value=0.01, format="%f")

# Define the quantity constraints based on the selected sector
quantity_constraints = {
    "Nifty": 50,
    "Sensex": 10,
    "Bank Nifty": 15,
    "Finnifty": 40,
}

# Input field for Quantity with sector-specific constraints
quantity = col2.selectbox(
    f"Select Quantity (Multiples of {quantity_constraints[selected_sector]}):",
    list(range(quantity_constraints[selected_sector], 3000, quantity_constraints[selected_sector]))
)
# Input field for Target Points (multiples of 5, up to 100)
target_points = col3.number_input("Target Points :", min_value=5, max_value=100, step=5, format="%d")

# Calculate button
if st.button("Calculate"):
    # Create an instance of the Trade_checkpoints class
    trade = Trade_checkpoints(buy_price, quantity)
    
    # Calculate the target based on the provided target points
    target = buy_price + target_points
    target_percentage = round((target_points / buy_price) * 100, 2)
    
    # Display the amount invested, target, and target percentage
    st.write(f"Amount Invested: {trade.invested_amount}")
    st.write(f"Target Points: {target_points}")
    st.write(f"Target Price: {target}")
    st.write(f"Target Percentage: {target_percentage} %")
    
    # Display the loss details for different points
    st.header("Stoploss Details:")

    # Define a list of points
    points = [5, 10, 15, 20, 25, 30]

    for point in points:
        stop_loss = trade.Buy_Price - point
        loss_percentage = round((point / trade.Buy_Price) * 100, 2)
        loss_amount = round((loss_percentage / 100) * trade.invested_amount)

        st.write(f"")
        st.write(f"Points: {point} -----> Stop Loss: {stop_loss} -----> Loss Percentage: {loss_percentage} % -----> Loss Amount: {loss_amount}")


st.write('DISCLAIMER:')
st.write('Before you use this calculator please visit the about section in the side bar by clicking on the arrow at top left side of this page.')
