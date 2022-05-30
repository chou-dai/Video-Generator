import requests
from bs4 import BeautifulSoup


class Baseball():
    def __init__(self):
        html = requests.get("https://baseball.yahoo.co.jp/npb/")
        soup = BeautifulSoup(html.text, 'html.parser')
        self.date = soup.select('h1.bb-head02__title')
        self.home_teams = soup.select('p.bb-score__homeLogo')
        self.away_teams = soup.select('p.bb-score__awayLogo')
        self.home_scores = soup.select('span.bb-score__score--left')
        self.away_scores = soup.select('span.bb-score__score--right')
        self.innings = soup.select('p.bb-score__link')
        links = soup.select('a.bb-score__content')
        self.link = []
        for n in range(len(links)):
            links[n] = links[n].get('href')
            self.link.append(links[n].replace('index', 'top'))
        num = self.date[0].text.find('（')
        self.date = self.date[0].text[:num]






    #全ての試合データ
    def all_game(self):
        home = []
        away = []
        h_score = []
        a_score = []
        ing = []
        count = 0

        for n in range(len(self.home_teams)):
            home.append(self.home_teams[n].text)
            away.append(self.away_teams[n].text)
            ing.append(self.innings[n].text)

            if(ing[n] == '見どころ' or ing[n] == '試合中止' or ing[n] == 'ノーゲーム'):
                h_score.append('')
                a_score.append('')
            else:
                h_score.append(str(self.home_scores[count].text))
                a_score.append(str(self.away_scores[count].text))
                count = count + 1

        return self.date, home, away, h_score, a_score, ing
    





    #試合詳細
    def detail_game(self, n):
        html = requests.get(self.link[n])
        soup = BeautifulSoup(html.text, 'html.parser')

        try:
            pit = soup.find('section', id='pit_rec')
            pit = pit.find_all('td', class_='bb-gameTable__data')
            win = self.adj_list(pit[0].get_text())
            lose = self.adj_list(pit[1].get_text())
            save = self.adj_list(pit[2].get_text())
        except AttributeError:
            win = ''
            lose = ''
            save = ''
            
        try:
            hr = soup.find('section', id='homerun')
            hr = hr.find_all('tr')
            home_hr = self.adj_list(hr[0].get_text(), 0)
            away_hr = self.adj_list(hr[1].get_text(), 0)
        except AttributeError:
            home_hr = ''
            away_hr = ''
        
        return win, lose, save, home_hr, away_hr
        
    #リスト調整
    def adj_list(self, str, i=1):
        list = []
        n = 0
        str = (str.replace(' ','').replace('、', '')).split('\n')
        while n < len(str):
            if str[n] != '':
                list.append(str[n])
            n += 1
        if i == 0:
            list = self.check(list)
        return list

    #本塁打の何回に打ったかを削除
    def check(self, list):
        for n in range(len(list)):
            num = list[n].find('(')
            if num != -1:
                list[n] = list[n][:num]
        return list







    #順位表
    def ranking(self):
        c_rank = self.get_rank(0)
        p_rank = self.get_rank(1)
        return c_rank, p_rank

    #順位取得
    def get_rank(self, num):
        #[順位, チーム, ゲーム差]
        ranking = [['' for n in range(3)] for m in range(6)]
        html = requests.get('https://baseball.yahoo.co.jp/npb/standings/')
        soup = BeautifulSoup(html.text, 'html.parser')

        rank = soup.find_all('section', class_='bb-modCommon01')[num]

        for i in range(6):
            rank_num = rank.find_all('tr', class_='bb-rankTable__row')[i]
            ranking[i][0] = rank_num.find('td', class_='bb-rankTable__data--rank').text
            ranking[i][1] = rank_num.find('td', class_='bb-rankTable__data--team').text.replace('\n','')
            ranking[i][2] = rank_num.find_all('td', class_='bb-rankTable__data')[7].text
            if ranking[i][2] == '-' or ranking[i-1][2] == '-':
                continue
            else:
                ranking[i][2] = str(float(ranking[i-1][2]) + float(rank_num.find_all('td', class_='bb-rankTable__data')[7].text)).replace('.0','')
        return ranking

    


