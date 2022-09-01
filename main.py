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
    # main event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(main_surface, (0, 0))

        for i in range(n_disks):
            screen.blit(runner.disks[i], runner.disks_pos[i])

        # update our view
        pygame.display.update()

        # locking framerate to 30fps
        clock.tick(3)


class Hanoi():
    # list to hold all the disks
    disks = []

    # position of each disk
    disks_pos = []

    # length of smallest disk
    disk_length = 10

    # position of starting tower
    S_disk_x = 200
    T_disk_x = 400
    D_disk_x = 600

    # tracking the disks present in each tower
    S_disks, T_disks, D_disks = n_disks, 0, 0

    # to calculate the starting y position of disks on towers
    disk_y = 450 + (5 - n_disks) * 10

    # take a pygame.Surface object to draw on as the parameter
    def drawTowers(self, surface):
        # drawing the base and the three towers for the game
        pygame.draw.rect(surface, (0, 0, 0), (100, 500, 600, 10))
        pygame.draw.rect(surface, (0, 0, 0), (200, 250, 10, 250))
        pygame.draw.rect(surface, (0, 0, 0), (400, 250, 10, 250))
        pygame.draw.rect(surface, (0, 0, 0), (600, 250, 10, 250))

    # create the disk pygame.Surface objects and also set their initial position on screen
    def createDisks(self):
        # creating disk surfaces and adding them to a list
        for i in range(n_disks):
            disk = pygame.Surface((self.disk_length + i * 20, 10))
            disk.fill(colors[i])
            self.disks.append(disk)
            self.disks_pos.append([200 - i * 10, self.disk_y + i * 10])

    # takes the display, the source tower and the destination tower as the parameter
    def moveDisk(self, disk_num, source, dest):
        pos = [0, 0]

        if dest == 'S':
            if self.disks_pos[disk_num][0] <= 200:
                return
            pos[0] = self.S_disk_x - disk_num * 10
            pos[1] = 490 - self.S_disks * 10
            self.S_disks += 1
            if source == 'T':
                self.T_disks -= 1
            elif source == 'D':
                self.D_disks -= 1

        elif dest == 'T':
            if self.disks_pos[disk_num][0] <= 400 and self.disks_pos[disk_num][0] > 200:
                return
            pos[0] = self.T_disk_x - disk_num * 10
            pos[1] = 490 - self.T_disks * 10
            self.T_disks += 1
            if source == 'S':
                self.S_disks -= 1
            elif source == 'D':
                self.D_disks -= 1

        elif dest == 'D':
            if self.disks_pos[disk_num][0] <= 600 and self.disks_pos[disk_num][0] > 400:
                return
            pos[0] = self.D_disk_x - disk_num * 10
            pos[1] = 490 - self.D_disks * 10
            self.D_disks += 1
            if source == 'S':
                self.S_disks -= 1
            elif source == 'T':
                self.T_disks -= 1

        self.disks_pos[disk_num] = pos


def algorithm(num_disks, S, T, D):
    moves = []

main()