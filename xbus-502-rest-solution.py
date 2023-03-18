#!/usr/bin/env python
"""
Template answer for REST Workshop
"""
##########################################################################
## Imports
##########################################################################

import os
import json
import requests


##########################################################################
## Module Variables/Constants
##########################################################################

DOJ_RELEASES_URL = "http://www.justice.gov/api/v1/press_releases.json?pagesize=5&direction=DESC&sort=date"


##########################################################################
## Functions
##########################################################################

def fetch_press_releases():
    """
    Performs a GET on the DOJ web service and return the array found in the
    'results' attribute of the JSON response
    """
    # execute a GET request and store the results
    r = requests.get(DOJ_RELEASES_URL) 
    # decode as json and store the results
    data = r.json()
    # return the 'results' array of press releases
    results = data['results']
    return(results)


def main():
    """
    Main execution function to perform required actions
    """
    # fetch array of press releases
    press_releases = fetch_press_releases()
    # iterate press releases
    for release in press_releases:
        print(release['title'])
        # save content to a new file in the releases sub-directory
        fname = release['title'] + '.json'
        with open(fname, 'w') as outfile:
            json.dump(release, outfile)
        

if __name__ == '__main__':
    main()

