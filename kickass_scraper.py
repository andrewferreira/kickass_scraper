
#this code can successfully scrape all torrent names, file sizes and magnets

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import webbrowser

print 'Welcome to the kickass torrent website web scraper!'
print ''
print ''

the_time = time.strftime("%H:%M:%S")
hour = the_time[:2]

if hour in ['00', '01', '02', '03', '04', '05']:
    query = raw_input('What would you like to torrent on this late night session?')
elif hour in ['06', '07', '08' ,'09', '10', '11']:
    query = raw_input('What would you like to torrent on this fine morning?')
elif hour in ['12', '13', '14', '15', '16']:
    query = raw_input('What would you like to torrent on this lazy afternoon?')
else:
    query= raw_input('what would you like to torrent on this eventful evening?')


print 'ok lets load up '+query
print ''

url = 'https://kickass.cd/search.php?q='+query.split()[0]

for i in query.split()[1:]:
    url+='+'
    url+=i



path = '/Users/davidferreira/Documents/kickass_torrent_scraper/chromedriver'
browser = webdriver.Chrome(path)

browser.get(url)

page = browser.page_source

soup = bs(page, 'lxml')

name_lst = soup.find_all('a', class_ = 'cellMainLink')
size = soup.find_all('td', class_ = 'nobr center')
date = soup.find_all('td', class_ = 'center')
seeds = soup.find_all('td', class_ = 'green center')
lees = soup.find_all('td', class_ = 'red lasttd center')

name = [str(i)+'. '+str(v.text.encode('utf-8')) for i,v in enumerate(name_lst)]

m_div = soup.find_all('div', class_ = 'iaconbox center floatright')
div_a = []

for i in m_div:
    div_a.append(i.find_all('a', class_ = 'icon16'))

m2 = [str(i[1]) for i in div_a]
magnet = []

for i in m2:
    mg = i.split('href="')[1]
    mgt = mg.split('"')[0]
    magnet.append(mgt)

print ""
browser.quit()

count = 0

for a,b,c,d,e in zip(name, size, date, seeds, lees):
    print a
    print 'size: '+b.text
    print 'date created: '+c.text
    print 'seeders: '+d.text
    print 'leechers: '+e.text
    print ''
    print ''


count2 = 0
while count2 <= 5:
    num = raw_input('type of the number of the file you wish to torrent here')

    utor_magnet = magnet[int(num)]

    webbrowser.open(utor_magnet)
    time.sleep(1)
    count+=1


