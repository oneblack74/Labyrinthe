import pygame
import random
import time
from P_F import *

class Maze:

    def __init__(self, lig, col, t_case):
        pygame.init()
        self.__lig = lig
        self.__col = col
        self.__t_case = t_case
        self.__plateau = []
        self.__plateau = self.creer_plateau()


        pygame.display.set_mode((self.__col * self.__t_case, self.__lig * self.__t_case + self.__t_case + 65))
        self.__surface = pygame.display.get_surface()
        pygame.display.set_caption('Maze')
        self.__clock = pygame.time.Clock()
        self.__police = pygame.font.SysFont("monospace", 15)

        self.run()

    def draw_maze(self):
        for i, lig in enumerate(self.__plateau):
            for j, case in enumerate(lig):
                pygame.draw.rect(self.__surface, "white", [j * self.__t_case, i * self.__t_case, self.__t_case, self.__t_case])
                if case == -1:
                    pygame.draw.rect(self.__surface, "black", [j * self.__t_case, i * self.__t_case, self.__t_case, self.__t_case])
                if case == -5:
                    pygame.draw.rect(self.__surface, "grey", [j * self.__t_case, i * self.__t_case, self.__t_case, self.__t_case])

                if case == -4:
                    pygame.draw.rect(self.__surface, "yellow", [j * self.__t_case, i * self.__t_case, self.__t_case, self.__t_case])

                if case == -2:
                    pygame.draw.rect(self.__surface, "blue", [j * self.__t_case, i * self.__t_case, self.__t_case, self.__t_case])
                if case == -3:
                    pygame.draw.rect(self.__surface, "red", [j * self.__t_case, i * self.__t_case, self.__t_case, self.__t_case])
                if case == -6:
                    pygame.draw.rect(self.__surface, "black", [j * self.__t_case, i * self.__t_case, self.__t_case, self.__t_case])

    def coord_possible(self,i, j):
        if 0 <= i <= self.__lig - 1 and 0 <= j <= self.__col - 1:
            return True
        return False

