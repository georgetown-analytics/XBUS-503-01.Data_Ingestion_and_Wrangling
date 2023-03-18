#!/usr/bin/env python
"""
Template for RSS exercise
"""
##########################################################################
## Imports
##########################################################################

import os
import re
from pprint import pprint 

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

    In short, this function converts text into a form safe to use as a 
    filename.
    """
    value = value.encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '-', value)


def save_article(title, content):
    """
    Save HTML content using a slugged version of the title as the basis for
    the filename
    """
    pass


def main():
    """
    Main execution
    """
    # grab RSS data and parse it
    pass
    
    # use pprint (pretty print) to print the formatted version of a variable
    # if you would like to better understand what it contains
    # pprint(SOME_PYTHON_VARIABLE)

    # loop through each article/RSS item
    for entry in entries:

        # fetch the article using its url and include the header dictionary shown here:
        # requests.get(URL_HERE, headers={"user-agent":"curl/7.86.0"})
        pass

        # save to disk or print an error message
        # hint: save_article(content)
        pass


##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()