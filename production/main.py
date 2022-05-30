from sys import path
from typing_extensions import runtime
from manim import *
import datetime
import sqlite3
from PIL import Image
from manim.utils import tex


class InteractiveDevlopment(Scene):
    def construct(self):

        # SQL開始
        conn = sqlite3.connect('./database/baseball.db')
        self.c = conn.cursor()


        # 設定
        self.setting()

        
        # 全試合
        self.all()

        # 試合詳細
        self.detail()

        # 順位表
        self.ranking()

        # SQL終了
        conn.commit()
        conn.close()


    def a(self):
        text = Tex(r'f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6')
        self.play(Write(text))





    def develop(self):
        text = 'こんにちは'
        set = VGroup()
        num = 0
        code = ['#444', '#555', '#666', '#777', '#888', '#999', '#999', '#fff']

        for color in zip(code):
            t = Text(text, font=self.font, weight=BOLD).set_stroke(color, width=2).move_to([-0.02*num, 0.02*num, 0]).scale(3)
            t.set_color(color)
            if num == len(code)-1:
                t.set_stroke('#999', width=2)
            num+=1
            set.add(t)

        self.play(FadeIn(set.move_to([0.02*(len(code)-1), -0.02*(len(code)-1), 0])))






#========================== 設定 ==========================
    def setting(self):
        # フォント
        self.font = 'Shippori Mincho B1'

        # データベース日付
        today = datetime.datetime.now()
        month = '{0:02d}'.format(today.month)
        date = '{0:02d}'.format(today.day)
        self.day = '{}-{}-{}'.format(today.year, month, date)






#========================== カラーコード ==========================
    def code(self, str):
        team = ['巨人', '阪神', '中日', 'DeNA', '広島', 'ヤクルト', 'ソフトバンク', 'ロッテ', '西武', '楽天', '日本ハム', 'オリックス']
        color = ['#F97709', '#FFE201', '#002569', '#094A8C', '#FF0000', '#98C145', '#F9CA00', '#CCCCCC', '#102961', '#85010F', '#02518C', '#B08F32']
        
        for n in range(12):
            if str == team[n]:
                return color[n]









#========================== 全試合 ==========================
    def all(self):

        today = datetime.datetime.now()
        ttl_text = Text('{}月{}日　プロ野球結果'.format(today.month, today.day), font=self.font, weight=BOLD).scale(1.2)
        ttl_text.shift(3.3*UP)
        self.play(Write(ttl_text))
        
        num, text = self.get_game()

        text.insert(0,Text('   '))
        for n in range(num):
            text[n+1].shift((2-n)*UP)
            self.play(Transform(text[n],text[n+1]))
        self.wait(1.5)
        self.play(FadeOut(ttl_text, text[1%num], text[2%num], text[3%num], text[4%num], text[5%num], text[6%num]))

    #----------SQLから全試合データ取得----------
    def get_game(self):
        num = 0
        text = []
        sql = "SELECT * FROM all_game WHERE date = '{}'".format(self.day)
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








