from requests import get
from bs4 import BeautifulSoup

#url = "https://www.imdb.com/title/tt0203259/episodes?season=1"
#response = get(url)
#soup = BeautifulSoup(response.text, 'html.parser')

titles = []
release_date = []
rating = []
num_reviews = []
episode_num = []

# At the time of data extraction (March 16, 2021), the last episode released was S22, Ep8
seasons = list(range(1, 23))

for season in seasons:
    url = "https://www.imdb.com/title/tt0203259/episodes?season=" + str(season)
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    odd_ep = soup.find_all('div', class_='list_item odd')
    even_ep = soup.find_all('div', class_='list_item even')
# Odd episodes
    for i in range(len(odd_ep)):
    # title
        title = odd_ep[i].strong.text
        titles.append(title)
    # episode number
        episode = odd_ep[i].div.text.strip()
        episode_num.append(episode)
    # release date
        release = odd_ep[i].find("div", class_="airdate").text.strip()
        release_date.append(release)
    # rating
        rate = odd_ep[i].find("span", class_="ipl-rating-star__rating").text
        rating.append(rate)
    # number of reviews
        reviews = odd_ep[i].find("span", class_="ipl-rating-star__total-votes").text
        num_reviews.append(reviews)
# Even episodes
    for i in range(len(even_ep)):
    # title
        title = even_ep[i].strong.text
        titles.append(title)
    # episode number
        episode = even_ep[i].div.text.strip()
        episode_num.append(episode)
    # release date
        release = even_ep[i].find("div", class_="airdate").text.strip()
        release_date.append(release)
    # rating
        rate = even_ep[i].find("span", class_="ipl-rating-star__rating").text
        rating.append(rate)
    # number of reviews
        reviews = even_ep[i].find("span", class_="ipl-rating-star__total-votes").text
        num_reviews.append(reviews)

    sleep(1)

import pandas as pd
SVU = pd.DataFrame(list(zip(episode_num, titles, release_date, rating, num_reviews)), 
columns = ['episode', 'title', 'release_date', 'rating', 'number_reviews'])

SVU.to_csv("/Users/rachelforbes/Desktop/SVU/SVU_imbd.csv", index=False)