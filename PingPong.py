import arcade
import random
import tkinter as tk
from tkinter import messagebox    

tk.Tk().withdraw() # to avoid showing the root window


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ping Pong"
SPEED_X = random.randint(3, 6)
SPEED_Y = random.randint(3, 6)
WINNER = 20
x = arcade.load_sound("end.mp3")
x2 = arcade.load_sound("crying.mp3")
x3 = arcade.load_sound("end2.mp3")
x4 = arcade.load_sound("end3.mp3")
x5 = arcade.load_sound("end4.mp3")
x6 = arcade.load_sound("end5.mp3")
x7 = arcade.load_sound("end6.mp3")
x8 = arcade.load_sound("N1 (1).mp3")
x9 = arcade.load_sound("N1 (2).mp3")
x10 = arcade.load_sound("N1 (3).mp3")

class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > SCREEN_WIDTH or self.left < 0:
            self.change_x = -self.change_x
        self.center_y += self.change_y
        if self.top > SCREEN_HEIGHT or self.bottom < 0:
            self.change_y = -self.change_y


class Bar(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > SCREEN_WIDTH or self.left < 0:
            self.change_x = 0


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball("ball.png", 0.1)
        self.bar = Bar("bar.png", 0.08)
        self.setup()
        self.score = 0
        self.attempts = 1
        self.game = True

    def setup(self):
        self.ball.center_x = SCREEN_WIDTH/2
        self.ball.center_y = SCREEN_HEIGHT/2
        self.direction = random.randint(1, 2)
        if self.direction < 2:
            self.ball.change_x = -SPEED_X
        else:
            self.ball.change_x = SPEED_X
        self.ball.change_y = SPEED_Y
        self.bar.center_x = SCREEN_WIDTH/2

    def on_draw(self):
        # if you have an error inside clear function we can use
        # self.background_color = (x,x,x)
        # self.clear()
        self.clear((25, 0, 51))
        self.ball.draw()
        self.bar.draw()
        arcade.draw_text(f"Score: {self.score}", 20,
                         SCREEN_HEIGHT - 30, (255, 255, 255), 20)
        arcade.draw_text(f"Attempts: {self.attempts}",
                         20, SCREEN_HEIGHT - 60, (30, 140, 50), 20)
        arcade.draw_text(f"X Factor Speed: {SPEED_X}",
                         20, SCREEN_HEIGHT - 80, (0, 128, 255), 10)
        arcade.draw_text(f"Y Factor Speed: {SPEED_Y}",
                         20, SCREEN_HEIGHT - 95, (0, 128, 255), 10)
        if self.attempts == 0:
            arcade.draw_text(f"You Have Lost :(", SCREEN_WIDTH /
                             2-150, SCREEN_HEIGHT/2, (255, 0, 0), 30)
            while True:
                arcade.play_sound(x, 1)
                arcade.play_sound(x2, 1)
                arcade.play_sound(x3, 1)
                arcade.play_sound(x4, 1)
                arcade.play_sound(x5, 1.3)
                arcade.play_sound(x6, 1)
                arcade.play_sound(x7, 1)
                arcade.play_sound(x8, 1)
                arcade.play_sound(x9, 3)
                arcade.play_sound(x10, 1)
                messagebox.showinfo(
                    title="VIRUS",
                    message="LOSER VIRUS, KEEP CLICKING 50 CLICKS AND YOUR FREE :)")
            self.game = False
        if self.score == WINNER:
            arcade.draw_text(f"You Have Won :D", SCREEN_WIDTH /
                             2-150, SCREEN_HEIGHT/2, (255, 0, 0), 30)
            self.game = False

    def update(self, delta_time):
        self.ball.update()
        self.bar.update()
        if arcade.check_for_collision(self.ball, self.bar):
            # self.ball.bottom = self.bar.top, to fix if the ball is going inside the bar
            self.ball.change_y = -self.ball.change_y
            self.score += 1
            if self.ball.change_x > 0:
                self.ball.change_x += 1
            if self.ball.change_x < 0:
                self.ball.change_y -= 1
        if self.ball.bottom < 0:
            self.attempts -= 1
            self.setup()
        if self.attempts == 0:
            self.ball.stop()
            self.bar.stop()
        if self.score == WINNER:
            self.ball.stop()
            self.bar.stop()
            self.setup()

    def on_key_press(self, key, modifiers):
        if self.game:
            if key == arcade.key.LEFT:
                self.bar.change_x = -SPEED_X
            if key == arcade.key.RIGHT:
                self.bar.change_x = SPEED_X

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)


arcade.run()
