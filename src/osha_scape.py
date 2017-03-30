import requests
from bs4 import BeautifulSoup
from lxml import html
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

url = 'https://www.osha.gov/chemicaldata/'
r = requests.get(url)
soup = BeautifulSoup(r.text)
tree = html.fromstring(r.text)

chemical_links = []

for table_row in soup.select('.resultsTable tr'):
    table_cells = table_row.findAll('td')

    #if len(table_cells) > 0:
