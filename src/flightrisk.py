# src/flightrisk.py

def detect_flight_risk(df):
    # keep only negative messages
    df_neg = df[df["sentiment"] == "Negative"].copy()

    # sort by sender ("from") and date
    df_neg = df_neg.sort_values(["from", "date"])

    risk_employees = set()

    # count negative messages per employee
    negative_counts = df_neg["from"].value_counts()

    # rule: employees with 3 or more negative messages = at risk
    for employee, count in negative_counts.items():
        if count >= 3:
            risk_employees.add(employee)

    return risk_employees
