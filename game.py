import pygame, sys


pygame.init()

WIDTH, HEIGHT = 960, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

clock = pygame.time.Clock()

class Button:
    def __init__(self, x, y):

        self.imageisblank = True

        if self.imageisblank:
            self.image = pygame.Surface((250, 225))
            self.image.fill((255, 255, 255))

        self.shadimage = self.image.copy()
        self.shadimage.fill((128, 128, 128))

        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

        self.bpos = (x, y - 20)

        self.mouse = False
        self.clicked = False
        

    def image_change(self, image):
        self.image = image

        self.fadeimage = image.copy()
        self.fadeimage.fill((255, 255, 255, 155), special_flags=pygame.BLEND_RGBA_MULT)
        self.imageisblank = False

    def draw(self):

        if self.mouse and self.imageisblank:
            screen.blit(self.shadimage, self.bpos)


        else:
            screen.blit(self.image, self.bpos)
            
    def interaction_check(self):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.mouse = True
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True

        else:
            self.mouse = False

        return self.clicked
    

class TicTacToe:
    def __init__(self):



        self.Ximg = pygame.image.load('Assets/Xmark.png')
        self.Ximg = pygame.transform.scale(self.Ximg, (250 , 250))

        self.Oimg = pygame.image.load('Assets/Omark.png')
        self.Oimg = pygame.transform.scale(self.Oimg, (250 , 250))

        self.game_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.button_list = []

        self.initialize_buttons()

        self.turn = 1

    def initialize_board(self):

        # for num in range (2):
        #     pygame.draw.line(screen, (0, 0, 0), ((WIDTH//2 - 125) + 250 * num, 50), ((WIDTH//2 - 125) + 250 * num, HEIGHT - 50))# |
        #     pygame.draw.line(screen, (0, 0, 0), (175, (HEIGHT//2 - 125) + 250 * num), (WIDTH - 175, (HEIGHT//2 - 125) + 250 * num))# --

        board_size = min(WIDTH, HEIGHT) - 40
        line_width = 10
        cell_size = board_size // 3

        # Calculate board position
        board_x = (WIDTH - board_size) // 2
        board_y = (HEIGHT - board_size) // 2

        # Draw the vertical and horizontal lines
        for i in range(1, 3):
            # Vertical lines
            pygame.draw.line(screen, (0, 0, 0), (board_x + i * cell_size, board_y), (board_x + i * cell_size, board_y + board_size), line_width)
            # Horizontal lines
            pygame.draw.line(screen, (0, 0, 0), (board_x, board_y + i * cell_size), (board_x + board_size, board_y + i * cell_size), line_width)



    def initialize_buttons(self):

        for num in range(len(self.game_board)):
            self.button_list.append(Button(100 + 250 * (num % 3), 50 + int(num/3) * 225))

    def determine_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]

        for combination in winning_combinations:
            if self.game_board[combination[0]] == self.game_board[combination[1]] == self.game_board[combination[2]] != 0:
                return self.game_board[combination[0]]  # Return the player (1 or 2) who won

        return None  # Return None if there is no winner


        


game = TicTacToe()

ingame = True
ending = False
winner = None

Rungame = True
while Rungame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))


    if ingame:

        

        for index, button in enumerate(game.button_list):
            button.draw()
            clicked_button = button.interaction_check()

            if clicked_button and game.game_board[index] == 0:
                
                if game.turn == 1:
                    button.image_change(game.Ximg)
                    game.turn = 2

                else:
                    button.image_change(game.Oimg)
                    game.turn = 1

                game.game_board[index] = game.turn
                
        game.initialize_board()

        winner = game.determine_winner()

        if winner != None:
            ingame = False
            ending = True

    if ending:
        if winner == 1:
            print('winner is player O')

        else:
            print('winner is player X')

        Rungame = False


    pygame.display.update()
    clock.tick(32)




