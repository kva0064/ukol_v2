import tkinter
import math

class Point: #vytvoření instance střed kružnice
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle: #vytvoření třídy kruh
    def __init__(self, radius, middle): #definování poloměru a středu kružnice
        self.middle = middle
        self.radius = radius

    def rot_circle(self, angle, speed): #definování azimutu úhlu mezi osou a středem kružnice a def. rychlosti
        if angle>360:
            self.angle = angle%360
        else:
            self.angle = angle
        self.speed = speed

    def draw(self, tocka): #vykreslení kružnice
        tocka.draw_circle(self)

class Tocka:

    def __init__(self): #definování okna ve kterém se kružnice zobrazí
        self.window = tkinter.Tk()
        self.window.title("Tocka")
        self.width = 1000
        self.canvas = tkinter.Canvas(self.window, width=self.width, height=700)
        self.canvas.pack()

    def show(self): #zobrazení okna po aplikování příkazu
        self.window.mainloop()

    def draw_circle(self, circle): #definování kružnice
        self.circle = circle
        x = circle.middle.x
        y = circle.middle.y
        r = circle.radius
        self.bod_osa = self.canvas.create_oval(x - r * (math.sin(math.radians(kruh.angle))),
                                            y + r * (math.cos(math.radians(kruh.angle))),
                                            x - r * (math.sin(math.radians(kruh.angle))),
                                            y + r * (math.cos(math.radians(kruh.angle))),
                                            outline="black", width= r/30)
        #definování osy, kolem které se kružnice bude točit
        self.kolecko = self.canvas.create_oval(x - r* (math.cos(math.radians(kruh.angle))),
                                               y - r,
                                               x + r* (math.cos(math.radians(kruh.angle))),
                                               y + r,
                                               outline="red", width=r / 30)
        self.move_circle()

    def move_circle(self): #definice trajektorie pohybu kružnice
            self.canvas.move(self.kolecko, (kruh.radius/56.5)*math.cos(math.radians(kruh.angle)), (kruh.radius/56.5)*math.sin(math.radians(kruh.angle)))
            self.canvas.after(self.circle.speed, self.move_circle)
            kruh.angle+=1
            #self.canvas.delete(self.kolecko)



bod = Point(400, 350) #zvolení počátečního středu kružnice (x,y)
kruh = Circle(100, bod) #zvolení poloměru kružnice
kruh.rot_circle(0, 15) #zvolení počátečního azimutu úhlu mezi osou a střdem kružnice a zvolení rychlosti
tocka = Tocka()
kruh.draw(tocka)
tocka.show()

