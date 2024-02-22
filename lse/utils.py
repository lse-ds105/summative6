import requests

import numpy as np
import pandas as pd

from scrapy import Selector

def print_designated_lse_department(candidate_number):
    """
    Get the designated department for a candidate number
    """
    # Get the page that contains the list of departments and institutes at LSE
    base_url = 'https://info.lse.ac.uk/Staff/Departments-and-Institutes'
    response = requests.get(base_url)

    # Extract the department names from the response
    sel = Selector(text=response.text)
    lse_departments = sel.xpath('//div[@class="pageContent pageContent--std"]//a/text()').extract()
    depts_url = sel.xpath('//div[@class="pageContent pageContent--std"]//a/@href').extract()

    # Dictionary to store the department names and their respective URLs
    depts_dict = dict(zip(lse_departments, depts_url))

    # Randomly, but deterministically, discover the department that you will be working in 
    np.random.seed(candidate_number)
    designated_depto = np.random.choice(lse_departments, 1)[0]

    print(f'Your designated department is: {designated_depto}')
    print(f'URL: {depts_dict[designated_depto]}')