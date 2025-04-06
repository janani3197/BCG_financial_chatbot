# Financial Chatbot

This Financial Chatbot is designed to assist users with queries related to financial metrics of companies for specific years. The chatbot allows users to ask about various financial metrics, such as total revenue, net income, growth rates, and more. The chatbot will respond with relevant data retrieved from an Excel file containing historical financial data.

## How It Works

1. **User Input**: The user enters a question in the text box at the bottom of the page. The question should be related to a specific company and financial metric for a particular year.
   
2. **Query Parsing**: The chatbot extracts:
   - **Company Name**: Identifies the company based on the user's query.
   - **Year**: Detects a year in the format of four digits (e.g., 2023).
   - **Metric**: Matches the query with predefined financial metrics (e.g., total revenue, net income).
   
3. **Response Generation**: Based on the identified company, year, and metric, the chatbot either:
   - Retrieves the specific value for the given metric from the dataset.
   - Calculates and returns the change in the metric compared to the previous year.
   
4. **Conversation History**: All questions and answers are stored in the session state and displayed in a chat-like format with alternating user and bot messages.

## PREDEFINED QUERIES

The chatbot can respond to the following types of queries:

- **Direct Metric Queries**: Users can ask for a specific metric for a company in a given year. Examples:
   - "What is the total revenue for Microsoft in 2023?"
   - "What was the net income for Tesla in 2022?"
   
- **Change in Metric Queries**: Users can ask how a financial metric has changed from one year to another. Examples:
   - "How has revenue changed for Microsoft?"
   - "What is the net income growth for Tesla?"
   - "How has cash flow changed for Apple?"

The chatbot supports the following metrics:
- **Total Revenue**
- **Net Income**
- **Total Assets**
- **Total Liabilities**
- **Cash Flow**
- **Revenue Growth**
- **Net Income Growth**
- **Assets Growth**
- **Liabilities Growth**
- **Cash Flow Growth**

## LIMITATIONS

- **Data Availability**: The chatbot relies on an Excel file containing financial data. If the data for the queried company or year is missing, the chatbot will respond with "Sorry, no data available."
  
- **Query Structure**: The chatbot requires queries to follow a certain structure, with both the company name and the year explicitly mentioned. For example, a query like "What is the total revenue for Microsoft in 2023?" will work, but "What is the revenue?" will not.
  
- **Data Precision**: The data returned is only as accurate as the Excel file provided. If the data is outdated or incomplete, the chatbot will not be able to answer accordingly.
  
- **No Complex Calculations**: The chatbot can handle only basic operations based on the dataset, such as retrieving values and calculating simple year-over-year changes. Complex financial analyses or predictions are beyond its capabilities.

## CONCLUSION

The Financial Chatbot provides an easy and interactive way to get financial data for specific companies and years, including direct metrics and year-over-year changes. It is designed for quick, straightforward financial queries but is limited by the data available in the underlying Excel file and the need for precise query formatting.
