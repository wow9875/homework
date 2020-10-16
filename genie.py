import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musics:
    rank = music.select_one('td.number').text[0:2].strip()
    artist = music.select_one('td.info > a.artist.ellipsis').text
    title = music.select_one('td.info > a.title.ellipsis').text.strip()
    musicchart = {
        'rank': rank,
        'artist': artist,
        'title': title
    }
    # print(rank, title, artist)
    # print(musicchart)
    db.musics.insert_one(musicchart)
