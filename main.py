import pygame
from sys import exit
from time import sleep
n_disks = 5

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

    # creating another transparent surface for the disks
    disk_surface = pygame.Surface((800, 600), pygame.SRCALPHA, 32)
    disk_surface = disk_surface.convert_alpha()
    # initializing main class
    runner = Hanoi()


    # runner.drawDisk(disk_surface, 5, 'D')
    # main event loop
    n = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        runner.drawTowers(main_surface)
        runner.drawDisk(main_surface, 3, 'S')
        sleep(2)
        main_surface.fill('White')
        screen.blit(main_surface, (0, 0))
        screen.blit(disk_surface, (0, 0))
        # update our view
        pygame.display.update()

        # locking framerate to 30fps
        clock.tick(60)


class Hanoi():
    S = (200, 250, 10, 250)
    T = (400, 250, 10, 250)
    D = (600, 250, 10, 250)
    base = (100, 500, 600, 10)
    def drawTowers(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.base)
        pygame.draw.rect(surface, (0, 0, 0), self.S)
        pygame.draw.rect(surface, (0, 0, 0), self.T)
        pygame.draw.rect(surface, (0, 0, 0), self.D)

    def drawDisk(self, surface, disk_num, position):
        disk_length = 90
        disk_thicc = 10
        disk_x = 160
        disk_y = 490

        # select the tower where the peg is to be drawn
        if position == 'S':
            disk_x = 160
        elif position == 'T':
            disk_x = 360
        elif position == 'D':
            disk_x = 560

        disk_x += (disk_num - 1) * 10
        disk_y -= (disk_num - 1) * 10
        disk_length -= (disk_num - 1) * 20

        # creating the tuple with position data of the disk
        disk_pos = (disk_x, disk_y, disk_length, disk_thicc)

        if disk_num == 1:
            pygame.draw.rect(surface, 'Green', disk_pos, 0, 1)
        elif disk_num == 2:
            pygame.draw.rect(surface, 'Yellow', disk_pos, 0, 1)
        elif disk_num == 3:
            pygame.draw.rect(surface, 'Purple', disk_pos, 0, 1)
        elif disk_num == 4:
            pygame.draw.rect(surface, 'Red', disk_pos, 0, 1)
        elif disk_num == 5:
            pygame.draw.rect(surface, 'Blue', disk_pos, 0, 1)


main()