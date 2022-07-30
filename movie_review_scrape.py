import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random as rd

urls = ['https://www.rottentomatoes.com/browse/movies_at_home/sort:popular?page=5',
        'https://www.rottentomatoes.com/browse/movies_at_home/sort:newest?page=5',
        'https://www.rottentomatoes.com/browse/movies_at_home/sort:critic_highest?page=5',
        'https://www.rottentomatoes.com/browse/movies_at_home/sort:critic_lowest?page=5',
        'https://www.rottentomatoes.com/browse/movies_at_home/sort:audience_highest?page=5',
        'https://www.rottentomatoes.com/browse/movies_in_theaters/sort:popular?page=5',
        'https://www.rottentomatoes.com/browse/movies_in_theaters/sort:newest?page=5',
        'https://www.rottentomatoes.com/browse/movies_in_theaters/sort:critic_highest?page=5',
        'https://www.rottentomatoes.com/browse/movies_in_theaters/sort:critic_lowest?page=5',
        'https://www.rottentomatoes.com/browse/movies_in_theaters/sort:audience_highest?page=5']



def movie_scrape(url):
    
    df= pd.DataFrame(columns=['Title','Rating','ReviewText'])
    
    rand_time1 = rd.randint(2, 6)
    rand_time2 = rd.randint(2, 6)
    rand_time3 = rd.randint(2, 6)
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    time.sleep(rand_time1)

    postbox = soup.find_all('div', class_ = 'discovery-tiles__wrap')
    postings = postbox[1].find_all('a')

    for post in postings:
        try:
            link = 'http://rottentomatoes.com' + post.get('href')
            info_page = requests.get(link)
            soup = BeautifulSoup(info_page.text, 'lxml')
            time.sleep(rand_time2)
            
            link = 'http://rottentomatoes.com' + soup.find('div', class_ = 'mop-audience-reviews__view-all clearfix').find('a').get('href')
            info_page = requests.get(link)
            soup = BeautifulSoup(info_page.text, 'lxml')
            time.sleep(rand_time3)
            
            #Get movie title
            title = soup.find('div', class_= 'center').find('a', class_= 'unstyled articleLink').text.split('\n')[1].strip()
                
                
            all_reviews = soup.find('div', class_ = 'js-reviews-container reviews-movie').find_all('li', class_ = 'audience-reviews__item')
            all_stars = soup.find_all('span', class_ = 'star-display')
            
            for i in range(10):
                
                #Get rating from stars
                star_info = str(all_stars[i]).split('<')
                
                rating = 0
                for star in star_info:
                    if 'filled' in star:
                        rating += 1
                    elif 'half' in star:
                        rating += 0.5
    
                #Get text review
                reviewtext = all_reviews[i].text.split('\n\n\n')[3].split('\n')[3]
            
            
                new_row = pd.DataFrame([[title,rating,reviewtext]],
                                  columns=['Title','Rating','ReviewText'])
            
                #Generate row in dataframe based on scraped information
                df = pd.concat([df,new_row])
                       
        except:
            pass
    
    return df

main_df = pd.DataFrame(columns=['Title','Rating','ReviewText'])
for i,url in enumerate(urls):
    print('Iteration: ', i+1)
    df = movie_scrape(url)
    main_df = pd.concat([main_df,df])

file = 'C:/Users/leave/OneDrive/Documents/Scraped_Datasets/Movie_Review_Data/movie_reviews.csv'
main_df.drop_duplicates(inplace=True)
main_df.dropna(inplace=True)
main_df.to_csv(file, index= False)
