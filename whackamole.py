import pygame
import random
#testpyyh

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        px = 0
        py = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(px, py)))
            for x1 in range (0, 641, 32):
                pygame.draw.line(screen, "black", (x1, 0), (x1, 512))
            for y1 in range (0, 513, 32):
                pygame.draw.line(screen, "black", (0, y1), (640, y1))
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x in range(0+px,33+px) and y in range (0+py, 33+py):
                    print("gotcha!")
                    px = random.randrange(0,640, 32)
                    py = random.randrange(0,512, 32)


            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
