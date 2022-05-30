from manim import *
import datetime
import sqlite3


class InteractiveDevlopment(Scene):
    def construct(self):
        conn = sqlite3.connect('./database/baseball.db')
        self.c = conn.cursor()
        self.font = 'Shippori Mincho B1'
        today = datetime.datetime.now()
        ttl_text = Text('{}月{}日  プロ野球結果'.format(today.month, today.day), font=self.font, weight=BOLD)
        ttl_text.scale(1.2)
        ttl_text.shift(3.3*UP)
        self.play(Write(ttl_text))
        
        num, text = self.gameget()

        for n in range(num):
            text[n].shift((2-n)*UP)
            self.play(FadeIn(text[n],text[n]))


    def gameget(self):
        num = 0
        text = []
        today = datetime.datetime.now()
        month = '{0:02d}'.format(today.month)
        date = '{0:02d}'.format(today.day)
        day = '{}-{}-{}'.format(today.year, month, date)
        sql = "select * from all_game where date = '{}'".format(day)
        for row in self.c.execute(sql):
            l_num = len(row[2])
            r_num = len(row[3])
            if row[2] == 'DeNA':
                l_num = 3.5
            elif row[3] == 'DeNA':
                r_num = 3.5

            center = Text('-', font=self.font)

            left1 = Text(str(row[4]), font=self.font)
            left1.next_to(center,2*LEFT)
            left2 = Text(row[2], font=self.font, weight=BOLD, color=self.code(row[2]))
            left2.next_to(center, (6+(6-l_num))*LEFT)
            left2.set_stroke('#FFFFFF', width=1)

            right1 = Text(str(row[5]), font=self.font)
            right1.next_to(center,2*RIGHT)
            right2 = Text(row[3], font=self.font, weight=BOLD, color=self.code(row[3]))
            right2.next_to(center, (6+(6-r_num))*RIGHT)
            right2.set_stroke('#FFFFFF', width=1)

            group = VGroup(left2, left1, center, right1, right2)
            text.append(group)
            num += 1
        return num, text


    def code(self, str):
        team = ['巨人', '阪神', '中日', 'DeNA', '広島', 'ヤクルト', 'ソフトバンク', 'ロッテ', '西武', '楽天', '日本ハム', 'オリックス']
        color = ['#F97709', '#FFE201', '#002569', '#094A8C', '#FF0000', '#98C145', '#F9CA00', '#CCCCCC', '#102961', '#85010F', '#02518C', '#B08F32']
        for n in range(12):
            if str == team[n]:
                return color[n]