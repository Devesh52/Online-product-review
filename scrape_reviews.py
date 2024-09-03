import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_amazon_reviews(product_url, num_pages=20):
    reviews = []
    try :
        for page in range(1, num_pages + 1):
            url = f"{product_url}" #/ref=cm_cr_arp_d_paging_btm_next_{page}?pageNumber={page}"
            headers = {"User-Agent": "Your User-Agent Here"}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')

        for review in soup.find_all('div', class_='a-section review aok-relative'):
            rating = review.find('i', class_='review-rating').text.strip()
            title = review.find('a', class_='review-title').text.strip()
            content = review.find('span', class_='review-text').text.strip()
            date = review.find('span', class_='review-date').text.strip()
            reviews.append([rating, title, content, date])
    
        return reviews
    except:
        print("url not valid\n")
        exit(1)
    

def save_reviews_to_csv(reviews, filename):
    df = pd.DataFrame(reviews, columns=['Rating', 'Title', 'Content', 'Date'])
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    product_url = "https://www.amazon.in/product-reviews/9352685482/ref=acr_dp_hist_3?ie=UTF8&filterByStar=three_star&reviewerType=all_reviews#reviews-filter-bar"  # Example product
    reviews = scrape_amazon_reviews(product_url)
    save_reviews_to_csv(reviews, 'amazon_reviews.csv')
