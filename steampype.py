from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

class steamCon:
    def __init__(self,sname):
        self.steamname=sname
        Steam= 'https://steamcommunity.com/search/users#text='+self.steamname
        soup=self.webGine(Steam)
        self.url=soup.find('a',attrs={'class':'searchPersonaName'}).get('href')
        #element= driver.find_element_by_class_name("searchPersonaName")
        imgerl= soup.find('div',attrs={'class':'avatarMedium'})
        self.imgurl= imgerl.find('img').get('src')


    def webGine(self,goto):
        chrome_options=Options()
        chrome_options.add_argument("--headless")
        driver=webdriver.Chrome(chrome_options=chrome_options)
        driver.get(goto)
        time.sleep(1)
        html= driver.page_source
        soup=BeautifulSoup(html,"html.parser")
        driver.close()
        return soup

    def friends(self):
        soup = self.webGine(self.url+"/friends/");
        friendlist=soup.findAll('div',attrs={'class':['selectable','friend_block_v2','persona','online']})
        i=0
        count=0
        for fren in friendlist:
            if(fren.get('data-search')is not None):
                count=count+1
        friends=[[0 for x in range(3)]for y in range(count)]
        for fren in friendlist:
            names=fren.get('data-search')
            if names is not None:
                friends[i][0]=names[0:-2]
                friends[i][1]=fren.find('img').get('src')
                friends[i][2]="Offline"
                i=i+1
            else:
                friends[i-1][2]="Online"
        return friends

    def games(self):
        soup = self.webGine(self.url+"/games/?tab=all");
        gamelist=soup.findAll('div',attrs={'class':'gameListRow'})
        i=0
        count=0
        for game in gamelist:
            count=count+1
        games=[[0 for x in range(3)]for y in range(count)]
        for gam in gamelist:
            games[i][0]=gam.find('div',attrs={'class':'gameListRowItemName'}).getText()
            games[i][1]=gam.find('img').get('src')
            try:
                games[i][2]=gam.find('h5',attrs={'class':'hours_played'}).getText()
            except:
                games[i][2]="No Hours Played"
            i=i+1
        return games

    def badges(self):
        soup = self.webGine(self.url+"/badges");
        badgelist=soup.findAll('div',attrs={'class':'badge_row'})
        i=0
        count=0
        for badg in badgelist:
            count=count+1
        badges=[[0 for x in range(3)]for y in range(count)]
        for badg in badgelist:
            badges[i][0]=badg.find('div',attrs={'class':'badge_info_title'}).getText()
            badges[i][1]=badg.find('img').get('src')
            badges[i][2]=badg.find(text=re.compile('XP')).strip()
            i=i+1
        return badges
