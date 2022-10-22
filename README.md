# NCDHHS-Fee-Schedule-Scraping
This script uses BeautifulSoup to scrape the Fee Schedules from the NCDHHS website to then store in a database.

First, install Python onto your laptop and use PIP command to install BeautifulSoup4.

There are 5 steps to the script:
Part 1: Pull all the Fee Schedule Program links from the DHB website (done)
Part 2: For each program, pull the Excel or PDF link to the fee schedule (done)
Part 3: We now have a full set of PDF Program Fee Schedules. The next step is to scrape the data from each PDF (in progress)
Part 4: Once the data is scraped from each PDF, the data must be cleaned and formatted (not done)
Part 5: Load fee schedules into PostgreSQL Database (not done)
