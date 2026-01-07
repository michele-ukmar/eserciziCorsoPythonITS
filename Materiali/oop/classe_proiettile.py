# projectile.py
"""proiettile.py
Provides a simple class for modeling the flight of projectiles."""

from math import pi, sin, cos

class Proiettile:
    """Simula il volo di semplici proiettili vicino alla terra
    superficie, ignorando la resistenza al vento. 
    Il tracciamento viene eseguito in dueDimensioni, altezza (y) 
    e distanza (x)"""
    def __init__(self, angle, velocity, height):
        """Creare un proiettile con un determinato angolo di lancio
          iniziale, Velocità e altezza"""
        self.xpos = 0.0
        self.ypos = height
        theta = pi * angle / 180.0
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)
    def update(self, time):
        """Update the state of this projectile to move it time seconds
        farther into its flight"""
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1
    def getY(self):
        "Returns the y position (height) of this projectile."
        return self.ypos
    def getX(self):
        "Returns the x position (distance) of this projectile."
        return self.xpos