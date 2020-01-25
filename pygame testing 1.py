import pygame
pygame.init()

win = pygame.display.set_mode((500,490))
pygame.display.set_caption("First Game")
walkRight = pygame.image.load('C:\\python\\pygame\\GAME SPRITES\\pixil-frame-0.png')
walkLeft = pygame.image.load('C:\\python\\pygame\\GAME SPRITES\\pixil-frame-0.png')
bg = pygame.image.load('C:\\python\\pygame\\GAME SPRITES\\bg.jpg')
char = pygame.image.load('C:\\python\\pygame\\GAME SPRITES\\pixil-frame-0.png')

clock = pygame.time.Clock()
x= 50
y = 380
width = 64
height = 64
vel = 5
isJump = False
jumpCount = 10
left= False
right = False
walkCount = 0
def reDrawGameWindow():
    global walkCount
    win.blit(bg, (0,10))

    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft, (x, y))
        walkCount+= 1
    elif right:
        win.blit(walkLeft, (x, y))
        walkCount+= 1
    else:
        win.blit(char, (x, y))
    pygame.display.update()
    
def scene2(walkCount, x):
    print("here")
    x -= vel
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and x > vel: 
        x -= vel
        left= True
        right = False
    elif keys[pygame.K_d] and x < 500 - vel - width:  
        x += vel
        left= False
        right = True
        if x == 435:
            scene2(walkCount, x)
    else:
        right = False
        left = False
        walkCount = 0 
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0 
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.1
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
    
    reDrawGameWindow()
pygame.quit()

































