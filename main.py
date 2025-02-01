from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.clock import Clock
import random
import math

# Configuración de pantalla
ANCHO = 1080
ALTO = 1920

class Particula:
    def __init__(self, widget):
        self.widget = widget
        self.x = random.randint(0, ANCHO)
        self.y = random.randint(0, ALTO)
        self.radio = random.randint(3, 8)
        self.velocidad_x = random.uniform(-2, 2)  # Movimiento horizontal
        self.velocidad_y = random.uniform(1, 3)  # Movimiento vertical
        self.angulo = random.uniform(0, 360)  # Ángulo de movimiento
        self.amplitud = random.uniform(20, 50)  # Para hacer que las partículas se muevan en trayectorias más complejas

        with self.widget.canvas:
            Color(0.67, 0, 1, 0.8)  # Color morado neón con transparencia
            self.ellipse = Ellipse(pos=(self.x, self.y), size=(self.radio * 2, self.radio * 2))

    def mover(self):
        # Movimiento dinámico con dirección y velocidad ajustada
        self.x += self.velocidad_x * math.sin(math.radians(self.angulo))
        self.y += self.velocidad_y

        # Amplitud para movimiento más fluido
        self.x += self.amplitud * math.sin(math.radians(self.angulo))

        if self.y > ALTO:
            self.y = 0
            self.x = random.randint(0, ANCHO)

        if self.x > ANCHO:
            self.x = 0
        elif self.x < 0:
            self.x = ANCHO

        self.ellipse.pos = (self.x, self.y)

class FondoAnimado(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.particulas = [Particula(self) for _ in range(100)]
        Clock.schedule_interval(self.actualizar, 1 / 30)

    def actualizar(self, dt):
        for particula in self.particulas:
            particula.mover()

class FondoApp(App):
    def build(self):
        return FondoAnimado()

if __name__ == "__main__":
    FondoApp().run()
