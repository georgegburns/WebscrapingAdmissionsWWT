import os
from datetime import date

import pandas as pd

# This is the location of the output - user's desktop folder
DESKTOP = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
COL_NAMES = ['Site', 'Date Captured', 'Company', 'Comparison', 'Ticket', 'With Gift Aid', 'Without Gift Aid']
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', 'Accept-Enconding' : 'grip, deflate', 'Accept' : '*/*', 'Connection' : 'keep-alive'}

def WWTScraper(sites : list, output = pd.DataFrame()):
    # loops through each site in the list
    WWT = pd.DataFrame()
    for site in sites:
        print(site)
        # adds the site name into the query string
        query = f'https://www.wwt.org.uk/wetland-centres/{site}/plan-your-visit/prices/'
        # produces a table of prices. If more tables are added to the website then will need to update the index, i.e. 0 = 1st table on the website when scrolling from top to bottom
        Centre = pd.read_html(query)[0]
        Centre['Site'] = site.strip('-')
        Centre ['Date Captured'] = date.today().strftime('%d-%m-%Y')
        Centre['Company'] = 'WWT'
        Centre['Comparison'] = site.strip('-')
        WWT = pd.concat([WWT, Centre], ignore_index=True)
        
    WWT = pd.concat([WWT, output],ignore_index=True).drop_duplicates()
    WWT.to_excel(DESKTOP + f'/Admission Prices - {date.today()}.xlsx', index=False)

def NTScraper(sites : list, output = pd.DataFrame()):
    # loops through each site in the list
    NT = pd.DataFrame()
    for site in sites.keys():
        print(site)
        # adds the site name into the query string
        query = f'https://www.nationaltrust.org.uk/{site}#Prices'
        # produces a table of prices. If more tables are added to the website then will need to update the index, i.e. 0 = 1st table on the website when scrolling from top to bottom
        # Dinefwr & Wicken Fen are special cases where the admission prices are located in the 3rd table, 2nd table has car park prices and 1st table has opening times.
        Centre = pd.read_html(query)[2]
        if site not in ['Dinefwr', 'Wicken-Fen']:
            Centre = pd.read_html(query)[1]
        Centre['Site'] = site.strip('-')
        Centre ['Date Captured'] = date.today().strftime('%d-%m-%Y')
        Centre['Company'] = 'National Trust'
        Centre['Comparison'] = sites[site]
        NT = pd.concat([NT, Centre], ignore_index=True)
    NT = NT[['Site', 'Date Captured', 'Company', 'Comparison', 'Ticket type', 'Gift aid', 'Standard']]
    NT.rename(columns={'Ticket type' : 'Ticket', 'Gift aid' : 'With Gift Aid', 'Standard' : 'Without Gift Aid'}, inplace=True)
    NT = pd.concat([NT, output],ignore_index=True).drop_duplicates()
    NT.to_excel(DESKTOP + f'/Admission Prices - {date.today()}.xlsx', index=False)