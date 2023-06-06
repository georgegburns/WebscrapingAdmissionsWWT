import os

import pandas as pd
from WWTAdmissionsScraper import NTScraper, WWTScraper

DESKTOP = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
# File must be closed and located on user desktop
FILENAME = 'Admission Prices - 2023-06-05.xlsx'
DF = pd.read_excel(DESKTOP + "/" + FILENAME)

# Sites with spaces must be connected as this is used in the URL query string, adding will capture but only if the url works
"""

    WWT Sites don't require a comparison site.
    All other sites require to be written in the following format: 'Name of Competitor Site'  :  'Name of WWT Site to Compare With'
    This creates a list of dictionaries. 

"""
WWT_SITES = ['Slimbridge', 'London', 'Martin-Mere', 'Welney', 'Arundel', 'Llanelli', 'Castle-Espie', 'Washington', 'Caerlaverock']
NT_SITES = {'Dinefwr':'Llanelli', 'Castle-Ward':'Castle Espie', 'Mount-Stewart':'Castle Espie', 'Rufford-Old-Hall':'Martin Mere', 'Tyntesfield':'Slimbridge', 'Gibside':'Washington', 'Souter-Lighthouse':'Washington', 'Washington-Old-Hall':'Washington', 'Wicken-Fen':'Welney'}

#Each scraper can be run independently, comment out with a #
"""

    ADMISSIONS

"""
"""
 
    Each scraper takes two variables, a list of sites to be used in the website URL as well as a pre-existing DF to add to. 
    The pre-existing DF will default to empty if not provided, allowing for extracts of a group of sites at a time alone. 
    Otherwise the data will be append to the pre-existing DF and duplicates removed, then saved on the desktop with today's date.
    
"""
WWTScraper(WWT_SITES)
NTScraper(NT_SITES, DF)