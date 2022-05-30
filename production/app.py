from manim import *
import datetime


class App():

    def __init__(self):
        self.time = datetime.datetime.now()
        self.week = ['月曜日','火曜日','水曜日','木曜日','金曜日','土曜日','日曜日']

    def cursor(self):
        return Polygon(1.3*RIGHT, UP+LEFT, 0.3*UP+0.7*LEFT, 0.3*UP+1.6*LEFT, 0.3*DOWN+1.6*LEFT, 0.3*DOWN+0.7*LEFT, DOWN+LEFT, 1.3*RIGHT,fill_color=WHITE, fill_opacity=1).set_stroke('#000', width=2).scale(0.25).rotate(TAU/3.2)

    def original(self):
        app_icon, app_text = self.make_app(YELLOW, 'オリジナル')
        return app_icon, app_text

    def click_cover(self):
        return self.make_app(BLACK, 'カバー', num=1).set_opacity(0.3)

    def amazon(self):
        app_icon, app_text = self.make_app('#ccab6c', 'Amazon', num=2)
        app_arrow = CurvedArrow(1*LEFT, 1*RIGHT, color=BLACK, radius=2).scale(0.7)
        app_sqr = RoundedRectangle(width=5, height=4, fill_color='#0aa4e3', corner_radius=0, fill_opacity=1).set_stroke(width=0).scale(0.13).align_to(app_icon, UP)
        return VGroup(app_icon, app_arrow, app_sqr), app_text

    def calendar(self):
        app_icon, app_text = self.make_app(WHITE, 'カレンダー', num=2)
        app_week = Text(self.week[self.time.weekday()], color=BLACK, font='Meiryo UI').scale(0.6).move_to([0,0.54,0])
        app_day = Text(str(self.time.day), color=BLACK, font='Meiryo UI').scale(1.6).move_to([0,-0.21,0])
        return VGroup(app_icon, app_week, app_day), app_text

    def instagram(self):
        app_icon, app_text = self.make_app(['#FFDD83','#F26939','#CF2E92','#4C64D3'], 'Instagram', num=2)
        app_sqr = RoundedRectangle(width=6.8, height=6.8, corner_radius=2).set_stroke(WHITE, width=13).scale(0.2)
        app_circ = Circle().set_stroke(WHITE, width=13).scale(0.34)
        app_dot = Dot().scale(1).move_to(0.4*UP+0.4*RIGHT)
        return VGroup(app_icon.rotate(-90*DEGREES), app_sqr, app_circ, app_dot), app_text

    def camera(self):
        app_icon, app_text = self.make_app(GRAY_C, 'カメラ',num=2)
        app_mark = Polygon(1.4*UP+2*RIGHT, 1.4*DOWN+2*RIGHT, 1.4*DOWN+2*LEFT, 1.4*UP+2*LEFT, 1.4*UP+1*LEFT, 1.8*UP+0.8*LEFT, 1.8*UP+0.8*RIGHT, 1.4*UP+1*RIGHT,fill_color=BLACK, fill_opacity=1).set_stroke(width=0).scale(0.35).move_to(app_icon.get_center())
        app_circ = Circle().set_stroke(GRAY_C, width=5).scale(0.28).move_to(0.05*DOWN)
        app_dot = Dot(color=YELLOW).scale(0.5).move_to(0.24*UP+0.35*RIGHT)
        return VGroup(app_icon, app_mark, app_circ, app_dot), app_text

    def itunes(self):
        app_icon, app_text = self.make_app(['#cc1af2', '#de6cc4'], 'iTunes Store', num=2)
        app_star = Star(color=WHITE, fill_opacity=0.8).set_stroke(width=0).scale(0.7).move_to(app_icon.get_center())
        return VGroup(app_icon, app_star), app_text

    def music(self):
        app_icon, app_text = self.make_app('#2104bd', 'amazonMusic')
        app_letter = Text('music', color=WHITE, font='Meiryo UI').scale(0.7)
        app_arrow = CurvedArrow(1*LEFT, 1*RIGHT, radius=2.5).scale(0.68).next_to(app_letter, 0.5*DOWN)
        return VGroup(app_icon, VGroup(app_letter, app_arrow).move_to(app_icon.get_center()+0.1*DOWN)), app_text

    def message(self):
        app_icon = self.make_app('#06c755', 'aaa', num=1)
        app_circ = Ellipse(width=3.5, height=3.1, fill_color=WHITE, fill_opacity=1).set_stroke(width=0).scale(0.42)
        app_poly = Polygon(1.3*RIGHT, LEFT, 4*DOWN, fill_color=WHITE, fill_opacity=1).set_stroke(width=0).rotate(-45*DEGREES).scale(0.07).move_to(app_icon.get_center()+0.57*DOWN+0.5*LEFT)
        return VGroup(app_icon, app_circ, app_poly)

    def safari(self):
        app_icon = self.make_app(WHITE, 'Safari', num=1)
        app_circ = Circle(fill_color=['#1c7cf4','#2aaffb'], fill_opacity=1).set_stroke(width=0).scale(0.86)
        app_red = Polygon(0.8*RIGHT, 6*UP, 0.8*LEFT, fill_color='＃FF0000', fill_opacity=1).set_stroke(width=0)
        app_white = Polygon(0.8*RIGHT, -6*UP, 0.8*LEFT, fill_color='＃FFFFFF', fill_opacity=1).set_stroke(width=0)
        return VGroup(app_icon, VGroup(app_circ, VGroup(app_red, app_white).scale(0.14)).rotate(-45*DEGREES))
    
    def facebook(self):
        app_icon = self.make_app(['#3b5998','#62dafc'], 'Facebook', num=1)
        app_text = Text('f', color=WHITE, font='Berlin Sans FB').scale(3.6).move_to(0.1*DOWN+0.3*RIGHT)
        return VGroup(app_icon, app_text)

    def youtube(self):
        app_icon = self.make_app(WHITE, 'YouTube', num=1)
        app_red = RoundedRectangle(width=7.5, height=5.2, fill_color='＃FF0000', corner_radius=1.2, fill_opacity=1).set_stroke(width=0).scale(0.2)
        app_tri = Triangle(fill_color=WHITE, fill_opacity=1).set_stroke(width=0).scale(0.28).rotate(-90*DEGREES).move_to(app_icon.get_center()+0.1*RIGHT)
        return VGroup(app_icon, app_red, app_tri)

    def make_app(self, color, letter=' ', num=0):
        icon = RoundedRectangle(width=10, height=10, fill_color=color, corner_radius=2, fill_opacity=1).set_stroke(width=0).scale(0.2)
        if num == 1:
            return icon
        text = Text(letter, font='Meiryo UI').scale(0.6).next_to(icon, DOWN)
        if num == 2:
            return icon, text
        app_set = VGroup(icon, text)
        return app_set