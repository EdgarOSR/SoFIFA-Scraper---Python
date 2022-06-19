from datetime import datetime
import requests
import json
from bs4 import BeautifulSoup
from regex import custom_regex as re

class sofifa:
    def __init__(self):
        self.url = 'https://sofifa.com/'

    def __parse_list(self, list):
        tmpName = []
        tmpId = []
        for item in list:
            tmpName.append(item[len(item)-2])
            tmpId.append(item[len(item)-1])
        return tmpName, tmpId

    def __parse_page(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
        response = requests.get(self.url, headers=headers)
        response = response.content.decode('utf8','ignore')
        self.soup = BeautifulSoup(re.remove_diacritics(response), 'html.parser')

    def get_games(self):
        self.__parse_page()
        tmpId = []
        tmpName = []
        rows = self.soup.select('h2 div.dropdown:nth-child(1) div a')
        for row in rows:
            tmpId.append(re.get_only_numbers(row.get('href')))
            tmpName.append(row.text.strip())
        return tmpName, tmpId

    def get_versions(self, gameId):
        self.url = f'https://sofifa.com/?r={gameId}&set=true'
        self.__parse_page()
        tmpId = []
        tmpName = []
        rows = self.soup.select('h2 div.dropdown:nth-child(2) div a')
        for row in rows:
            tmpId.append(re.get_only_numbers(row.get('href')))
            tmpName.append(row.text.strip())
        return tmpName, tmpId

    def get_clubs(self, country, ver):
        self.url = f'https://sofifa.com/teams?type=all&na%5B%5D={country}&r={ver}&set=true&col=oa&sort=desc'
        self.__parse_page()
        tmpList = []
        tmpId = 0
        tmpName = 'All by country'
        tmpOvr = 0
        rows = self.soup.select('table tbody tr')
        for row in rows:
            children = row.find_all('td')
            tmpName = children[1].find_all('a')[0].text.strip()
            tmpId = re.get_only_numbers(children[1].find_all('a')[0].get('href'))
            tmpOvr = int(children[2].text)
            tmpList.append((tmpOvr, tmpName, tmpId))
        tmpList.insert(0,(99, 'By Nation', 0))
        return self.__parse_list(tmpList)

    def get_players(self, typeSel, nation, club, min, max, ver, player_name):
        if (len(player_name) > 0):
            self.url = f'https://sofifa.com/players/?keyword={player_name}&type={typeSel}&oal={min}&oah={max}&col=oa&sort=desc&r={ver}&set=true'
        elif (int(club) > 0):
            self.url = f'https://sofifa.com/team/{club}/?col=oa&sort=desc&r={ver}&set=true'
        elif (int(nation) > 0):
            self.url = f'https://sofifa.com/players/?type={typeSel}&na%5B%5D={nation}&oal={min}&oah={max}&col=oa&sort=desc&r={ver}&set=true'
        else:
            self.url = f'https://sofifa.com/players/?type={typeSel}&oal={min}&oah={max}&col=oa&sort=desc&r={ver}&set=true'
        self.__parse_page()
        tmpList = []
        tmpId = 0
        tmpOvr = 0
        tmpName = 'null'
        tmpClub = 'null'
        tmpPos = 'null'     
        pagination = True
        while pagination != None:
            if(club > 0):
                rows = self.soup.select('div.col.col-12 div.card:nth-child(2) table tbody tr')
            else:
                rows = self.soup.select('table tbody tr')    
            for row in rows:
                children = row.find_all('td')
                tmpId = re.get_only_numbers(children[1].find_all('a')[0].get('href'))
                tmpOvr = int(children[3].text)
                # tmpNation = children[1].find_all('a')[0].get('aria-label').title()
                tmpNation = children[1].find('img').get('title')
                tmpName = children[1].find_all('a')[0].text.strip()
                tmpPos = children[1].find_all('a')[1].text.strip().upper()
                if(club > 0):
                    tmpClub = int(re.get_only_numbers(children[5].find('div').contents[1].text))
                else:
                    tmpClub = children[5].find('a').text.strip()
                tmpList.append((tmpOvr, tmpName, tmpClub, tmpPos, tmpNation, tmpId))
            pagination = self.soup.select_one('div.pagination span.bp3-icon-chevron-right')
            if(pagination != None):
                self.url = 'https://sofifa.com' + str(pagination.parent.get('href'))
                self.__parse_page()
        return tmpList

    def get_countries(self):
        tmpName = ('Any','Austria','Belgium','Croatia','Czech Republic','Denmark','England','France','Germany','Greece','Hungary','Italy','Netherlands','Norway','Poland','Portugal','Romania','Russia','Scotland','Spain','Sweden','Switzerland','Turkey','Ukraine','Argentina','Bolivia','Brazil','Chile','Colombia','Ecuador','Paraguay','Peru','Uruguay','Venezuela','Canada','Mexico','United States','China PR','Japan','Saudi Arabia','Australia','Albania','Armenia','Belarus','Bosnia','Bulgaria','Cyprus','Finland','Georgia','Kosovo','Latvia','Montenegro','North Macedonia','Iceland','Ireland','Northern Ireland','Slovakia','Slovenia','Wales','Serbia','Suriname','Costa Rica','Honduras','Jamaica','Panama','Algeria','Angola','Burkina Faso','Cameroon','Congo','Congo DR','Gabon','Ivory Coast','Egypt','Ghana','Mali','Morocco','Nigeria','Senegal','Togo','Tunisia','Zambia','Zimbabwe','Iran','Israel','Korea Republic','Qatar','United Arab Emirates','Uzbekistan','New Zealand','Monaco')
        tmpId = (0,4,7,10,12,13,14,18,21,22,23,27,34,36,37,38,39,40,42,45,46,47,48,49,52,53,54,55,56,57,58,59,60,61,70,83,95,155,163,183,195,1,3,6,8,9,11,17,20,219,28,15,19,24,25,35,43,44,50,51,92,72,81,82,87,97,98,101,103,107,110,115,108,111,117,126,129,133,136,144,145,147,148,161,26,167,182,190,191,198,1037)
        return tmpName, tmpId

    def __get_player_skills(self, season):
        skills = {}
        ignore = []
        if int(season) < 2019:
            ignore = ['Volleys','Curve','Agility','Balance','Jumping','Interceptions','Positioning','Vision','Composure','Sliding Tackle']
        skills.clear()
        tags = self.soup.select('div:nth-child(6) div.col.col-12 ul.pl li')
        if(len(tags)==0):
            tags = self.soup.select('div:nth-child(5) div.col.col-12 ul.pl li')
        for tag in tags:
            span = tag.find_all('span')
            if(len(span) > 1):
                if not span[len(span)-1].text in ignore:
                    if(span[len(span)-1].text == 'Defensive Awareness'):
                        skills['marking'] = int(span[0].text)
                    else:
                        skills[f'{span[len(span)-1].text.replace(" ","_").lower()}'] = int(span[0].text)
        return skills

    def __get_player_traits(self):
        traits = []
        tags = self.soup.select('div:nth-child(6) > div > div.col.col-12 > div:nth-child(10) span')
        if len(tags) == 0:
            tags = self.soup.select('div:nth-child(5) > div > div.col.col-12 > div:nth-child(10) span')
        if len(tags) > 0:
            for tag in tags:
                traits.append(str(tag.text.strip()))
        return traits

    def __get_player_positions(self):
        positions = []
        # tags = self.soup.select('div.lineup div.bp3-tag')
        # for tag in tags:
        #     if tag.parent.get('style') in ['opacity:1', 'opacity:0.99', 'opacity:0.98']:
        #         positions.append(tag.contents[0].text.strip())
        tags = self.soup.select('div.info span')
        for tag in tags:
            positions.append(tag.text.strip())
        tags = self.soup.select_one('div.col.col-4 ul span.pos').text.strip()
        positions.append(tags)
        return positions
    
    def __get_player_age(self, birthday, season):
        datediff = int(datetime.now().year) - int(season)
        return str(int(birthday.replace(')','')) + datediff) + '/Jan/01'

    def player_json(self, player, version, season):
        pjson = {}
        self.url = f'https://sofifa.com/player/{player}?r={version}&set=true'
        self.__parse_page()
        pjson.clear()
        pjson['name'] = self.soup.select_one('div.info h1').text.strip()
        pjson['imageUrl'] = self.soup.select_one('div.bp3-card.player img').get("data-src")
        pjson['positions'] = self.__get_player_positions()
        pjson['nationality'] = self.soup.select_one('div.info div.meta.ellipsis a').get('title').strip()
        tmp = self.soup.select_one('div.info div.meta.ellipsis')
        tmp = tmp.contents[len(tmp)-1].text.split(' ')
        pjson['birth_date'] = self.__get_player_age(tmp[4], season)
        pjson['height'] = int(tmp[5].replace('cm',''))
        pjson['weight'] = int(tmp[6].replace('kg',''))
        pjson['overall_rating'] = int(self.soup.select_one('div.block-quarter span.bp3-tag').text)
        tmp = self.soup.select_one('div.block-quarter div.card').find_all('li')
        pjson['preferred_foot'] = tmp[0].contents[1].text.strip()
        pjson['weak_foot'] = int(tmp[1].contents[0].text)
        pjson['skill_moves'] = int(tmp[2].contents[0].text)
        pjson['international_reputation'] = int(tmp[3].contents[0].text)
        pjson['position_prefered_team'] = self.soup.select_one('div.col.col-4 ul span.pos').text.strip()
        pjson['skills'] = self.__get_player_skills(season)
        pjson['traits'] = self.__get_player_traits()
        return json.dumps(pjson)