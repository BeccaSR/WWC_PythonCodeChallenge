# Day 56 Challenge:
# Create a function to extract all URLs from a given text using regular expressions.

import re

def extract_urls(text):
    # Regular expression to match URLs
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'

    urls = re.findall(url_pattern, text)
    
    return urls

# Example:
text = "Here are some example URLs: News Websites: https://www.nytimes.com/,https://www.bbc.com/news,https://edition.cnn.com/,https://www.theguardian.com/international, https://www.example.com, http://another-example.com"
urls = extract_urls(text)
print(urls)