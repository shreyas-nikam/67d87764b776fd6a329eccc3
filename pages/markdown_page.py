import streamlit as st

def app():
    st.header("Documentation & Explanations")
    st.markdown("""
    # Balance Sheet Estimator - Documentation

    This application simulates a balance sheet estimator where users can input financial parameters and
    observe dynamic calculations and interactive visualizations.

    ## Calculated Financial Metrics

    - **Total Financial Wealth**: Sum of stocks, bonds, and cash.
    - **Estimated Value of Human Capital**: Calculated as current annual income multiplied by the remaining working years.
    - **Estimated Value of Liabilities**: Estimated as half of your human capital (for demonstration).
    - **Estimated Net Worth**: Total financial wealth plus human capital minus liabilities.
    - **Initial Consumption**: Based on a multiple of your annual income.
    - **Bequest**: An arbitrarily set multiplication of net worth.

    ## Visualizations Included

    - **Line Chart**: Trends net worth over time.
    - **Bar Graph**: Displays asset allocation percentages.
    - **Scatter Plot**: Demonstrates random data points for interactivity.

    ## Interactivity

    All inputs update the calculations and visualizations in real time. Tooltips and markdown explainers provide additional details.

    Enjoy exploring the balance sheet estimator!
    """)
