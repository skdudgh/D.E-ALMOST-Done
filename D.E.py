import ED2
import ED2
import pygame
import os
import time
pygame.init()

screen_width = 1000
screen_height = 600
caption = "E.D"
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(caption)

WHITE = pygame.Color("#FFFFFF")
BLACK = pygame.Color("#000000")
BLUE = pygame.Color("#0000FF")
RED = pygame.Color("#FF0000")
GREEN = pygame.Color("#00FF00")
PALE_GREEN = pygame.Color("#98FB98")
YELLOW = pygame.Color("#FFFF00")

#image
path = os.path.dirname(__file__)
image = os.path.join(path, "image")
button = os.path.join(path, "button")
information = os.path.join(path, "information")

background = pygame.image.load(os.path.join(image, 'galaxy.png'))
background = pygame.transform.scale(background, (screen_width, screen_height))

enc_background = pygame.image.load(os.path.join(image, 'encryption.png'))
enc_background = pygame.transform.scale(enc_background, (screen_width, screen_height))

dec_background = pygame.image.load(os.path.join(image, 'decryption.png'))
dec_background = pygame.transform.scale(dec_background, (screen_width, screen_height))

lock1 = pygame.image.load(os.path.join(image, 'lock1.png'))
lock1 = pygame.transform.scale(lock1, (100, 100))
pygame.display.set_icon(lock1)

lock2 = pygame.image.load(os.path.join(image, 'lock2.png'))
lock2 = pygame.transform.scale(lock2, (125, 150))
lock2_rect = lock2.get_rect()
lock2_size = lock2.get_size()
lock2_x = (screen_width / 2) - (lock2.get_width() / 2)
lock2_y = (screen_height / 5) - (lock2.get_height() / 2)

Original_blue = pygame.image.load(os.path.join(button, 'blue.png'))
blue = pygame.transform.scale(Original_blue, (400, 100))
blue_rect = blue.get_rect()
blue_size= blue.get_size()
blue_x = (screen_width / 4) - (blue.get_width() / 2)
blue_y = (screen_height / 2) - (blue.get_height() / 2)

Original_orange = pygame.image.load(os.path.join(button, 'orange.png'))
orange = pygame.transform.scale(Original_orange, (400, 100))
orange_rect = orange.get_rect()
orange_size= orange.get_size()
orange_x = (screen_width / 1.32) - (orange.get_width() / 2)
orange_y = (screen_height / 2) - (orange.get_height() / 2)

Original_green = pygame.image.load(os.path.join(button, 'green.png'))
green = pygame.transform.scale(Original_green, (400, 100))
green_rect = green.get_rect()
green_size= green.get_size()
green_x = (screen_width / 2) - (green.get_width() / 2)
green_y = (screen_height / 1.5) - (green.get_height() / 2)

Original_pink = pygame.image.load(os.path.join(button, 'pink.png'))
pink = pygame.transform.scale(Original_pink, (400, 100))
pink_rect = pink.get_rect()
pink_size= pink.get_size()
pink_x = (screen_width / 2) - (pink.get_width() / 2)
pink_y = (screen_height / 1.5) - (pink.get_height() / 2)

Original_redC = pygame.image.load(os.path.join(button, 'red(gold).png'))
redC = pygame.transform.scale(Original_redC, (200, 200))
redC_rect = redC.get_rect()
redC_size= redC.get_size()
redC_x = (screen_width / 2) - (redC.get_width() / 2)
redC_y = (screen_height / 1.32) - (redC.get_height() / 2)

Original_textImg = pygame.image.load(os.path.join(image, 'textImg.png'))
textImg = pygame.transform.scale(Original_textImg, (65, 75))
textImg_rect = textImg.get_rect()
textImg_size= textImg.get_size()
textImg_x = (blue_x + (blue.get_width() / 2)) - (textImg.get_width() / 2)
textImg_y = (blue_y + (blue.get_height() / 2)) - (textImg.get_height() / 2)

Original_textImg2 = pygame.image.load(os.path.join(image, 'textImg2.png'))
textImg2 = pygame.transform.scale(Original_textImg2, (65, 75))
textImg2_rect = textImg2.get_rect()
textImg2_size= textImg2.get_size()
textImg2_x = (orange_x + (orange.get_width() / 2)) - (textImg2.get_width() / 2)
textImg2_y = (orange_y + (orange.get_height() / 2)) - (textImg2.get_height() / 2)

