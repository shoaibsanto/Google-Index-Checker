import csv
import requests
from bs4 import BeautifulSoup as bs
import time
import streamlit as st
import pandas as pd

# Function to check index status of a domain
def check_index_status(url):
    base = f'https://www.google.com/search?q=site%3A{url}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }

    # Create a session and make a request
    s = requests.session()
    r = s.get(base, headers=headers)

    # Parse the page content
    soup = bs(r.content, 'html.parser')

    # Try to find the element with id='result-stats'
    result_stats = soup.find('div', attrs={'id': 'result-stats'})

    if result_stats:
        # Extract the number of results from the text if available
        result_text = result_stats.text.strip().split(' ')[1]
        result = int(result_text.replace(',', ''))  # Remove commas and convert to an integer

        return result > 0
    else:
        return False

# Streamlit app setup
st.title("Google Index Checker")

# File uploader to upload the text file containing URLs
uploaded_file = st.file_uploader("Choose a file", type="txt")

# If the file is uploaded
if uploaded_file is not None:
    # Decode the uploaded file to get the URLs as a list of strings
    content = uploaded_file.getvalue().decode("utf-8")
    domains_to_check = [line.strip() for line in content.splitlines()]

    # Create a dataframe to store the results
    results = []
    
    # Progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()

    # Prepare CSV file to save results
    output_file = "index_status.csv"
    
    # Iterate over the domains and check their indexing status
    for i, domain in enumerate(domains_to_check):
        found = check_index_status(domain)

        # Display the result
        index_status = "Indexed" if found else "Not Indexed"
        results.append({"urls": domain, "index_status": index_status})

        # Update progress bar and status
        progress_bar.progress((i + 1) / len(domains_to_check))
        status_text.text(f"Checking: {domain} - {index_status}")
        
        # Add a delay between requests
        time.sleep(2)

    # Create a dataframe from the results
    df = pd.DataFrame(results)

    # Display the dataframe
    st.write("Results:", df)

    # Convert dataframe to CSV
    csv = df.to_csv(index=False).encode('utf-8')

    # Download button for the CSV file
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name=output_file,
        mime='text/csv',
    )
