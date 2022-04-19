import pygame

pygame.init()

score = 0
textX = 10
textY = 10
font = pygame.font.Font('freesansbold.ttf', 16)

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('Сквош')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

paddle = pygame.image.load('paddle.png')
posX = 348
posY = 556
changeX = 0

ball = pygame.image.load('ball.png')
ballX = 368
ballY = 556
changeBallX = 0
changeBallY = 0
play = 0

def player(x,y):
    screen.blit(paddle, (x,y))

def seeball(x,y):
    screen.blit(ball, (x,y))

def show_score(x,y):
    view_score = font.render('Счет ' + str(score), True, (255,255,255))
    screen.blit(view_score, (x,y))

run = True
while run:
    screen.fill((0, 0, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -1
                if play == 0:
                    changeBallX = -1

            elif event.key == pygame.K_RIGHT:
                changeX = 1
                if play == 0:
                    changeBallX = 1
            if event.key == pygame.K_SPACE:
                changeBallX = 1
                changeBallY = -1
                play = 1

        if event.type == pygame.KEYUP:
            changeX = 0
            if play == 0:
                changeBallX = 0

    ballX += changeBallX
    ballY += changeBallY

    if play == 1:
        if ballX >= 776:
            changeBallX = -1
        elif ballX <= 0:
            changeBallX = 1
    else:
        if ballX == 776 or ballX == 0:
            changeBallX = 0

    if ballY ==0:
        changeBallY = 1

    if play == 1:
        if ballY == 556:
            if posX-22 < ballX < posX+64:
                changeBallY = -1
                score += 1

    seeball(ballX, ballY)

    show_score(textX, textY)

    posX += changeX

    if posX <= 0:
        posX = 0
    elif posX >= 734:
        posX = 734

    player(posX, posY)

    pygame.display.update()





