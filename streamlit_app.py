import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Mock database of signals (replace this with your actual data)
signals_data = pd.DataFrame({
    'Signal ID': [1, 2, 3],
    'Signal Name': ['Signal A', 'Signal B', 'Signal C'],
    'Description': ['Signal A Explanation', 'Signal B Explanation', 'Signal C Explanation'],
    'Buy Price': [100, 120, 110],
    'Sell Price': [110, 125, 115],
    'Performance': [10, 5, 4],  # Percentage change
    'Date': ['2024-12-25', '2024-12-26', '2024-12-27'],
})

# Function to show performance history of a signal
def plot_performance(signal_id):
    # Placeholder for the actual trading data, here using mock data
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=signals_data['Date'],
        y=signals_data['Performance'],
        mode='lines+markers',
        name='Performance'
    ))
    fig.update_layout(title=f"Signal {signal_id} Performance", xaxis_title="Date", yaxis_title="Performance (%)")
    st.plotly_chart(fig)

# Title of the app
st.title("Trade Signal Marketplace")

# Dropdown to select a signal
signal_id = st.selectbox('Choose a trading signal', signals_data['Signal Name'])

# Get the details of the selected signal
signal_details = signals_data[signals_data['Signal Name'] == signal_id].iloc[0]
st.write(f"**Signal Name**: {signal_details['Signal Name']}")
st.write(f"**Description**: {signal_details['Description']}")
st.write(f"**Buy Price**: {signal_details['Buy Price']}")
st.write(f"**Sell Price**: {signal_details['Sell Price']}")
st.write(f"**Performance**: {signal_details['Performance']}%")

# Plot performance history
plot_performance(signal_id)

# Subscription button (for the user to subscribe to a signal)
if st.button(f"Subscribe to {signal_id}"):
    st.success(f"You have subscribed to {signal_id}!")

# Additional features: User authentication (optional)
