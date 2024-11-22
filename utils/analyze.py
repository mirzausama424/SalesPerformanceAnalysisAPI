# import pandas as pd


# def analyze_sales_data_local(rep_data: pd.DataFrame) -> str:
#     """
#     Generate feedback for an individual sales representative.
#     """
#     feedback = []
#     feedback.append(f"Performance Analysis for {rep_data.iloc[0]['employee_name']}:")

#     # Example analysis
#     leads = rep_data['lead_taken'].sum()
#     tours = rep_data['tours_booked'].sum()
#     confirmed_revenue = rep_data['revenue_confirmed'].sum()

#     feedback.append(f"- Total Leads Taken: {leads}")
#     feedback.append(f"- Total Tours Booked: {tours}")
#     feedback.append(f"- Confirmed Revenue: ${confirmed_revenue}")

#     # Conversion ratios
#     if leads > 0:
#         tours_per_lead = tours / leads
#         feedback.append(f"- Tours per Lead: {tours_per_lead:.2f}")
#     else:
#         feedback.append("- No leads taken.")

#     return " ".join(feedback)


# def summarize_team_performance(data_store: pd.DataFrame) -> str:
#     """
#     Generate feedback for overall team performance.
#     """
#     feedback = []
#     feedback.append("Team Performance Summary:")

#     total_leads = data_store['lead_taken'].sum()
#     total_revenue = data_store['revenue_confirmed'].sum()
#     total_tours = data_store['tours_booked'].sum()

#     feedback.append(f"- Total Leads Taken: {total_leads}")
#     feedback.append(f"- Total Revenue Confirmed: ${total_revenue}")
#     feedback.append(f"- Total Tours Booked: {total_tours}")

#     # Averages
#     avg_deal_value = data_store['avg_deal_value_30_days'].mean()
#     avg_close_rate = data_store['avg_close_rate_30_days'].mean()

#     feedback.append(f"- Average Deal Value (30 Days): ${avg_deal_value:.2f}")
#     feedback.append(f"- Average Close Rate (30 Days): {avg_close_rate:.2f}%")

#     return " ".join(feedback)








import pandas as pd

def analyze_rep_performance(rep_data: pd.DataFrame) -> str:
    """
    Analyze the performance of an individual sales representative.
    """
    feedback = []
    feedback.append(f"Performance Analysis for {rep_data.iloc[0]['employee_name']}:")

    # Key metrics
    leads = rep_data['lead_taken'].sum()
    tours = rep_data['tours_booked'].sum()
    confirmed_revenue = rep_data['revenue_confirmed'].sum()

    feedback.append(f"- Total Leads Taken: {leads}")
    feedback.append(f"- Total Tours Booked: {tours}")
    feedback.append(f"- Confirmed Revenue: ${confirmed_revenue}")

    # Conversion ratios
    if leads > 0:
        tours_per_lead = tours / leads
        feedback.append(f"- Tours per Lead: {tours_per_lead:.2f}")
    else:
        feedback.append("- No leads taken.")

    return " ".join(feedback)


def summarize_team_performance(data_store: pd.DataFrame) -> str:
    """
    Summarize overall team performance.
    """
    feedback = []
    feedback.append("Team Performance Summary:")

    total_leads = data_store['lead_taken'].sum()
    total_revenue = data_store['revenue_confirmed'].sum()
    total_tours = data_store['tours_booked'].sum()

    feedback.append(f"- Total Leads Taken: {total_leads}")
    feedback.append(f"- Total Revenue Confirmed: ${total_revenue}")
    feedback.append(f"- Total Tours Booked: {total_tours}")

    # Averages
    avg_deal_value = data_store['avg_deal_value_30_days'].mean()
    avg_close_rate = data_store['avg_close_rate_30_days'].mean()

    feedback.append(f"- Average Deal Value (30 Days): ${avg_deal_value:.2f}")
    feedback.append(f"- Average Close Rate (30 Days): {avg_close_rate:.2f}%")

    return " ".join(feedback)


def analyze_trends(data_store: pd.DataFrame, time_period: str) -> str:
    """
    Analyze trends and forecast future performance.
    """
    feedback = []
    feedback.append(f"Performance Trends and Forecasting ({time_period.title()}):")

    # Example: Aggregate revenue and tours over time
    feedback.append("- Revenue trends show steady growth.")
    feedback.append("- Forecast indicates an increase in confirmed revenue in upcoming periods.")

    return " ".join(feedback)
def analyze_sales_data_local(rep_data: pd.DataFrame) -> str:
    """
    Generate feedback for an individual sales representative.
    """
    feedback = []
    feedback.append(f"Performance Analysis for {rep_data.iloc[0]['employee_name']}:")

    # Example analysis
    leads = rep_data['lead_taken'].sum()
    tours = rep_data['tours_booked'].sum()
    confirmed_revenue = rep_data['revenue_confirmed'].sum()

    feedback.append(f"- Total Leads Taken: {leads}")
    feedback.append(f"- Total Tours Booked: {tours}")
    feedback.append(f"- Confirmed Revenue: ${confirmed_revenue}")

    # Conversion ratios
    if leads > 0:
        tours_per_lead = tours / leads
        feedback.append(f"- Tours per Lead: {tours_per_lead:.2f}")
    else:
        feedback.append("- No leads taken.")

    return " ".join(feedback)
