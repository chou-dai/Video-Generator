from manim import *

class Indications(Scene):
    # def construct(self):
    #     indications = [ApplyWave,Circumscribe,Flash,FocusOn,Indicate,ShowPassingFlash,Wiggle]
    #     names = [Tex(i.__name__).scale(3) for i in indications]

    #     tex = MathTex(r'x(t)=\int{udu}+C=\frac{u^2}{2}+C=\frac{(\log{t})^2}{2}+C').scale(1.5)
    #     self.play(Write(tex))

    #     self.play(ApplyWave(tex))

    #     # self.add(names[0])
    #     # for i in range(len(names)):
    #     #     if indications[i] is Flash:
    #     #         self.play(Flash(UP))
    #     #     elif indications[i] is ShowPassingFlash:
    #     #         self.play(ShowPassingFlash(Underline(names[i])))
    #     #     else:
    #     #         self.play(indications[i](names[i]))
    #     #     self.play(AnimationGroup(
    #     #         FadeOut(names[i], shift=UP*1.5),
    #     #         FadeIn(names[(i+1)%len(names)], shift=UP*1.5),
    #     #     ))

    def construct(self):
        func = lambda pos: ((pos[0]*UR+pos[1]*LEFT) - pos)/3
        tex = MathTex(r'x(t)=\int{udu}+C=\frac{u^2}{2}+C=\frac{(\log{t})^2}{2}+C', weight=BOLD).set_stroke(WHITE, width=2).scale(1.3)

        self.play(StreamLines(func).create(), run_time=2)
        self.play(Write(tex), run_time=1)
        self.play(ApplyWave(tex))