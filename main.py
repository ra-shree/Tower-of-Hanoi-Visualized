import pygame
from sys import exit
from time import sleep

# number of disks in the hanoi tower
n_disks = 7

# list to store all the moves from the tower of hanoi algorithm
moves = []

# RGB codes for red, blue, green, purple, yellow
colors = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 0, 255), (255, 255, 0)]

# recursive algorithm to find the order of moves in tower of hanoi with n disks


def towerOfHanoi(num_disks, S, T, D):
    if num_disks == -1:
        return
    towerOfHanoi(num_disks - 1, S, D, T)
    moves.append([num_disks, S, D])
    towerOfHanoi(num_disks - 1, T, S, D)


# function call to tower of hanoi algorithm
towerOfHanoi(n_disks - 1, 'S', 'T', 'D')

# main function
def main():

    # initialize pygame
    pygame.init()

    # size of display window
    screen = pygame.display.set_mode((800, 600))

    # changing the window name to 'Tower of Hanoi'
    pygame.display.set_caption('Tower of Hanoi')

    # adding a clock
    clock = pygame.time.Clock()

    # creating the main surface for drawing
    main_surface = pygame.Surface((800, 600))
    main_surface.fill('White')

    # creating object of Hanoi() class
    runner = Hanoi()
    runner.drawTowers(main_surface)
    runner.createDisks()

    n = 0
    # main event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # attaching the main surface to screen
        screen.blit(main_surface, (0, 0))

        # drawing all the disks initially and redrawing when their position changes
        for i in range(n_disks):
            screen.blit(runner.disks[i], runner.disks_pos[i])

        if (n < 2 ** n_disks - 1):
            # moving the disk to their next position according to the tower of hanoi algorithm
            runner.moveDisk(moves[n][0], moves[n][1], moves[n][2])

        # update our view
        pygame.display.update()
        n += 1

        # locking framerate to 2fps
        clock.tick(2)


class Hanoi(object):
    # list to hold all the disks
    disks = []

    # latest position of each disk
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
            disk.fill(colors[i % 5])
            self.disks.append(disk)
            self.disks_pos.append([200 - i * 10, self.disk_y + i * 10])

    # takes the disk number, the source tower and the destination tower as the parameter and change position of disk
    def moveDisk(self, disk_num, source, dest):
        # stores the calculated position of the destination
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

        # setting the position of the disk to the new position
        self.disks_pos[disk_num] = pos


if __name__ == '__main__':
    main()