Original_textImg_E = pygame.image.load(os.path.join(image, 'textImg_Encrypt.png'))
textImg_E = pygame.transform.scale(Original_textImg_E, (65, 75))
textImg_E_rect = textImg_E.get_rect()
textImg_E_size= textImg_E.get_size()
textImg_E_x = (blue_x + (blue.get_width() / 2)) - (textImg_E.get_width() / 2)
textImg_E_y = (blue_y + (blue.get_height() / 2)) - (textImg_E.get_height() / 2)

Original_textImg2_D = pygame.image.load(os.path.join(image, 'textImg2_Decrypt.png'))
textImg2_D = pygame.transform.scale(Original_textImg2_D, (65, 75))
textImg2_D_rect = textImg2_D.get_rect()
textImg2_D_size= textImg2_D.get_size()
textImg2_D_x = (pink_x + (pink.get_width() / 2)) - (textImg2_D.get_width() / 2)
textImg2_D_y = (pink_y + (pink.get_height() / 2)) - (textImg2_D.get_height() / 2)

#text
font = pygame.font.SysFont(None, 50)
font_small = pygame.font.SysFont(None, 30, bold=False, italic=True)

encryption = font.render("Encryption", True, YELLOW)
encryption_rect = encryption.get_rect()
encryption_size = encryption.get_size()
encryption_x = (blue_x + (blue.get_width() / 2)) - (encryption.get_width() / 2)
encryption_y = (blue_y + (blue.get_height() / 2)) - (encryption.get_height() / 2)

decryption = font.render("Decryption", True, BLUE)
decryption_rect = decryption.get_rect()
decryption_size = decryption.get_size()
decryption_x = (orange_x + (orange.get_width() / 2)) - (decryption.get_width() / 2)
decryption_y = (orange_y + (orange.get_height() / 2)) - (decryption.get_height() / 2)

MadeBy = font_small.render("Made by: Na Yeong Ho", True, GREEN)

message = os.path.join(information, "ED.txt")

enc_file = os.path.join(information, "ED.txt")

info = font.render("Info", True, PALE_GREEN)
info_rect = info.get_rect()
info_size = info.get_size()
info_x = (redC_x + (redC.get_width() / 2)) - (info.get_width() / 2)
info_y = (redC_y + (redC.get_height() / 2)) - (info.get_height() / 2)

main = True
enc = False
dec = False

blank = ""

active = False
openfile = False

def original():
    global blue, blue_x, blue_y, green, green_x, green_y, orange, orange_x, orange_y, pink, pink_x, pink_y
    blue = pygame.transform.scale(Original_blue, (400, 100))
    green = pygame.transform.scale(Original_green, (400, 100))
    orange = pygame.transform.scale(Original_orange, (400, 100))
    pink = pygame.transform.scale(Original_pink, (400, 100))

    blue_x = (screen_width / 4) - (blue.get_width() / 2)
    blue_y = (screen_height / 2) - (blue.get_height() / 2)
    green_x = (screen_width / 2) - (green.get_width() / 2)
    green_y = (screen_height / 1.5) - (green.get_height() / 2)
    orange_x = (screen_width / 1.32) - (orange.get_width() / 2)
    orange_y = (screen_height / 2) - (orange.get_height() / 2)
    pink_x = (screen_width / 2) - (pink.get_width() / 2)
    pink_y = (screen_height / 1.5) - (pink.get_height() / 2)

def clear():
    global background1, lock2, lock2_x, lock2_y, Original_blue, blue, blue_x, blue_y, Original_orange, orange, orange_x, orange_y, decryption, decryption_x, decryption_y, encryption, encryption_x, encryption_y, redC, redC_x, redC_y
    original()
    screen.blit(background, (0, 0))
    screen.blit(lock2, (lock2_x, lock2_y))
    blue = pygame.transform.scale(Original_blue, (400, 100))
    screen.blit(blue, (blue_x, blue_y))
    orange = pygame.transform.scale(Original_orange, (400, 100))
    screen.blit(orange, (orange_x, orange_y))
    screen.blit(decryption, (decryption_x, decryption_y))
    screen.blit(encryption, (encryption_x, encryption_y))
    screen.blit(MadeBy, (screen_width - MadeBy.get_width() - 10, screen_height - MadeBy.get_height() - 25))
    screen.blit(redC, (redC_x, redC_y))
    screen.blit(info, (info_x, info_y))

