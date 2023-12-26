"""Placeholder"""
# Standard Library Imports
from time import sleep

# 3rd Party Imports
from bs4 import BeautifulSoup
import requests

# Globals
PENETRATION_DEPTH = 1 # Levels of links to go down
MIN_DELAY = 30 # seconds
MAX_DELAY = 80 # seconds

def main(root_site:str):
    session = get_session_with_header()

    # Need to be careful with verify=False
    raw_request = session.get(root_site,verify=False)
    try:
        test_status_ok(raw_request.status_code)
    except AssertionError:
        pass # Do something if status is not ok

    for depth in range(PENETRATION_DEPTH):
        # Get the list of links

        # Iterate through the links. 

        # To be continued
        pass


def get_session_with_header()->requests.Session:
    """Returns a session object with a predefined
    user agent header. In the future authentication can
    be added as well.
    """
    session = requests.Session()
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"}
    session.headers.update(headers)
    return session

def get_all_links_from_page(page_text:str)->list:
    """Returns all the <a> tag links from a single webpage
    as a list of links
    """

def get_page_text(raw_request:requests.models.Response):
    """placeholder"""
    soup = BeautifulSoup(raw_request.text)

    # Get text or P tags or all?
    return

def write_text_to_file():
    # One big text or lines of text?
    pass

def get_single_page():
    """placeholder"""
    return

def test_status_ok(request_status:int):
    """Test to make sure a status code of 200
    was returned with the get request (request was ok
    with no error)

    Future scope: do something with the error

    Returns nothing - just a test
    """
    try:
        assert request_status==200
    except AssertionError:
        pass

if __name__ == "main":
    main()