from turtle import Turtle, Screen


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        self.goto(x=0, y=250)
        self.write(arg=f'Score: {self.score}', move=False, align='center', font=('Courier', 20, 'normal'))

    def refresh(self):
        self.clear()
        self.write(arg=f'Score: {self.score}', move=False, align='center', font=('Courier', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.screen.bgcolor('red')
        self.write(arg=f'GAME OVER', move=False, align='center', font=('Courier', 30, 'normal'))