#========================== 試合詳細 ==========================
    def detail(self):
        num, text = self.get_game()
        num, text_shadow = self.get_game()
        square = []
        text_set = []
        self.scale = 0.85

        win_ttl = self.make_ttl('勝利投手').move_to([-4.3, 1.5, 0]).scale(self.scale)
        win_shadow = self.make_ttl('勝利投手', 1).move_to([-4.23, 1.43, 0]).scale(self.scale)
        win_set = VGroup(win_shadow, win_ttl)
        lose_ttl = self.make_ttl('敗戦投手').next_to(win_ttl, 1.0*DOWN).scale(self.scale)
        lose_shadow = self.make_ttl('敗戦投手', 1).next_to(win_shadow, 1.0*DOWN).scale(self.scale)
        lose_set = VGroup(lose_shadow, lose_ttl)
        save_ttl = self.make_ttl('セーブ').next_to(lose_ttl, 1.0*DOWN).scale(self.scale)
        save_shadow = self.make_ttl('セーブ', 1).next_to(lose_shadow, 1.0*DOWN).scale(self.scale)
        save_set = VGroup(save_shadow, save_ttl)
        hr_ttl = self.make_ttl('ホームラン').next_to(save_ttl, 1.7*DOWN).scale(self.scale)
        hr_shadow = self.make_ttl('ホームラン', 1).next_to(save_shadow, 1.7*DOWN).scale(self.scale).set_opacity(0.6)
        hr_set = VGroup(hr_shadow, hr_ttl)
        hr_square = RoundedRectangle(width=13, height=2.7, corner_radius=0.03, fill_opacity=0.2, z_index=-101).set_stroke('#ffffff',width=1).move_to([0,-2.05,0])

        for i in range(num):
            win, lose, save = self.get_pitch(i)
            win_s, lose_s, save_s = self.get_pitch(i)
            home_hr, away_hr, home_team, away_team = self.get_homerun(i)
            home_hr_s, away_hr_s, home_team, away_team = self.get_homerun(i)

            win.next_to(win_ttl, 4*RIGHT)
            win_s.set_color('#000000').set_stroke('#00000', width=1).next_to(win_shadow, 4*RIGHT)
            lose.next_to(lose_ttl, 4*RIGHT)
            lose_s.set_color('#000000').set_stroke('#00000', width=1).next_to(lose_shadow, 4*RIGHT)
            save.next_to(save_ttl, 5*RIGHT)
            save_s.set_color('#000000').set_stroke('#00000', width=1).next_to(save_shadow, 5*RIGHT)
            pitch_set = VGroup(win_s, win, lose_s, lose, save_s, save)

            home_hr_text = VGroup()
            home_hr_shadow = VGroup()
            for j in range(len(home_hr)):
                if j == 0:
                    home_hr_text.add(home_hr[0])
                    home_hr_shadow.add(home_hr_s[0])
                    continue
                if i == 0 and j == 2:
                    home_hr[j].next_to(home_hr[j-2], 1.2*DOWN)
                    home_hr_s[j].next_to(home_hr_s[j-2], 1.2*DOWN)
                    home_hr_text.add(home_hr[j])
                    home_hr_shadow.add(home_hr_s[j])
                else:
                    home_hr[j].next_to(home_hr[j-1], 1.2*RIGHT)
                    home_hr_s[j].next_to(home_hr_s[j-1], 1.2*RIGHT)
                    home_hr_text.add(home_hr[j])
                    home_hr_shadow.add(home_hr_s[j])

            away_hr_text = VGroup()
            away_hr_shadow = VGroup()
            for j in range(len(away_hr)):
                if j == 0:
                    away_hr_text.add(away_hr[0])
                    away_hr_shadow.add(away_hr_s[0])
                    continue
                if i == 0 and j == 2:
                    away_hr[j].next_to(away_hr[j-2], 1.2*DOWN)
                    away_hr_s[j].next_to(away_hr_s[j-2], 1.2*DOWN)
                    away_hr_text.add(away_hr[j])
                    away_hr_shadow.add(away_hr_s[j])
                else:
                    away_hr[j].next_to(away_hr[j-1], 1.2*RIGHT)
                    away_hr_s[j].next_to(away_hr_s[j-1], 1.2*RIGHT)
                    away_hr_text.add(away_hr[j])
                    away_hr_shadow.add(away_hr_s[j])
            away_hr_text.next_to(home_hr_text, DOWN)
            away_hr_shadow.next_to(home_hr_shadow, DOWN)
            hr_text = VGroup(home_hr_text, away_hr_text).move_to([0, -2.1, 0])
            hr_s = VGroup(home_hr_shadow, away_hr_shadow).move_to([0.07, -2.17, 0]).set_color('#000000').set_stroke('#00000', width=1).set_opacity(0.6)
            hr = VGroup(hr_s, hr_text)

            square.append(RoundedRectangle(width=14.1, height=7.8, corner_radius=0.03, fill_opacity=0.35, z_index=-100).set_stroke('#FFFFFF',width=3).move_to([0,0,0]))
            square[i].set_color(color=[self.code(home_team), self.code(away_team)])

            text[i].shift(3*UP).scale(1.2)
            text_shadow[i].set_color('#000000').shift(2.92*UP).shift(0.08*RIGHT).scale(1.2).set_stroke('#00000', width=1)
            text_set.append(VGroup(text_shadow[i], text[i]))

            if i == 0:
                self.play(FadeInFromLarge(square[i], scale_factor=0.1, run_time=1))
                self.play(FadeIn(text_set[i], win_set, lose_set, save_set, hr_set, hr_square))
            else:
                self.play(ReplacementTransform(text_set[i-1], text_set[i]), ReplacementTransform(square[i-1], square[i]))
                self.wait()
            
            self.play(FadeInFrom(pitch_set, 0.2*DOWN, run_time=1))
            self.play(FadeInFrom(hr, 0.2*DOWN, run_time=1))
            self.wait(2)
            self.play(FadeOut(pitch_set, hr))
            if i == (num-1):
                end = VGroup(text_set[i], win_set, lose_set, save_set, hr_set, hr_square, square[i])
                self.play(ShrinkToCenter(end, run_time=1))
                self.play(FadeOut(end, run_time=0.1))


    #----------SQLから勝利・敗戦投手を取得----------
    def get_pitch(self, num):
        win = ''
        lose = ''
        save = ''

        sql = "SELECT * FROM pitch WHERE id = {} AND date = '{}'".format(num, self.day)
        for row in self.c.execute(sql):
            win = self.make_text(row[2], row[3], row[4])
            lose = self.make_text(row[5], row[6], row[7])
            save = self.make_text(row[8], row[9], row[10])

        return win, lose, save

    #----------SQLからホームランを取得----------
    def get_homerun(self, num):
        home_hr = []
        away_hr = []
        home_team = ''
        away_team = ''
        i = 0
        none_hr = 0

        sql = "SELECT * FROM homerun WHERE id = {} AND date = '{}'".format(num, self.day)
        for row in self.c.execute(sql):
            if row[2] == 0:
                if i == 0:
                    home_team = row[3]
                    i = 1
                    if row[4] != '':
                        home_hr.append(self.make_text(home_team, row[4], row[5]))
                    else:
                        none_hr += 1
                else:
                    home_hr.append(self.make_text_sub(row[4], row[5]))
            else:
                if i == 1:
                    away_team = row[3]
                    i = 2
                    if row[4] != '':
                        away_hr.append(self.make_text(away_team, row[4], row[5]))
                    else:
                        none_hr += 1
                else:
                    away_hr.append(self.make_text_sub(row[4], row[5]))
            
            if none_hr == 2:
                home_hr = Text('なし', weight=BOLD, font=self.font)

        return home_hr, away_hr, home_team, away_team

    #----------テキスト作成----------
    def make_ttl(self, word, code=0):
        if code == 0:
            return Text(word, weight=BOLD, font=self.font)
        else:
            return Text(word, weight=BOLD, font=self.font, color='#000000')

    def make_text(self, team, player, count):
        team = Text(team, font = self.font, weight=BOLD, color=self.code(team)).scale(self.scale).set_stroke('#FFFFFF', width=1)
        player = Text(player, weight=BOLD, font = self.font).next_to(team).scale(self.scale)
        count = Text(count, font = self.font).next_to(player).scale(self.scale)
        text = VGroup(team, player, count)
        return text

    def make_text_sub(self, player, count):
        player = Text(player, weight=BOLD, font = self.font).scale(self.scale)
        count = Text(count, font = self.font).next_to(player).scale(self.scale)
        text = VGroup(player, count)
        return text










