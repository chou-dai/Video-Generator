from manim import *
import datetime
import os
import glob
from app import App
import shutil
from pydub import AudioSegment




class InteractiveDevlopment(Scene):

    def construct(self):

        # 設定
        self.setting()

        # スマートフォン
        self.smart_phone()

        # オープニング
        self.opening()

        # No1
        self.number_1()




#========================== 設定 ==========================
    def setting(self):

        # BGM設定
        BGM = '勝者' # BGMファイル名
        bgm_time = 20       # BGM時間

        samplePath = 'C:/Users/c.daiki/Desktop/production/bgm/' + BGM +'.mp3'
        bgmPath = 'C:/Users/c.daiki/Desktop/production/bgm/bgm.mp3'
        shutil.copy(samplePath, bgmPath)
        sound = AudioSegment.from_file(bgmPath, format="mp3")
        bgm = sound[:(bgm_time+1)*1000]
        bgm.export(bgmPath, format="mp3")
        self.back_bgm = './bgm/bgm.mp3'

        # 余分なファイルの削除
        def remove(path):
            files = glob.glob(path)
            for p in files:
                os.remove(p)
        path = [
          'C:/Users/c.daiki/Desktop/production/media/videos/shorts/480p15/partial_movie_files/InteractiveDevlopment/*',
          'C:/Users/c.daiki/Desktop/production/media/videos/shorts/1080p60/partial_movie_files/InteractiveDevlopment/*'
        ]
        for n in range(len(path)):
            remove(path[n])

        self.app = App()
        self.font = 'Shippori Mincho B1'
        self.time = datetime.datetime.now()
        self.minute = '{0:02d}'.format(self.time.minute)
        self.week = ['月曜日','火曜日','水曜日','木曜日','金曜日','土曜日','日曜日']

        # サウンド設定
        self.click_sound = './bgm/click.wav'
        self.title_sound = './bgm/和太鼓でドドン.mp3'
        self.swipe_sound = './bgm/スワイプ.mp3'





#========================== スマートフォン ==========================
    def smart_phone(self):
        out_color = '#555555'
        main_color = '#666666'
        filter_color = '#ffffff'

        black = RoundedRectangle(width=14.2, height=26, corner_radius=0).set_stroke(width=10)
        smart_out = RoundedRectangle(width=14.1, height=25, corner_radius=1.5).set_stroke(width=10)
        smart_out_filter = RoundedRectangle(width=13.6, height=24.5, corner_radius=1.5).set_stroke(width=0)
        screen = RoundedRectangle(width=12.9, height=19, corner_radius=0).set_stroke(width=10)
        film = RoundedRectangle(width=12.9, height=19, corner_radius=0, fill_opacity=0.15).set_stroke(width=0)
        home_btn = Circle(color='#666666').move_to([0,-11,0]).set_stroke('#666666', width=20)
        sound =RoundedRectangle(width=3, height=0.22, fill_color='#000', corner_radius=0.1, fill_opacity=0.9).set_stroke(out_color, width=1).move_to([0,10.6,0])
        camera = Dot(fill_color='#000').set_stroke(out_color, width=1).scale(3).move_to([-2.3,10.65,0])
        dot = Dot(fill_color='#000').set_stroke(out_color, width=1).scale(2).next_to(sound, 2.4*UP)

        cut_black = Cutout(black, smart_out, fill_opacity=1, color=BLACK)
        cut_out = Cutout(smart_out, screen, fill_opacity=1, color=main_color, stroke_color=out_color).set_stroke(out_color,width=10)
        cut_out_filter = Cutout(smart_out_filter, screen, fill_opacity=0.2, color=filter_color, stroke_color=main_color)
        attached_set = VGroup(sound, camera, dot)

        self.smart = VGroup(film, cut_black, cut_out, cut_out_filter, home_btn, attached_set, z_index=100)
        self.add(self.smart)
        self.wait()



