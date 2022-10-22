# NCDHHS-Fee-Schedule-Scraping
This script uses BeautifulSoup to scrape all the Fee Schedules and their corresponding hyperlink from the NCDHHS website. 

First, install Python (https://www.python.org/downloads/). Then install BeautifulSoup4 (https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

The script works in 5 steps: 
  Part 1: Pull all the Fee Schedule Program links from the DHB website (done)
  Part 2: For each program, pull the PDF link to the fee schedule (done)
  Part 3: Once we have all PDF links, scrape the data from each PDF fee schedule (in progress)
  Part 4: Once the data is scraped from each PDF, clean and format the fee schedule data (not done)
  Part 5: Load structured fee schedules into PostgreSQL Database (not done)
