# BCG: AI-powered Financial Analysis Chatbot

## Project Brief

### Background Context
The GenAI Consulting team at BCG has been approached by a leading global financial institution, **Global Finance Corp. (GFC)**, to address a pressing challenge in their operations. GFC, amid a rapidly evolving financial landscape, is seeking to enhance its capabilities in analyzing corporate financial performance. They have identified a need for a sophisticated, AI-driven solution to stay ahead in the market and provide their clients with deeper, more accessible insights into corporate financial health.

GFC's traditional methods of financial analysis, though reliable, have become time-consuming and less efficient in the face of increasing data volumes and the fast pace of financial markets. They are looking to BCG, known for its cutting-edge AI solutions, to develop a tool that can quickly analyze and interpret large sets of financial data, specifically from **10-K** and **10-Q reports**.

### The Project
Developing an AI-powered chatbot that can analyze and provide insights on corporate financial performance from **10-K** and **10-Q** financial documents. This chatbot is intended to revolutionize the way GFC and its clients interact with financial data, making complex information easily accessible and understandable through conversational AI.

### Key Terms
- **10-K and 10-Q Reports**: Annual and quarterly financial reports filed by publicly traded companies containing detailed information about financial performance.
- **GenAI**: A branch of AI focusing on generating new content, including text and data analysis, which is crucial for the chatbot's ability to interpret and communicate financial data.
- **Natural Language Processing (NLP)**: An AI technology that the chatbot will use to understand and respond to user queries in natural language.

### Specific Project Requirements and Outcomes
- **Efficiency**: The solution must significantly reduce the time taken to analyze financial documents compared to traditional methods.
- **Accuracy**: The chatbot should provide precise and reliable financial insights backed by thorough data analysis.
- **User-friendly Interface**: The chatbot should be intuitive and easy to use for GFC’s diverse client base, regardless of their financial expertise.
- **Scalability**: The solution should be scalable – capable of handling an increasing number of documents and user queries.

---

## Task 1: Financial Data Extraction from Form 10-k for Apple, microsoft and Tesla

### Overview of 10-K Reports
10-K reports are comprehensive annual filings submitted to the SEC by publicly traded companies. These reports contain in-depth information about a company’s financial performance, including audited financial statements, management's discussion and analysis (MD&A), and disclosures regarding market risk, controls, and legal proceedings.

### Key Sections for Financial Data Extraction:
- **Income Statement**: 
  - Provides details on the company's revenue, costs, and expenses over a specific period.
  - **Key Data Points**: Total revenue, cost of goods sold (COGS), operating expenses, and net income.
  - **Extraction Technique**: Look for the income statement summary, typically found in the early pages of the report. Pay close attention to year-over-year changes.

- **Balance Sheet**: 
  - Outlines the company’s assets, liabilities, and shareholders' equity at a particular point in time.
  - **Key Data Points**: Current assets, long-term assets, current liabilities, long-term liabilities, total shareholders' equity.
  - **Extraction Technique**: Focus on the balance sheet summary. Compare assets with liabilities to gauge the company’s financial health, and track significant changes.

- **Cash Flow Statement**: 
  - Shows how changes to the balance sheet and income affect cash and cash equivalents.
  - **Key Data Points**: Cash from operating activities, investing activities, and financing activities.
  - **Extraction Technique**: Analyze the cash flow statement to assess how the company generates and spends its cash, which provides insights into its liquidity.

### Effective Techniques for Data Extraction:
- **Manual Extraction**: Review the reports manually to understand the layout and identify where key financial information is located.
- **Highlight and Annotate**: Use digital tools to highlight key figures and annotate them for easy reference.
- **Excel and Spreadsheet Tools**: Input key financial figures into spreadsheets for comparative analysis.
- **Automated Extraction Tools**: For more advanced users, Python libraries like **BeautifulSoup** and **Pandas** can be employed to automate data extraction, especially for reports available in digital formats.

---

## Task 2: Financial Chatbot

### Project Description
This Financial Chatbot is designed to assist users with queries related to financial metrics of companies for specific years. The chatbot enables users to ask questions regarding various financial metrics, such as total revenue, net income, growth rates, and more. It retrieves data from an Excel file containing historical financial data and answers the user's query accordingly.

### How It Works
1. **User Input**: The user enters a question in the text box at the bottom of the page. The query should mention a company name, a specific financial metric, and the year.
   
2. **Query Parsing**: The chatbot extracts:
   - **Company Name**: Identifies the company from the user's query.
   - **Year**: Detects the year in four-digit format (e.g., 2023).
   - **Metric**: Matches the query with predefined financial metrics (e.g., total revenue, net income).

3. **Response Generation**: Based on the identified company, year, and metric, the chatbot:
   - Retrieves the exact value for the metric from the dataset.
   - Calculates and returns the change in the metric compared to the previous year.

4. **Conversation History**: All questions and answers are stored in the session state and displayed in a chat-like format, alternating user and bot messages.

### Predefined Queries
The chatbot can respond to the following types of queries:
- **Direct Metric Queries**: Users can ask for a specific metric for a company in a given year. Examples:
  - "What is the total revenue for Microsoft in 2023?"
  - "What was the net income for Tesla in 2022?"
  
- **Change in Metric Queries**: Users can ask how a financial metric has changed from one year to another. Examples:
  - "How has revenue changed for Microsoft?"
  - "What is the net income growth for Tesla?"
  - "How has cash flow changed for Apple?"

### Supported Metrics:
- Total Revenue
- Net Income
- Total Assets
- Total Liabilities
- Cash Flow
- Revenue Growth
- Net Income Growth
- Assets Growth
- Liabilities Growth
- Cash Flow Growth

### Limitations
- **Data Availability**: The chatbot relies on an Excel file containing financial data. If data for the queried company or year is missing, the chatbot will respond with "Sorry, no data available."
- **Query Structure**: The chatbot requires queries to explicitly mention the company name and year. For example, "What is the total revenue for Microsoft in 2023?" will work, but "What is the revenue?" will not.
- **Data Precision**: The data returned is only as accurate as the underlying Excel file. If the data is outdated or incomplete, the chatbot will not be able to answer accordingly.
- **No Complex Calculations**: The chatbot handles basic operations based on the dataset (e.g., retrieving values, year-over-year changes) but cannot perform advanced financial analyses or predictions.

---

## Conclusion

The **Financial Chatbot** provides an intuitive way to interact with financial data, answering user queries related to corporate performance metrics and historical data. It is designed to offer quick, reliable insights but is limited by the available data and the structure of the user's queries.

---

![image](https://github.com/user-attachments/assets/135562bd-faa5-49c9-96e4-f9163cc03369)

## Link to chatbot: 
https://bcg-fin-chatbot.streamlit.app/

