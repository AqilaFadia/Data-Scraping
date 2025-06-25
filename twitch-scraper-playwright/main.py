from scraper.twitch_scraper import scrape_twitch_data
from utils.save_to_sheet import save_data_to_sheet


def main():
    print("Scraping data from Twitch...")
    data = scrape_twitch_data()
    print(f"The amount of data taken: {len(data)}")
    
    
    print("Save to google sheets...")
    save_data_to_sheet(data)
    print("Done..")
    
if __name__ == "__main__":
    main()
