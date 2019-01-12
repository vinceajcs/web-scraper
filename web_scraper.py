from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('http://coreyms.com')
html_file = source.text
soup = BeautifulSoup(html_file, 'html5lib')

# create csv file
csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_url'])

# get headline, summary and video url of one article
# article = soup.find('article')
# print(article.prettify())
#
# headline = article.h2.a.text
# print(headline)
#
# summary = article.find('div', class_='entry-content').p.text
# print(summary)

# parse html to get video url
# video_source = article.find('iframe', class_='youtube-player')['src']
# print(video_source)
# video_id = video_source.split('/')[4]
# video_id = video_id.split('?')[0]
# print(video_id)
#
# youtube_link = 'https://youtube.com/watch?v={}'.format(video_id)
# print(youtube_link)

# get headline, summary, and video url of all articles
articles = soup.find_all('article')

for article in articles:
    headline = article.h2.a.text
    summary = article.find('div', class_='entry-content').p.text

    try:
        video_source = article.find('iframe', class_='youtube-player')['src']
        video_id = video_source.split('/')[4].split('?')[0]
        youtube_url = 'http://youtube.com/watch?v={}'.format(video_id)
    except Exception as e:
        youtube_url = None

    print(headline)
    print(summary)
    print(youtube_url)
    print()

    # write data to csv file
    csv_writer.writerow([headline, summary, youtube_url])

csv_file.close()