#========================== 表示上部の情報 ==========================
    def information(self, num):
        wave1 = RoundedRectangle(width=3, height=4, fill_color='#fff', corner_radius=1, fill_opacity=1).set_stroke(width=0)
        wave2 = RoundedRectangle(width=3, height=6, fill_color='#fff', corner_radius=1, fill_opacity=1).set_stroke(width=0).next_to(wave1, 2*RIGHT).align_to(wave1, DOWN)
        wave3 = RoundedRectangle(width=3, height=8, fill_color='#fff', corner_radius=1, fill_opacity=1).set_stroke(width=0).next_to(wave2, 2*RIGHT).align_to(wave1, DOWN)
        wave4 = RoundedRectangle(width=3, height=10, fill_color='#fff', corner_radius=1, fill_opacity=0.3).set_stroke(width=0).next_to(wave3, 2*RIGHT).align_to(wave1, DOWN)
        wave = VGroup(wave1, wave2, wave3, wave4).move_to([-5.9,8.9,0]).scale(0.045)
        docomo = Text('docomo 5G', font='Arial').scale(0.7).next_to(wave, 1*RIGHT).align_to(wave, DOWN)
        left_set = VGroup(wave, docomo)

        charge1 = RoundedRectangle(width=21, height=10,  corner_radius=2, fill_opacity=0).set_stroke('#ccc', width=3)
        charge2 = RoundedRectangle(width=1.2, height=4, fill_color='#ccc', corner_radius=0.5, fill_opacity=1).set_stroke(width=0).next_to(charge1, 5*RIGHT)
        charge3 = RoundedRectangle(width=10, height=7.5, fill_color='#fff', corner_radius=2, fill_opacity=1).set_stroke(width=0).move_to([-4.7,0,0])
        charge = VGroup(charge1, charge2, charge3).move_to([5.7,9,0]).scale(0.04)
        charge_text = Text("49%", font='Arial').scale(0.7).next_to(charge, 0.5*LEFT)
        right_set = VGroup(charge, charge_text).align_to(left_set, DOWN)

        t = datetime.datetime.now()
        min = '{0:02d}'.format(t.minute)
        center_set = Text('{}:{}'.format(t.hour, min), font='Meiryo UI', t2f={':':''}).scale(0.7).align_to(left_set, DOWN)

        if num == 0:
            return left_set, right_set
        else:
            return left_set, right_set, center_set




