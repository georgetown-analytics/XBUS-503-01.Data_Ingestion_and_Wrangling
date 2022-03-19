#!/usr/bin/env python
"""
Model answer for REST Workshop

NOTE: In order to use this program, be sure to create a sub-directory
called 'releases'
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

DOJ_RELEASES_URL = 'http://www.justice.gov/api/v1/press_releases.json?pagesize=5'


##########################################################################
## Functions
##########################################################################

def fetch_press_releases():
    """
    Performs a GET on the DOJ web service and return the array found in the
    'results' attribute of the JSON response
    """
    # execute a GET request and store the results
    response = requests.get(DOJ_RELEASES_URL)

    # decode as json and store the results
    data = response.json()

    # return the 'results' array of press releases
    return data['results']


def main():
    """
    Main execution function to perform required actions
    """
    # fetch array of press releases
    press_releases = fetch_press_releases()

    # iterate press releases
    for release in press_releases:

        # NOTE: be sure the releases subdirectory exists
        path = './releases/{}.json'.format(release['uuid'])
        content = json.dumps(release)

        with open(path, 'w') as f:
            f.write(content)


##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    main()
