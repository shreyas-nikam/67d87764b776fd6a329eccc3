import streamlit as st
import plotly.graph_objs as go
import random

def app():
    st.header("Visualizations")
    st.markdown("Explore interactive visualizations of your financial data.")

    # Sample data for net worth presentation
    years = list(range(2020, 2031))
    net_worth = [100000 + 10000*(i - 2020) for i in years]

    # Line Chart - Net Worth over time
    line_fig = go.Figure()
    line_fig.add_trace(go.Scatter(x=years, y=net_worth, mode='lines+markers', name='Net Worth'))
    line_fig.update_layout(title="Net Worth Over Time", xaxis_title="Year", yaxis_title="Net Worth")
    st.plotly_chart(line_fig, use_container_width=True)

    # Bar Graph - Asset Allocations example
    allocations = {'Stocks': 47.06, 'Bonds': 39.15, 'Cash': 13.78}
    bar_fig = go.Figure(data=[go.Bar(x=list(allocations.keys()), y=list(allocations.values()))])
    bar_fig.update_layout(title="Asset Allocations", xaxis_title="Asset", yaxis_title="Percentage")
    st.plotly_chart(bar_fig, use_container_width=True)

    # Scatter Plot - Random demo data
    x_vals = [random.randint(1, 100) for _ in range(10)]
    y_vals = [random.randint(1, 100) for _ in range(10)]
    scatter_fig = go.Figure(data=go.Scatter(x=x_vals, y=y_vals, mode='markers'))
    scatter_fig.update_layout(title="Random Scatter Plot", xaxis_title="X", yaxis_title="Y")
    st.plotly_chart(scatter_fig, use_container_width=True)
