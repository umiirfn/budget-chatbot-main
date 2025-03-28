import requests
from bs4 import BeautifulSoup

def get_aldi_lidl_prices(product_name):
    # Construct URLs for Aldi and Lidl product searches
    aldi_url = f"https://www.aldi.co.uk/search?text={product_name}"
    lidl_url = f"https://www.lidl.co.uk/en/search?query={product_name}"

    # Headers to mimic browser access (helps avoid bot blocks)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    # Send requests to both websites
    aldi_response = requests.get(aldi_url, headers=headers)
    lidl_response = requests.get(lidl_url, headers=headers)

    # Parse the page content
    aldi_soup = BeautifulSoup(aldi_response.text, "html.parser")
    lidl_soup = BeautifulSoup(lidl_response.text, "html.parser")

    # Extract product and price data
    aldi_prices = aldi_soup.find_all("span", class_="product-price")
    lidl_prices = lidl_soup.find_all("span", class_="product-price")

    aldi_price = None
    lidl_price = None

    if aldi_prices:
        aldi_price = aldi_prices[0].text.strip()
    if lidl_prices:
        lidl_price = lidl_prices[0].text.strip()

    return aldi_price, lidl_price
