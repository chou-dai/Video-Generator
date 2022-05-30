from manim import *

class ExampleThreeD(ThreeDScene):
CONFIG = {
"plane_kwargs" : {
"color" : RED_B
},
"point_charge_loc" : 0.5*RIGHT-1.5*UP,
}
def construct(self):
self.set_camera_position(0, -np.pi/2)
plane = NumberPlane(**self.plane_kwargs)
plane.main_lines.fade(.9)
plane.add(plane.get_axis_labels())
self.add(plane)
 
field2D = VGroup(*[self.calc_field2D(x*RIGHT+y*UP)
for x in np.arange(-9,9,1)
for y in np.arange(-5,5,1)
])
 
self.play(ShowCreation(field2D))
self.wait()
self.move_camera(0.8*np.pi/2, -0.45*np.pi)
self.begin_ambient_camera_rotation()
self.wait(6)
 
def calc_field2D(self,point):
x,y = point[:2]
Rx,Ry = self.point_charge_loc[:2]
r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
efield = (point - self.point_charge_loc)/r**3
return Vector(efield).shift(point)