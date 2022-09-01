import pygame
from sys import exit
from time import sleep

# number of disks in the hanoi tower
n_disks = 5
# red, blue, green, purple, yellow
colors = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 0, 255), (255, 255, 0)]
def main():

    # initialize pygame
    pygame.init()

    # size of display window
    screen = pygame.display.set_mode((800, 600))

    # changing the window name to 'Tower of Hanoi'
    pygame.display.set_caption('Tower of Hanoi')

    # adding a clock
    clock = pygame.time.Clock()

    # creating a surface to draw on
    main_surface = pygame.Surface((800, 600))
    main_surface.fill('White')


    runner = Hanoi()
    runner.drawTowers(main_surface)
    runner.createDisks()
    disk_surface = pygame.Surface((90, 10))
    # main event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(main_surface, (0, 0))
        runner.drawDisks(screen)

        # update our view
        pygame.display.update()

        # locking framerate to 30fps
        clock.tick(60)


class Hanoi():
    # list to hold all the disks
    disks = []

    # length of smallest disk
    disk_length = 10

    # position of starting tower
    disk_x = 200

    # to calculate the starting y position of disks on towers
    disk_y = 450 + (5 - n_disks) * 10

    # take a pygame.Surface object to draw on as the parameter
    def drawTowers(self, surface):
        # drawing the base and the three towers for the game
        pygame.draw.rect(surface, (0, 0, 0), (100, 500, 600, 10))
        pygame.draw.rect(surface, (0, 0, 0), (200, 250, 10, 250))
        pygame.draw.rect(surface, (0, 0, 0), (400, 250, 10, 250))
        pygame.draw.rect(surface, (0, 0, 0), (600, 250, 10, 250))

    # create the disk pygame.Surface objects
    def createDisks(self):
        # creating disk surfaces and adding them to a list
        for i in range(n_disks):
            disk = pygame.Surface((self.disk_length + i * 20, 10))
            disk.fill(colors[i])
            self.disks.append(disk)

    # take a pygame.Display as a parameter to draw the disk surfaces on
    def drawDisks(self, display):
        # displaying each surface in the disks list
        for i in range(n_disks):
            display.blit(self.disks[i], (self.disk_x - i * 10, self.disk_y + i * 10))
main()