# Maze 1 ===============================================================================================================
    def creer_ligne_mur(self):
        list = []
        for i in range(self.__col):
            list.append(-1)
        return list

    def creer_ligne(self):
        list = []
        list.append(-1)
        for i in range(self.__col // 2):
            list.append(0)
            list.append(-1)
        return list

    def creer_plateau(self):
        list = []
        list.append(self.creer_ligne_mur())
        for i in range(self.__lig // 2):
            list.append(self.creer_ligne())
            list.append(self.creer_ligne_mur())
        return list

    def creation_groupes(self):
        valeur = 1
        for i, lig in enumerate(self.__plateau):
            for j, case in enumerate(lig):
                if case == 0:
                    self.__plateau[i][j] = valeur
                    valeur += 1

    def creation_maze(self):

        while True:
            list_mur = []
            for i, lig in enumerate(self.__plateau):
                for j, case in enumerate(lig):
                    if case == -1 and i != 0 and i != self.__lig - 1 and j != 0 and j != self.__col - 1:
                        list_groupe = []
                        for new_case in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                            x = i + new_case[0]
                            y = j + new_case[1]
                            if self.coord_possible(x, y):
                                if self.__plateau[x][y] != -1 and self.__plateau[x][y] not in list_groupe:
                                    list_groupe.append(self.__plateau[x][y])
                        if len(list_groupe) == 2:
                            list_mur.append((i, j))

            if len(list_mur) == 0:
                break

            index = random.randint(0, len(list_mur) - 1)

            list_verif = []
            for new_case in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                i = list_mur[index][0] + new_case[0]
                j = list_mur[index][1] + new_case[1]
                if self.coord_possible(i, j):
                    if self.__plateau[i][j] != -1 and self.__plateau[i][j] not in list_verif:
                        list_verif.append(self.__plateau[i][j])

            a = list_verif[0]
            b = list_verif[1]
            if a < b:
                self.__plateau[list_mur[index][0]][list_mur[index][1]] = a
                new_groupe = a
            else:
                self.__plateau[list_mur[index][0]][list_mur[index][1]] = b
                new_groupe = b

            for i, lig in enumerate(self.__plateau):
                for j, case in enumerate(lig):
                    if case == b or case == a:
                        self.__plateau[i][j] = new_groupe
            self.draw_maze()
            pygame.display.update()

    def possible_sup(self, i, j):
        horizontale = True
        vertical = True
        for new_case in [(-1, 0), (1, 0)]:
            x = i + new_case[0]
            y = j + new_case[1]
            if self.coord_possible(x, y):
                if self.__plateau[x][y] == -1:
                    vertical = False

        for new_case in [(0, 1), (0, -1)]:
            x = i + new_case[0]
            y = j + new_case[1]
            if self.coord_possible(x, y):
                if self.__plateau[x][y] == -1:
                    horizontale = False
        return horizontale or vertical

    def supprimer_murs(self):
        list_mur = []
        for i, lig in enumerate(self.__plateau):
            for j, case in enumerate(lig):
                if case == -1 and i != 0 and i != self.__lig - 1 and j != 0 and j != self.__col - 1:
                    list_groupe = []
                    for new_case in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        x = i + new_case[0]
                        y = j + new_case[1]
                        if self.coord_possible(x, y):
                            if self.__plateau[x][y] == 1:
                                list_groupe.append(self.__plateau[x][y])
                    if len(list_groupe) == 2:
                        list_mur.append((i, j))
        if len(list_mur) != 0:
            for nb in range(self.__col // 10 + self.__lig // 10):
                index = random.randint(0, len(list_mur) - 1)

                while not self.possible_sup(list_mur[index][0], list_mur[index][1]):
                    index = random.randint(0, len(list_mur) - 1)
                self.__plateau[list_mur[index][0]][list_mur[index][1]] = 1
                list_mur.pop(index)


# Depart / Arrive ======================================================================================================
    def poser_depart_arriver(self):

        i = random.randint(1, self.__lig - 1)
        j = random.randint(1, self.__col - 1)
        while self.__plateau[i][j] != 1:
            i = random.randint(1, self.__lig - 1)
            j = random.randint(1, self.__col - 1)
        self.__plateau[i][j] = -2

        i = random.randint(1, self.__lig - 1)
        j = random.randint(1, self.__col - 1)
        while self.__plateau[i][j] != 1:
            i = random.randint(1, self.__lig - 1)
            j = random.randint(1, self.__col - 1)
        self.__plateau[i][j] = -3

    def preparation_plateau_pathfinding(self):
        for i, lig in enumerate(self.__plateau):
            for j, case in enumerate(lig):
                if case == -3:
                    self.__plateau[i][j] = 0
                if case == -2:
                    self.__plateau[i][j] = -2
                if case == -1:
                    self.__plateau[i][j] = -6
                if case == 1:
                    self.__plateau[i][j] = -5

    def creer_pathfinding(self):
        compteur = 0
        list = []
        for i, lig in enumerate(self.__plateau):
            for j, case in enumerate(lig):
                if case == 0:
                    list.append((i, j))
        while True:
            new_list = []
            for nb_case in list:
                for new_pos in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                    x = new_pos[0] + nb_case[0]
                    y = new_pos[1] + nb_case[1]
                    if self.coord_possible(x, y):
                        if self.__plateau[x][y] == -5:
                            new_list.append((x, y))
                            self.__plateau[x][y] = compteur + 1
                        if self.__plateau[x][y] == -2:
                            return
            compteur += 1
            list = new_list[:]
            self.draw_maze()
            pygame.display.update()

    def update_plateau(self):

        for i, lig in enumerate(self.__plateau):
            for j, case in enumerate(lig):
                if case == -6:
                    self.__plateau[i][j] = -1

    def resoudre_pathfinding(self):
        chemin = (0, 0)
        compteur = 0
        arriver = (0, 0)
        for i, lig in enumerate(self.__plateau):
            for j, case in enumerate(lig):
                if case == -2:
                    compteur_max = 0
                    for new_pos in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                        x = new_pos[0] + i
                        y = new_pos[1] + j
                        if self.coord_possible(x, y):
                            if self.__plateau[x][y] > compteur_max:
                                compteur_max = self.__plateau[x][y]
                    compteur = compteur_max + 1
                    chemin = (i, j)
                    self.__plateau[i][j] = -4
                if case == 0:
                    arriver = (i, j)
        while True:
            for new_pos in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                x = new_pos[0] + chemin[0]
                y = new_pos[1] + chemin[1]
                if self.coord_possible(x, y):
                    if self.__plateau[x][y] == compteur - 1 and self.__plateau[x][y] != -1:
                        compteur -= 1
                        self.__plateau[x][y] = -4
                        chemin = (x, y)
                        break
                    if self.__plateau[arriver[0]][arriver[1]] == -4:
                        return
            self.draw_maze()
            pygame.display.update()

    def plateau_base_deja_generer(self):
        for i, lig in enumerate(self.__plateau):
            for j, case in enumerate(lig):
                if case == -6 or case == -1:
                    self.__plateau[i][j] = -1
                else:
                    self.__plateau[i][j] = 1

    def generation_maze(self):
        self.__plateau = self.creer_plateau()
        self.creation_groupes()
        self.creation_maze()



    def pathfinding(self):
        self.preparation_plateau_pathfinding()
        self.creer_pathfinding()
        self.update_plateau()
        self.resoudre_pathfinding()

    def run(self):
        e_ready = False
        z_ready = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        pygame.draw.rect(self.__surface, "red", (0, self.__lig * self.__t_case, self.__col * self.__t_case, self.__t_case))
                        pygame.display.update()
                        self.generation_maze()
                        z_ready = True

                    if event.key == pygame.K_z and z_ready:
                        z_ready = True
                        self.plateau_base_deja_generer()
                        self.poser_depart_arriver()
                        e_ready = True

                    if event.key == pygame.K_e and e_ready:
                        e_ready = False
                        pygame.draw.rect(self.__surface, "red", (0, self.__lig * self.__t_case, self.__col * self.__t_case, self.__t_case))
                        pygame.display.update()
                        self.pathfinding()

            self.__surface.fill("black")
            self.draw_maze()
            text_a = self.__police.render("A : Reload le Labirynte", False, "white")
            text_z = self.__police.render("Z : Position début et fin", False, "white")
            text_e = self.__police.render("E : Pathfinding", False, "white")
            self.__surface.blit(text_a, (self.__t_case, self.__lig * self.__t_case + self.__t_case + 5))
            self.__surface.blit(text_z, (self.__t_case, self.__lig * self.__t_case + self.__t_case + 20))
            self.__surface.blit(text_e, (self.__t_case,self.__lig * self.__t_case + self.__t_case +  35))
            pygame.display.flip()

            pygame.display.update()
            self.__clock.tick(60)

        pygame.quit()
