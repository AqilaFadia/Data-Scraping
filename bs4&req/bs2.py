# Import Library
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

baseurl = "https://books.toscrape.com/"

# Used User Agent Browser /// Link >> https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbXF2UF9WRVRRUEZHYjZER2Q3eG1VYkg3dEFpQXxBQ3Jtc0tueXVSV0MyU0R3S1FRNVZOQWlNWEd5SDRrNzRjZHI5Sjh4NXozbVBCZndmLUhlTWVNeXJmUzZ3QnlTZnVPeVdSdVVQVGM2Qm5SUzM3QkRNQUZOdHU5aUh5b2V3cnR6dzJva1VIdlFUaEc1SkF0QzRwVQ&q=https%3A%2F%2Fdevelopers.whatismybrowser.com%2Fuseragents%2Fexplore%2Fsoftware_type_specific%2Fweb-browser%2F&v=nCuPv3tf2Hg
headers = {
    'User-Agent': 'Mozilla/5.0'    
}  

productlinks = []

# Scrape from the first page to the last
for x in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{x}.html"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    
    productlist = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    for item in productlist:
        link = item.find('a', href=True)['href']
        full_link = urljoin(url, link)  
        productlinks.append(full_link)

# Get details of each book
booklist = []
for link in productlinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    try: # Erorr Handling
        name = soup.find('h1').text.strip()                                 # to scrape detail name Book
        price = soup.find('p', class_='price_color').text.strip()           # to scrape detail Price Book
        stock = soup.find('p', class_='instock availability').text.strip()  # to scrape detail Stock Book
        
        # for table detail Scrape
        table = soup.find('table', class_='table table-striped')
        rows = table.find_all('tr')

        product_info = {}
        for row in rows:
            header = row.find('th').text.strip()
            value = row.find('td').text.strip()
            product_info[header] = value
    
        upc = product_info.get('UPC')                           # to scrape Upc detail product
        product_type = product_info.get('Product Type')         # to scrape  product type
        price_excl_tax = product_info.get('Price(excl. tax)')   # to scrape price exclude tax
        price_incl_tax = product_info.get('Price (incl. tax)')  # to scrape price include tax
        tax = product_info.get('Tax')                           # to scrape tax info
        Number_reviews = product_info.get('Number of reviews')  # to scrape Number of reviews

        # Save the dictionary to the booklist.
        book = {
            'name': name,
            'price': price,
            'stock': stock,
            'UPC': upc,
            'Product Type': product_type,
            'Price excl. tax': price_excl_tax,
            'Price incl. tax': price_incl_tax,
            'Tax': tax,
            'Number Reviews': Number_reviews
        }
        booklist.append(book)
        print('Saving:', name)

    except Exception as e:
        print("Gagal parsing:", link)

# Show 10 data
df = pd.DataFrame(booklist)
print(df.head(10))

# Save to CSV
df.to_csv('books_scraped.csv', index=False, encoding='utf-8-sig')
print("Data berhasil disimpan ke books_scraped.csv")
