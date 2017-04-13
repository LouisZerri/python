# -*-coding:Latin-1 -*
import random
import sys

class Unit(object):
	"""docstring for Personnage"""
	def __init__(self,name,pdv,pa):
		self.nom = name
		self.points_de_vie = pdv
		self.points_armure = pa

	def attaque(self,name):
		print("{0} attaque {1}".format(name,self.nom))

	def subit_attaque(self):
		degats = random.randint(7, 10)
		self.points_de_vie -= degats

		if(self.points_de_vie < 0):
			self.points_de_vie = 0
			print("{0} subit une attaque de {1} de dégats, il lui reste {2} points de vie".format(self.nom,degats,self.points_de_vie))
		else:
			print("{0} subit une attaque de {1} de dégats, il lui reste {2} points de vie".format(self.nom,degats,self.points_de_vie))

		if(self.points_de_vie <= 0):
			print("{0} est vaincu".format(self.nom))


	def soin(self):
		soin = random.randint(100, 110)
		self.points_de_vie += soin

		if(self.points_de_vie > 100):
			self.points_de_vie = 100
			print("{0} gagne {1} de points de vie".format(self.nom,soin))
		else:
			print("{0} gagne {1} de points de vie".format(self.nom,soin))

	def affiche(self):
		print("Nom : {0}".format(self.nom))
		print("Points de vie : {0}".format(self.points_de_vie))
		print("Points d'armure : {0}".format(self.points_armure))


class Joueur(Unit):
    def __init__(self, name, pdv, pa):
        super(Joueur,self).__init__(name,pdv,pa)

class Ennemi(Unit):
	def __init__(self,name, pdv, pa):
		super(Ennemi,self).__init__(name,pdv,pa)


""" PROGRAMME PRINCIPAL """

joueur = Joueur("L\'aventurier",100,30)
balrog = Ennemi("Balrog",100,10)
squelette = Ennemi("Squelette",100,10)
 
j = 5 # Initialisation de la variable pour limiter l'accès au soin

for i in range(1,101):
	print("\n\n===== | L\'aventurier - ({0}/100pv) | =====\n\n".format(joueur.points_de_vie))
	print("")
	print("=====Tour n°{0}=====".format(i))
	print("")
	print("Quelle action souhaitez vous faire : ")
	
	if(j >= 1):
		print("1 - Se soigner (encore {0} fois)".format(j))
	else:
		print("1 - Vous ne pouvez plus soigner")


	#On verifie si balrog est en vie et donc si on peut l'attaquer
	if(balrog.points_de_vie > 0):
		print("2 - Attaquer {0} - ({1}/100pv)".format(balrog.nom,balrog.points_de_vie))
	else:
		print("2 - {0} est vaicu".format(balrog.nom))


	#De même pour le squelette
	if(squelette.points_de_vie > 0):
		print("3 - Attaquer {0} - ({1}/100pv)".format(squelette.nom,squelette.points_de_vie))
	else:
		print("3 - {0} est vaicu".format(squelette.nom))

	print("4 - Quitter")
	choix = input("Entrer votre choix : ")
	print("")

	if(choix == 1):

		if(j >= 1):
			joueur.soin()
			print("Vous pouvez vous soigner encore {0} fois".format(j-1))
		else:
			print("Vous ne pouvez plus vous soigner !")
		j -= 1
	
	elif(choix == 2):
		balrog.attaque(joueur.nom)
		balrog.subit_attaque();

	elif(choix == 3):
		squelette.attaque(joueur.nom)
		squelette.subit_attaque();

	elif(choix == 4):
		print("Game Over")
		sys.exit(1)

	else:
		print("Erreur, veuillez réessayer")


	print("\n===Les ennemis ripostent===\n")


	#L'ennemi balrog attaque le joueur	
	if(balrog.points_de_vie > 0):
		print("{0} attaque : \n".format(balrog.nom))
		joueur.attaque(balrog.nom); #le joueur se fait attaquer par balrog
		joueur.subit_attaque(); #le joueur subit l'attaque de balrog
	else:
		print("{0} est mort".format(balrog.nom))

	
	#L'ennemi squelette attaque le joueur
	if(squelette.points_de_vie > 0):
		print("{0} attaque : \n".format(squelette.nom))
		joueur.attaque(squelette.nom); #le joueur se fait attaquer par squelette
		joueur.subit_attaque(); #le joueur subit l'attaque de squelette
	else:
		print("{0} est mort".format(squelette.nom))


	#Condition de fin de jeu
	if(joueur.points_de_vie == 0):
		print("Game Over")
		sys.exit(1)

	if((balrog.points_de_vie == 0) and (squelette.points_de_vie == 0)):
		print("Vous avez gagné !")
		sys.exit(1)
