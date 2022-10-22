from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

"""
Part 1: Pull all the Fee Schedule Program links from the DHB website
"""

req = Request("https://medicaid.ncdhhs.gov/providers/fee-schedules")
html_page = urlopen(req)

fee_schedule_main_page = BeautifulSoup(html_page, "html.parser")

# Pull all hyperlinks from the main DHB website
all_links_on_fee_schedule_website = []
for link in fee_schedule_main_page.findAll('a'):
    all_links_on_fee_schedule_website.append(link.get('href'))

# By the end of the for loop, we have a concise list of all Program Fee Schedule hyperlinks
fee_schedule_links = all_links_on_fee_schedule_website[32:81]
for i in range(len(fee_schedule_links)):
    if "https://" not in fee_schedule_links[i]:
        fee_schedule_links[i] = "https://medicaid.ncdhhs.gov" + fee_schedule_links[i]

"""
Part 2: For each program, pull the Excel or PDF link to the fee schedule
"""

def all_links_from_link(link, fee_schedule_pdf_links):
    # this function allows us to pull the first Excel or PDF link from each Program Fee Schedule webpage
    req = Request(link)
    html_page = urlopen(req)
    program_fee_schedule_page = BeautifulSoup(html_page, "html.parser")

    # pull all initial links from the main fee schedule page
    all_links_on_webpage = []
    for hyperlink in program_fee_schedule_page.findAll('a'):
        all_links_on_webpage.append(hyperlink.get('href'))

    # find the hyperlink with the pdf link
    pdf_found = False
    for hyperlink in all_links_on_webpage:
        if isinstance(hyperlink, str):
            if "pdf" in hyperlink:
                fee_schedule_pdf_links.append(hyperlink)
                pdf_found = True
                break

    # if there isn't an explicit pdf link, find it by pulling the second link with fee-schedules/ in the hyperlink
    if not pdf_found:
        # print(link) - use this print statement to check which programs don't have a PDF version of their fee schedule
        for i in range(len(all_links_on_webpage)):
            if isinstance(all_links_on_webpage[i], str):
                if "fee-schedules/" in all_links_on_webpage[i]:
                    fee_schedule_pdf_links.append(all_links_on_webpage[i + 1])
                    break

# this calls the function above to pull the raw link to the PDF version for each Program Fee Schedule
fee_schedule_pdf_links = []
for link in fee_schedule_links:
    all_links_from_link(link, fee_schedule_pdf_links)

# we add the full hyperlink if it is missing the initial https://... component
for i in range(len(fee_schedule_pdf_links)):
    if "https://" not in fee_schedule_pdf_links[i]:
        fee_schedule_pdf_links[i] = "https://medicaid.ncdhhs.gov" + fee_schedule_pdf_links[i]
        print(fee_schedule_pdf_links[i])

"""
Part 3: We now have a full set of PDF Program Fee Schedules. The next step is to scrape the data from each PDF
Part 4: Once the data is scraped from each PDF, the data must be cleaned and formatted prior to be loading into a database
"""
