import tkinter
from maze import Maze

class Menu:
    def __init__(self):

        fenetre = tkinter.Tk()
        fenetre.title("Maze")

        self.__current_value_hauteur = tkinter.IntVar()
        scale_hauteur = tkinter.Scale(fenetre, orient='horizontal', from_=21, to=151,
                                    resolution=2, tickinterval=10, length=500,
                                    label='Hauteur :', variable=self.__current_value_hauteur)
        scale_hauteur.pack()

        self.__current_value_largeur = tkinter.IntVar()
        scale_largeur = tkinter.Scale(fenetre, orient='horizontal', from_=21, to=151,
                                  resolution=2, tickinterval=10, length=500,
                                  label='Largeur :', variable=self.__current_value_largeur)
        scale_largeur.pack()

        self.__current_value_taille = tkinter.IntVar()
        scale_taille = tkinter.Scale(fenetre, orient='horizontal', from_=1, to=30,
                                  resolution=1, tickinterval=5, length=500,
                                  label="Taille d'une case :", variable=self.__current_value_taille)
        scale_taille.pack()

        """self.__current_type_g = tkinter.IntVar()
        scale_type_g = tkinter.Scale(fenetre, orient='horizontal', from_=1, to=2,
                                     resolution=1, tickinterval=1, length=500,
                                     label="Type de génération :", variable=self.__current_type_g)
        scale_type_g.pack()

        self.__current_type_p = tkinter.IntVar()
        scale_type_p = tkinter.Scale(fenetre, orient='horizontal', from_=1, to=2,
                                     resolution=1, tickinterval=1, length=500,
                                     label="Type de pathfinding :", variable=self.__current_type_p)
        scale_type_p.pack()"""

        btn_lancer = tkinter.Button(fenetre, text="Lancer",command=self.lancer_partie)
        btn_lancer.pack()


        fenetre.mainloop()

    def lancer_partie(self):
        play = Maze(self.__current_value_hauteur.get(),self.__current_value_largeur.get(),self.__current_value_taille.get())