#========================== 順位表 ==========================
    def ranking(self):
        text = Text('順位表', font=self.font, weight=BOLD).move_to([0, 3.4, 0]).scale(1.3)

        c_square = RoundedRectangle(width=5.9,height=6.2,fill_color='#78BC84',corner_radius=0.03, fill_opacity=0.2).set_stroke('#ffffff',width=2)
        c_rank, c_shadow = self.get_rank(0)
        c_rank.set_opacity(0).move_to([0, -0.25, 0])
        c_shadow.set_opacity(0).move_to([0.08, -0.33, 0])
        c_label = Text("セリーグ",font=self.font, weight=BOLD, color='#78BC84').move_to([0, 3.15, 0]).set_stroke('#FFFFFF', width=1).set_opacity(1)
        c_label_s = Text("セリーグ",font=self.font, weight=BOLD, color='#000000').move_to([0.05, 3.1, 0]).set_stroke('#000000', width=1).set_opacity(0.8)
        c_set = VGroup(c_square, c_label_s, c_label, c_shadow, c_rank).move_to([-3, -0.6, 0])

        p_square = RoundedRectangle(width=5.9,height=6.2,fill_color='#259CCF',corner_radius=0.03,fill_opacity=0.2).set_stroke('#ffffff',width=2)
        p_rank, p_shadow = self.get_rank(1)
        p_rank.set_opacity(0).move_to([0, -0.25, 0])
        p_shadow.set_opacity(0).move_to([0.08, -0.33, 0])
        p_label = Text("パリーグ",font=self.font, weight=BOLD, color='#259CCF').move_to([0, 3.15, 0]).set_stroke('#FFFFFF', width=1).set_opacity(1)
        p_label_s = Text("パリーグ",font=self.font, weight=BOLD, color='#000000').move_to([0.05, 3.1, 0]).set_stroke('#000000', width=1).set_opacity(0.8)
        p_set = VGroup(p_square, p_label_s, p_label, p_shadow, p_rank).move_to([3, -0.6, 0])

        self.play(Write(text))

        league_set = VGroup(c_set, p_set)
        self.play(FadeIn(league_set, run_time=1.2))

        rank_set = VGroup(c_shadow.set_opacity(1), c_rank.set_opacity(1), p_shadow.set_opacity(1), p_rank.set_opacity(1))
        self.play(FadeInFrom(rank_set, 0.2*DOWN, run_time=1))
        self.wait()

    #----------SQLから順位表データ取得----------
    def get_rank(self, num):
        text = VGroup()
        shadow = VGroup()
        n = 0
        sql = "SELECT * FROM ranking WHERE id = {} AND date = '{}'".format(num, self.day)
        
        for row in self.c.execute(sql):
            rank = Text(row[2], font=self.font)
            team = Text(row[3], font=self.font, weight=BOLD, color=self.code(row[3])).set_stroke('#FFFFFF', width=1)
            team.next_to(rank, 3.5*RIGHT)
            group = VGroup(rank, team).shift((2-n*0.9)*UP)

            s_rank = Text(row[2], font=self.font, color='#000000').set_stroke('#000000', width=1)
            s_team = Text(row[3], font=self.font, weight=BOLD, color='#000000').set_stroke('#000000', width=1)
            s_team.next_to(s_rank, 3.5*RIGHT)
            s_group = VGroup(s_rank, s_team).shift((2-n*0.9)*UP)

            text.add(group)
            shadow.add(s_group)
            n += 1
        return text, shadow
