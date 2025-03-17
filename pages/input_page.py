import streamlit as st
from calculations import compute_financials

def app():
    st.header("Input & Calculations")
    st.markdown("Provide your financial inputs below:")

    net_worth_risk_tolerance = st.selectbox("Net Worth Risk Tolerance", ["Low", "Moderate", "High"], index=1)
    financial_capital_stocks = st.number_input("Financial Capital - Stocks", value=100000.0, step=1000.0)
    financial_capital_bonds = st.number_input("Financial Capital - Bonds", value=100000.0, step=1000.0)
    financial_capital_cash = st.number_input("Financial Capital - Cash", value=50000.0, step=1000.0)
    current_annual_income = st.number_input("Current Annual Income", value=50000.0, step=1000.0)
    riskiness_of_human_capital = st.selectbox("Riskiness of Human Capital", ["Low", "Average", "High"], index=1)
    current_dc_contribution = st.number_input("Current DC Contribution", value=15000.0, step=1000.0)
    dc_match_percentage = st.number_input("DC Match Percentage", value=50.0, step=1.0)
    nondiscretionary_annual_spending = st.number_input("Nondiscretionary Annual Spending", value=40000.0, step=1000.0)
    current_age = st.number_input("Current Age", value=25, step=1)
    retirement_age = st.number_input("Retirement Age", value=65, step=1)
    sex = st.selectbox("Sex", ["Male", "Female"], index=1)
    subjective_life_expectancy = st.selectbox("Subjective Life Expectancy", ["Low", "Average", "High"], index=1)
    education_level = st.selectbox("Education Level", ["High School", "College", "Graduate"], index=1)
    flexibility_bequest = st.selectbox("Flexibility of Bequest vs. Consumption", ["Low", "Moderate", "High"], index=1)
    strength_bequest = st.selectbox("Strength of Bequest vs. Consumption", ["Low", "Medium", "High"], index=1)

    if st.button("Calculate Financials"):
        financials = compute_financials(
            financial_capital_stocks,
            financial_capital_bonds,
            financial_capital_cash,
            current_annual_income,
            current_dc_contribution,
            dc_match_percentage,
            nondiscretionary_annual_spending,
            current_age,
            retirement_age
        )
        st.markdown("### Financial Outputs")
        st.write(financials)
