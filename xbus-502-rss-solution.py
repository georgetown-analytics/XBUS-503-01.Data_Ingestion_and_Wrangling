"""
Solutions for RSS exercise
"""
##########################################################################
## Imports
##########################################################################

import os
import re

import requests
import feedparser


##########################################################################
## Module Variables/Constants
##########################################################################

RSS_URL = 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'


##########################################################################
## Functions
##########################################################################

def slugify(value):
    """
    Converts to ASCII. Converts spaces to hyphens. Removes characters that
    aren't alphanumerics, underscores, or hyphens. Converts to lowercase.
    Also strips leading and trailing whitespace.

    Note: This is not production code
    """
    value = value.encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '-', value)


def save_article(title, content):
    """
    Save HTML content using a slugged version of the title as the basis for
    the filename
    YOU MUST CREATE THE DIRECTORY 'news' before running
    """
    filename = slugify(title)
    filename = title+".html"
    filename = filename.replace("?", "") #replaces question marks in titles as this may cause errors.
    with open("news/"+filename, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    """
    Main execution
    """
    # grab RSS data and parse it
    result = feedparser.parse(RSS_URL)
    entries = result.entries 

    # loop through each article/RSS item
    for entry in entries:

        # fetch article using url
        # hint: content = ???
        titlex = entry['title']
        link = entry['link']
        response = requests.get(link, headers={"user-agent":"curl/7.86.0"}) 
        contentx = response.text 
        print("Saving "+titlex+"...")
        # save to disk or print an error message
        # hint: save_article(content)
        save_article(titlex, contentx)
        


##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()