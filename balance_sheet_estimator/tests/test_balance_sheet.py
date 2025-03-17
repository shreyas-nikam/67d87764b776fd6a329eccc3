def run_tests():
    print("Running Tests...")
    
    inputs = {
        'financial_capital_stocks': 100000,
        'financial_capital_bonds': 100000,
        'financial_capital_cash': 50000,
        'current_annual_income': 50000,
        'current_dc_contribution': 15000,
        'dc_match_percentage': 50,
        'nondiscretionary_annual_spending': 40000,
        'current_age': 25,
        'retirement_age': 65,
    }

    # Test - Calculate Financial Metrics
    metrics = calculate_financial_metrics(inputs)
    assert len(metrics) == 4, "Financial metrics did not return 4 values"
    print("Financial Metrics Test Passed!")
    
    # Test - Input Handling
    input_page()  # This would use Streamlit to set session state
    assert 'user_inputs' in st.session_state, "User inputs are not present in session state"
    print("Input Handling Test Passed!")

    # Test - Visualization Output
    visualization_page(0, 0, 0, 0)  # Execute to ensure it runs without error
    print("Visualization Test Executed Successfully!")

run_tests()
