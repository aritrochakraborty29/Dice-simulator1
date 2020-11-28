# importing module
import random
import pygame as pg


class Button():
    def __init__(self, x, y, pos, width, height):
        # Initializing the Display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = pos
        
    def clicked(self, pos):
        # Adding the clicking function
        self.pos = pg.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
        return False


class rpsGame():
    def __init__(self):
        # Setting the window screen
        pg.init()

        self.screen = pg.display.set_mode((960, 640))
        # Title
        pg.display.set_caption("Rock Paper Scissors")

        # Image
        self.bg = pg.image.load("img/background.jpg")
        self.r_btn = pg.image.load("img/r_button.png").convert_alpha()
        self.p_btn = pg.image.load("img/p_button.png").convert_alpha()
        self.s_btn = pg.image.load("img/s_button.png").convert_alpha()

        self.choose_rock = pg.image.load("img/rock.png").convert_alpha()
        self.choose_paper = pg.image.load("img/paper.png").convert_alpha()
        self.choose_scissors = pg.image.load("img/scissors.png").convert_alpha()

        self.font = pg.font.Font(('img/Splatch.ttf'), 90)
        self.text = self.font.render(f" ", True, (255, 255, 255))
        
        # Image position
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.r_btn, (20, 500))
        self.screen.blit(self.p_btn, (330, 500))
        self.screen.blit(self.s_btn, (640, 500))

        self.rock_btn = Button(30, 520, (30, 520), 300, 140)
        self.paper_btn = Button(340, 520, (340, 520), 300, 140)
        self.scissors_btn = Button(640, 520, (640, 520), 300, 140)

        # Initiating SCORE
        self.pl_score = 0
        self.pc_score = 0


    def player(self):
        # Addinng functionality for player
        if self.rock_btn.clicked(30):
            self.p_option = "rock"
            self.screen.blit(self.choose_rock, (120, 200))
        elif self.paper_btn.clicked(340):
            self.p_option = "paper"
            self.screen.blit(self.choose_paper, (120, 200))
        else:
            self.scissors_btn.clicked(640)
            self.p_option = "scissors"
            self.screen.blit(self.choose_scissors, (120, 200))

        return self.p_option

    def computer(self):
        # Function performed by PC
        self.pc_random_choice = " "
        option = ["rock", "paper", "scissors"]
        pc_choice = random.choice(list(option))
        if pc_choice == "rock":
            self.pc_random_choice = "rock"
            pc_choice = self.choose_rock
        elif pc_choice == "paper":
            self.pc_random_choice = "paper"
            pc_choice = self.choose_paper
        else:
            self.pc_random_choice = "scissors"
            pc_choice = self.choose_scissors
        pc_option = self.screen.blit(pc_choice, (600, 200))
        return pc_option

    def pl_score_cache(self):
        # Scoring FOR player

        self.pl_score = 0
        self.pc_score = 0
        
        pl = self.p_option
        pc = self.pc_random_choice
        if pl == "rock" and pc == "paper" or pl == "paper" and pc == "scissors" or pl == "scissors" and pc == "rock":
            self.pc_score += 1
        elif pl == pc:
            pass
        else:
            self.pl_score += 1
        return self.pl_score

    def pc_score_cache(self):
        # Scoring for PC

        self.pl_score = 0
        self.pc_score = 0
        
        pl = self.p_option
        pc = self.pc_random_choice

        if pl == "rock" and pc == "paper" or pl == "paper" and pc == "scissors" or pl == "scissors" and pc == "rock":
            self.pc_score += 1
        elif pl == pc:
            pass
        else:
            self.pl_score += 1

        return self.pc_score
        

    def image_reset(self):
        # Reseting the Image
        self.screen.blit(self.text, (330, 0))
        self.text = self.font.render(" ", True, (0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.r_btn, (20, 500))
        self.screen.blit(self.p_btn, (330, 500))
        self.screen.blit(self.s_btn, (640, 500))
        pass

    def game_loop(self):
        run = True
        clock = pg.time.Clock()
        rps_game = rpsGame()

        while run:
            # Updating the display
            pg.display.update()
            self.screen.blit(self.text, (330, 0))

            for event in pg.event.get():
                # For Exit
                if event.type == pg.QUIT:
                    run = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        run = False

                # Action Take Place
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.rock_btn.clicked(30)or self.paper_btn.clicked(340)or self.scissors_btn.clicked(640):
                        rps_game.image_reset()
                        rps_game.player()
                        rps_game.computer()

                        self.pl_score += rps_game.pl_score_cache()
                        self.pc_score += rps_game.pc_score_cache()
                        self.text = self.font.render(f"{self.pl_score}: {self.pc_score}", True, (255, 255, 255))

            pg.display.flip()
            clock.tick(30)

        pg.quit()
# game start 
if __name__ == '__main__':
    game = rpsGame()
    game.game_loop()





