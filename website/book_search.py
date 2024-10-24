import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY') # gets google books api key from .env file

def get_book_search(query, api_key="AIzaSyAF7yCYmAZX9QVUlLqgXGOX0gBAArh8kws"):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=20&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        book_data = response.json()
        books = []
        for item in book_data.get('items', []):
            title = item['volumeInfo'].get('title', 'No title')
            authors = item['volumeInfo'].get('authors', ['No author'])
            genres = item['volumeInfo'].get('categories', ['No genre'])
            page_count = item['volumeInfo'].get('pageCount', 'N/A')
            published_date = item['volumeInfo'].get('publishedDate', 'No date')
            thumbnail = item['volumeInfo'].get('imageLinks', {}).get('thumbnail', 'No image')
            
            if published_date != 'No date' and len(published_date) >= 4:
                published_year = published_date[:4]  # slices to only get the year
            else:
                published_year = 'No year'

            books.append({
                'title': title,
                'authors': ', '.join(authors),
                'genres': ', '.join(genres),
                'page_count': page_count,
                'published_year': published_year,
                'thumbnail': thumbnail
            })
        return books
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []
    


# testing
#books = search_books('the way of kings')
#print(books)
#search_books('the hero of ages', api_key)


