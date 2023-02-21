from bs4 import BeautifulSoup
import requests
import csv

# declare saving path
path = ""
prefix = 'https://'

# broswer's head info, pretending you're using broswer
headers = {
    'user-agent': ''
}

# target url
url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
# find book list
book_info = soup.find('ol', class_='row')
# find all book that listed
books = book_info.find_all('li')
# loop in book list
for book in books:
    book_name = book.h3.text
    print(book_name)
    book_price = book.find('p', class_='price_color').text
    book_status = book.find('p', class_='instock').text.strip()
    # book_link = book.find('div', class_='image_container').a['href']
    print(book_price)
    print(book_status)

    with open('book1.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['name', 'price', 'status'])
        for i in range(len(books)):
            csv_writer.writerow([book_name, book_price, book_status])
            print(f'writting {book_name}')
        f.close()
#     csv_writer.writerow([title, suffix+link])
# csv_file.close()
print('success')


