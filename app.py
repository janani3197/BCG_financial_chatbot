import streamlit as st
import pandas as pd
import re

# Load the Excel file
df = pd.read_excel("Task_2_data.xlsx")

# Normalize columns for easier handling
df.columns = df.columns.str.strip().str.lower()
df['company'] = df['company'].str.lower()

# Function to retrieve direct metric
def get_direct_metric(company, year, metric, df):
    metric_mapping = {
        'total revenue': 'total revenue',
        'net income': 'net income',
        'total assets': 'total assets',
        'total liabilities': 'total liabilities',
        'cash flow': 'cash flow from operating activities',
        'revenue growth': 'revenue growth (%)',
        'net income growth': 'net income growth (%)',
        'assets growth': 'assets growth (%)',
        'liabilities growth': 'liabilities growth (%)',
        'cash flow growth': 'cash flow growth (%)'
    }

    metric_column = metric_mapping.get(metric.lower())
    if not metric_column:
        return "Sorry, the metric you're asking for is not available."

    company_data = df[(df['company'].str.lower() == company.lower()) & (df['year'] == year)]
    
    if not company_data.empty:
        value = company_data.iloc[0][metric_column]
        return f"The {metric} for {company} in {year} is {value:.2f}."
    else:
        return f"Sorry, no data available for {company} in {year}."

def get_change_query(company, metric):
    company = company.lower()
    company_data = df[df['company'] == company].sort_values(by='year')

    if not company_data.empty:
        if 'net income' in metric:
            metric_column = 'net income'
        elif 'assets' in metric:
            metric_column = 'total assets'
        elif 'liabilities' in metric:
            metric_column = 'total liabilities'
        elif 'revenue' in metric:
            metric_column = 'total revenue'
        elif 'cash flow' in metric:
            metric_column = 'cash flow from operating activities'
        elif 'growth' in metric:
            if 'revenue' in metric:
                metric_column = 'revenue growth (%)'
            elif 'net income' in metric:
                metric_column = 'net income growth (%)'
            elif 'assets' in metric:
                metric_column = 'assets growth (%)'
            elif 'liabilities' in metric:
                metric_column = 'liabilities growth (%)'
            elif 'cash flow' in metric:
                metric_column = 'cash flow growth (%)'
            else:
                return "Sorry, I couldn't understand the metric you are asking about."

        metric_changes = company_data[['year', metric_column]]
        metric_changes['change'] = metric_changes[metric_column].diff()
        
        recent_data = metric_changes.iloc[-1]
        prev_data = metric_changes.iloc[-2] if len(metric_changes) > 1 else None

        if prev_data is not None:
            metric_change = recent_data['change']
            change_type = "increase" if metric_change > 0 else "decrease"
            change_percentage = (metric_change / prev_data[metric_column]) * 100
            return f"The {metric_column.replace('_', ' ').title()} for {company.title()} has {change_type} by ${abs(metric_change):,.2f} ({abs(change_percentage):.2f}% change) from {recent_data['year']} to {prev_data['year']}."
        else:
            return f"Not enough data to calculate {metric_column.replace('_', ' ').title()} change for {company.title()}."
    else:
        return f"Sorry, no data found for {company.title()}."

# Initialize session state to store conversation history
if 'conversation_history' not in st.session_state:
    st.session_state['conversation_history'] = []

# Display the conversation history
def display_conversation():
    for entry in st.session_state['conversation_history']:
        st.write(f"**You:** {entry['question']}")
        st.write(f"**Bot:** {entry['answer']}")

def main():
    st.title("Financial Chatbot")

    # Get user input
    user_input = st.text_input("Ask a question:")

    if user_input:
        company = None
        year = None
        metric = None
        
        # Extract company name (case insensitive match)
        companies = df['company'].unique()
        company = next((c for c in companies if c.lower() in user_input.lower()), None)

        # Extract year (if present in the format of 4 digits)
        year_match = re.search(r'\b\d{4}\b', user_input)
        year = int(year_match.group()) if year_match else None
        
        # Define the list of metrics
        metrics = ['total revenue', 'net income', 'total assets', 'total liabilities', 'cash flow', 'revenue growth', 
                   'net income growth', 'assets growth', 'liabilities growth', 'cash flow growth']

        # Extract metric (if present in the user input)
        metric = next((m for m in metrics if m in user_input.lower()), None)

        # Case 1: Direct Metric Query
        if company and year and metric:
            response = get_direct_metric(company, year, metric, df)

        # Case 2: Change Query
        elif company and metric:
            response = get_change_query(company, metric)
        else:
            response = "Sorry, I couldn't understand the query. Please ask about a financial metric for a specific company and year."

        # Store the conversation
        st.session_state['conversation_history'].append({"question": user_input, "answer": response})

        # Display the current and previous conversations
        display_conversation()

if __name__ == "__main__":
    main()
