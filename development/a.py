from manim import *
import datetime
import sqlite3



class InteractiveDevlopment(Scene):

    def gameget(self):
        conn = sqlite3.connect('baseball.db')
        c = conn.cursor()
        today = '2021-06-06'
        sql = "select * from all_game where date = '{}'".format(today)
        n=0
        self.all_game = []
        for row in c.execute(sql):
            l_num = len(row[2])
            r_num = len(row[3])

            if row[2] == 'DeNA':
                l_num = 3.5
            elif row[3] == 'DeNA':
                r_num = 3.5

            center = Text('-', font='Shippori Mincho B1')

            left1 = Text(str(row[4]), font='Shippori Mincho B1')
            left1.next_to(center,2*LEFT)
            left2 = Text(row[2], font='Shippori Mincho B1', weight=BOLD, color=self.code(row[2]))
            left2.next_to(center, (6+(6-l_num))*LEFT)
            left2.set_stroke('#FFFFFF', width=1)

            right1 = Text(str(row[5]), font='Shippori Mincho B1')
            right1.next_to(center,2*RIGHT)
            right2 = Text(row[3], font='Shippori Mincho B1', weight=BOLD, color=self.code(row[3]))
            right2.next_to(center, (6+(6-r_num))*RIGHT)
            right2.set_stroke('#FFFFFF', width=1)
            text = VGroup(left2, left1, center, right1, right2)
            self.all_game.append(text)

            n+=1
        conn.close()
        
        
    def code(self, str):
        team = ['巨人', '阪神', '中日', 'DeNA', '広島', 'ヤクルト', 'ソフトバンク', 'ロッテ', '西武', '楽天', '日本ハム', 'オリックス']
        color = ['#F97709', '#FFE201', '#609AFF', '#66ADF4', '#FF0000', '#98C145', '#F5C700', '#FFFFFF', '#5481E2', '#E8021D', '#E1A823', '#D5BA70']
        for n in range(12):
            if str == team[n]:
                return color[n]


    def construct(self):
        self.gameget()
        num = len(self.all_game)
        today = datetime.datetime.now()
        text = Text('{}月{}日　プロ野球結果' .format(today.month, today.day), font='Shippori Mincho B1')
        
        text.shift(3.3*UP)
        self.play(FadeIn(text))

        for n in range(num):
            self.all_game[n].shift((2-n)*UP)
            self.play(Write(self.all_game[n]))