#========================== オープニング ==========================
    def opening(self):

        start_left, start_right = self.information(0)
        start_screen = RoundedRectangle(width=14, height=20, fill_color='#fff', corner_radius=0, fill_opacity=1)
        start_screen.set_color(color=['#d1a172', '#c17c4c', '#c8c6cc', '#0a8e7b', '#067668', '#045948', '#164043', '#043b34' '#121b1d'])
        start_time = Text('{}:{}'.format(self.time.hour, self.minute), font='Meiryo UI', t2f={':':''}).scale(3).move_to([0,5,0])
        start_day = Text('{}月{}日 {}'.format(self.time.month, self.time.day, self.week[self.time.weekday()]), font='Meiryo UI').scale(1.3).next_to(start_time, 2*DOWN)
        start_time_set = VGroup(start_time, start_day)
        start_message = RoundedRectangle(width=12.5, height=2, fill_color='#fff', corner_radius=0.4, fill_opacity=0.4).set_stroke(width=0).next_to(start_time_set, 4.4*DOWN)
        start_set = VGroup(start_screen, start_left, start_right, start_time_set, start_message)


        #　アプリ作成
        opening_left, opening_right, opening_center = self.information(1)
        opening_screen = RoundedRectangle(width=14, height=20, fill_color=WHITE, corner_radius=0, fill_opacity=0.9)
        opening_screen.set_color(color=[BLUE, BLACK])
        opening_set = VGroup(opening_screen, opening_left, opening_right, opening_center)

        amazon_icon, amazon_text = self.app.amazon()
        amazon = VGroup(amazon_icon, amazon_text)
        calendar_icon, calendar_text = self.app.calendar()
        calendar = VGroup(calendar_icon, calendar_text).next_to(amazon, 3.8*RIGHT)
        instagram_icon, instagram_text = self.app.instagram()
        instagram = VGroup(instagram_icon, instagram_text).next_to(calendar, 3.8*RIGHT)
        camera_icon, camera_text = self.app.camera()
        camera = VGroup(camera_icon, camera_text).next_to(instagram, 3.8*RIGHT)
        itunes_icon, itunes_text = self.app.itunes()
        itunes = VGroup(itunes_icon, itunes_text).next_to(amazon_icon, 3.8*DOWN)
        music_icon, music_text = self.app.music()
        music = VGroup(music_icon, music_text).next_to(calendar_icon, 3.8*DOWN)
        original_icon, original_text = self.app.original()
        original = VGroup(original_icon, original_text).next_to(music_icon, 3.8*RIGHT).align_to(music, DOWN)
        op_app = VGroup(amazon, calendar, instagram, camera, itunes, music, original)
        op_app.move_to(self.smart.get_center()+5.2*UP)

        under = RoundedRectangle(width=13, height=3.1, fill_color='#000', corner_radius=0, fill_opacity=0.4).set_stroke(width=0)
        message = self.app.message()
        safari = self.app.safari().next_to(message, 3.8*RIGHT)
        facebook = self.app.facebook().next_to(safari, 3.8*RIGHT)
        youtube = self.app.youtube().next_to(facebook, 3.8*RIGHT)
        under_app = VGroup(message, safari, facebook, youtube).move_to(self.smart.get_center())
        op_under_set = VGroup(under, under_app).move_to(8*DOWN)

        cover = self.app.click_cover().move_to(original_icon.get_center())
        cursor = self.app.cursor()
        cursor.generate_target()
        cursor.target.move_to(original.get_center())
        opening_set.add(op_app, op_under_set, cursor.move_to(2*DOWN+2*LEFT))
        self.original_screen = RoundedRectangle(width=14, height=20, fill_color=[ORANGE, YELLOW], corner_radius=0, fill_opacity=0.7)

        # アニメーション
        self.add_sound(self.back_bgm, gain=-30)
        self.add_sound('./bgm/start1.wav', gain=-7)
        self.play(FadeIn(start_set), run_time=0.8)
        self.add(self.smart)
        self.wait(1.0)
        self.play(FadeIn(opening_set), FadeOut(start_set, shift=20*UP), run_time=0.3)
        self.add(self.smart)
        self.wait(0.3)
        self.play(MoveToTarget(cursor, run_time=0.5))
        self.add_sound(self.click_sound)
        self.add(cover, cursor)
        self.add(self.smart)
        self.wait(0.4)
        self.play(FadeOut(opening_set, run_time=0.1), ReplacementTransform(original_icon, self.original_screen, run_time=0.3))
        self.add(self.smart)
        self.wait()



#========================== タイトル画面作成 ==========================
    def make_title(self, title, sub_title):
        head1 = Text(title, font=self.font, color=BLACK, weight=BOLD).scale(2.2).shift(4*UP)
        head2 = Text(sub_title, font=self.font, color=BLACK, weight=BOLD).scale(1.8).next_to(head1, 5*DOWN)
        head = VGroup(head1, head2)
        original_set = VGroup(self.original_screen, head)
        self.add_sound(self.title_sound, gain=-10)
        self.play(FadeInFrom(head, 0.8*UP), run_time=0.2)
        self.wait(1)
        self.add_sound(self.swipe_sound, gain=-10)
        self.play(FadeOut(original_set, shift=20*UP), run_time=0.5)




#========================== No1 ==========================
    def number_1(self):
        self.make_title('a', 'b')
