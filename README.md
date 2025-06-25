## Web Scraping with [BeautifulSoup and Requests](https://github.com/AqilaFadia/Data-Scraping/blob/main/bs4%26req/bs2.py)

This folder contains a simple web scraping project using **BeautifulSoup**, **requests**, and **urllib.parse**.
### 🔧 Libraries Used
- `requests` for sending HTTP requests
- `BeautifulSoup` from `bs4` for parsing HTML
- `pandas` for saving the data into a CSV file
- `urllib.parse.urljoin` to resolve relative URLs

- 📚 [Article Link](https://medium.com/ai-in-plain-english/i-just-learned-web-scraping-and-scraped-1000-books-from-a-website-d4f326832846)

## Web Scraping with [Scrapy](https://github.com/AqilaFadia/Data-Scraping/tree/main/bookscraper)
In this post, I'll guide you through a simple web scraping project using Scrapy, one of the most powerful frameworks for web scraping in Python. Scrapy is designed for large-scale web scraping tasks and is perfect for projects that need to extract data from multiple pages or websites efficiently.

**Why Choose Scrapy?**
- Built for Speed: Scrapy is fast and can handle large amounts of data with ease.

- Complete Framework: Scrapy provides everything you need for scraping, including built-in support for crawling, parsing, and storing scraped data.

- Highly Customizable: It’s easy to customize Scrapy to suit the needs of different websites.
- 📚 [Article Link](https://medium.com/@rakyatambis/scrapy-tutorial-for-beginners-step-by-step-guide-to-web-scraping-in-python-5b97633117a3)

**Getting Started**
First, you need to install Scrapy:

- `pip install scrapy` to resolve relative URLs

## Web Scraping with [Selenium](https://github.com/AqilaFadia/Data-Scraping/blob/main/main.ipynb)

This project demonstrates how to perform web scraping using **Selenium** in Python.  
The goal is to extract movie data (title, rating, and link) from IMDb categorized by genre, and save it into a structured CSV file.

**What You Need**
Before running the script, make sure you have the following installed:
- `pip install selenium pandas webdriver-manager` to resolve relative URLs
- You can download ChromeDriver manually based on your Chrome version here:
🔗 https://sites.google.com/chromium.org/driver/
- We scrape movie categories and film data from IMDb's genre interest page:
🔗 https://www.imdb.com/interest/all/?ref_=fn_asr_gnr
- 📚 [Article Link](https://medium.com/@rakyatambis/scrapy-tutorial-for-beginners-step-by-step-guide-to-web-scraping-in-python-5b97633117a3)

  ## Web Scraping with [Playwright](https://github.com/AqilaFadia/Data-Scraping/tree/main/twitch-scraper-playwright)

A simple portfolio project using **Playwright** to scrape live stream data from Twitch's "Just Chatting" category and store it in **Google Sheets** automatically every 15 minutes.

### 🚀 Features

- 🎥 Scrape live stream data from Twitch:
  - Stream title
  - Streamer username
  - Viewer count
- 📤 Save data to Google Sheets
- ⏱️ Automated scraping every 15 minutes
- 🔐 Secure configuration with `.env` and credentials
- 📚 [Article Link](https://medium.com/@rakyatambis/how-i-built-a-twitch-data-scraper-that-runs-every-15-minutes-with-python-playwright-7c80a5982d7e)