def encrypt():
    global Original_blue, blue, blue_x, blue_y, Original_green, green, green_x, green_y, textImg, textImg_x, textImg_y, textImg_E, textImg_E_x, textImg_E_y
    screen.blit(enc_background, (0, 0))
    blue = pygame.transform.scale(Original_blue, (200, 100))
    blue_x, blue_y = 20, 20
    textImg_x = (blue_x + (blue.get_width() / 2)) - (textImg.get_width() / 2)
    textImg_y = (blue_y + (blue.get_height() / 2)) - (textImg.get_height() / 2)
    green = pygame.transform.scale(Original_green, (200, 100))
    green_x, green_y = 20, (blue_y + blue.get_height()) + 80
    textImg_E_x = (green_x + (green.get_width() / 2)) - (textImg_E.get_width() / 2)
    textImg_E_y = (green_y + (green.get_height() / 2)) - (textImg_E.get_height() / 2)
    screen.blit(blue, (blue_x, blue_y))
    screen.blit(textImg, (textImg_x, textImg_y))
    screen.blit(green, (green_x, green_y))
    screen.blit(textImg_E, (textImg_E_x, textImg_E_y))

def decrypt():
    global Original_orange, orange, orange_x, orange_y, Original_pink, pink, pink_x, pink_y, textImg2, textImg2_x, textImg2_y, textImg2_D, textImg2_D_x, textImg2_D_y
    screen.blit(dec_background, (0, 0))
    orange = pygame.transform.scale(Original_orange, (200, 100))
    textImg2_x = (orange_x + (orange.get_width() / 2)) - (textImg2.get_width() / 2)
    textImg2_y = (orange_y + (orange.get_height() / 2)) - (textImg2.get_height() / 2)
    orange_x, orange_y = 20, 20
    pink = pygame.transform.scale(Original_pink, (200, 100))
    pink_x, pink_y = 20, (orange_y + orange.get_height()) + 80
    textImg2_D_x = (pink_x + (pink.get_width() / 2)) - (textImg2_D.get_width() / 2)
    textImg2_D_y = (pink_y + (pink.get_height() / 2)) - (textImg2_D.get_height() / 2)
    screen.blit(orange, (orange_x, orange_y))
    screen.blit(textImg2, (textImg2_x, textImg2_y))
    screen.blit(pink, (pink_x, pink_y))
    screen.blit(textImg2_D, (textImg2_D_x, textImg2_D_y))

mouse_x, mouse_y = pygame.mouse.get_pos()
openfile = False

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if event.button == 1:
                if main  == True and enc == False and dec == False:
                    if (blue_x <= mouse_x <= blue_x + blue.get_width()) and (blue_y <= mouse_y <= blue_y + blue.get_height()):
                        main = False
                        dec = False
                        enc = True
                        screen.fill(BLACK)
                        print("Encryption")
                    if (orange_x <= mouse_x <= orange_x + orange.get_width()) and (orange_y <= mouse_y <= orange_y + orange.get_height()):
                        main = False
                        enc = False
                        dec = True
                        screen.fill(BLACK)
                        print("Decryption")
                    if (redC_x <= mouse_x <= redC_x + redC.get_width()) and (redC_y <= mouse_y <= redC_y + redC.get_height()):
                        print("Information")
                        os.startfile(os.path.join(information, "info.pdf"))
            
            if event.button == 1:
                if enc:
                    if (textImg_x <= mouse_x <= textImg_x + textImg.get_width()) and (textImg_y <= mouse_y <= textImg_y + textImg.get_height()):
                        openfile = True
                        print("Encryption button clicked")
                    if (textImg_E_x <= mouse_x <= textImg_E_x + textImg_E.get_width()) and (textImg_E_y <= mouse_y <= textImg_E_y + textImg_E.get_height()):
                        ED2.encrypt()
                        os.startfile(os.path.join(information, "ED.txt"))

            if event.button == 1:
                if dec:
                    if (textImg2_x <= mouse_x <= textImg2_x + textImg2.get_width()) and (textImg2_y <= mouse_y <= textImg2_y + textImg2.get_height()):
                        print("Decryption button clicked")
                        os.startfile(os.path.join(information, "ED.txt"))
                    if (textImg2_D_x <= mouse_x <= textImg2_D_x + textImg2_D.get_width()) and (textImg2_D_y <= mouse_y <= textImg2_D_y + textImg2_D.get_height()):
                        ED2.decrypt()
                        os.startfile(os.path.join(information, "ED.txt"))

        if openfile:
            os.startfile(os.path.join(information, "ED.txt"))
            with open(os.path.join(information, "ED.txt"), 'w', encoding='utf-8') as file:
                file.write(blank)
            openfile = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if enc == True and main == False and dec == False:
                    original()
                    enc, main = False, True
                if dec == True and main == False and enc == False:
                    original()
                    dec, main = False, True
                screen.fill(BLACK)

    if main == True and enc == False and dec == False:
        clear()

    if enc == True and main == False and dec == False:
        encrypt()

    if dec == True and main == False and enc == False:
        decrypt()

    pygame.display.update()
pygame.quit()