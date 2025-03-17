def compute_financials(stocks, bonds, cash, income, dc_contrib, dc_match, spending, current_age, ret_age):
    # Total Financial Wealth
    total_financial_wealth = stocks + bonds + cash
    # Estimated Value of Human Capital: Simplified present value of future income
    human_capital = income * (ret_age - current_age)
    # Estimated Value of Liabilities: Set as half of human capital for demonstration
    liabilities = human_capital * 0.5
    # Estimated Net Worth: financial wealth + human capital - liabilities
    net_worth = total_financial_wealth + human_capital - liabilities
    # Initial Consumption: demonstration formula: 1.2 x income
    initial_consumption = income * 1.2
    # Bequest: demonstration formula: 1.05 x net worth
    bequest = net_worth * 1.05

    # Compute allocations (in percentages)
    total = stocks + bonds + cash
    stocks_alloc_implied = (stocks / total) * 100 if total else 0
    bonds_alloc_implied = (bonds / total) * 100 if total else 0
    cash_alloc_implied = (cash / total) * 100 if total else 0
    # Quasi-recommended allocations (made-up adjustment for demo)
    stocks_alloc_recommended = stocks_alloc_implied + 0.5
    bonds_alloc_recommended = bonds_alloc_implied + 7.33
    cash_alloc_recommended = max(0, 100 - stocks_alloc_recommended - bonds_alloc_recommended)

    return {
        "Total Financial Wealth": total_financial_wealth,
        "Estimated Value of Human Capital": human_capital,
        "Estimated Value of Liabilities": liabilities,
        "Estimated Net Worth": net_worth,
        "Initial Consumption": initial_consumption,
        "Bequest": bequest,
        "Current / Implied Allocations": {
            "Stocks": round(stocks_alloc_implied, 2),
            "Bonds": round(bonds_alloc_implied, 2),
            "Cash": round(cash_alloc_implied, 2),
        },
        "Quasi-Recommended Allocations": {
            "Stocks": round(stocks_alloc_recommended, 2),
            "Bonds": round(bonds_alloc_recommended, 2),
            "Cash": round(cash_alloc_recommended, 2),
        }
    }
