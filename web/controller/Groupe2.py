#!/usr/bin/python
# -*- coding: UTF-8 -*-

#enable debugging

import random
import copy

import sys

class Etudiant:
	def __init__(self,idJean):
		self.idPersonne 		= 	idJean
		self.organisateur 		= 	int(random.uniform(0,20))
		self.president			=	int(random.uniform(0,20))
		self.faiseur			=	int(random.uniform(0,20))
		self.creatif			=	int(random.uniform(0,20))
		self.eclaireur			=	int(random.uniform(0,20))
		self.coequipier			=	int(random.uniform(0,20))
		self.finisseur			=	int(random.uniform(0,20))
		self.evaluateur			=	int(random.uniform(0,20))
		self.web 				=	int(random.uniform(0,6))
		self.bdd				=	int(random.uniform(0,6))
		self.programmation		=	int(random.uniform(0,6))
		self.metier				=	int(random.uniform(0,6))
		self.marketing			=	int(random.uniform(0,6))
		self.incompatibilite1	=	int(random.uniform(0,nbPersonne))
		self.incompatibilite2 	=	int(random.uniform(0,nbPersonne))
		self.incompatibilite3 	=	int(random.uniform(0,nbPersonne))
		self.incompatibilite4	=	int(random.uniform(0,nbPersonne))

def moyWeb(liste):
	chocapic = 0;
	for i in range(len(liste)):
		chocapic += liste[i].web
	return chocapic/len(liste)
	
def moybdd(liste):
	lampadaire = 0
	for i in range(len(liste)):
		lampadaire += liste[i].bdd
	return lampadaire/len(liste)
	
def moyProgrammation(liste):
	croissant = 0
	for i in range(len(liste)):
		croissant += liste[i].programmation
	return croissant/len(liste)

def moyMetier(liste):
	chomeur = 0
	for i in range(len(liste)):
		chomeur += liste[i].metier
	return chomeur/len(liste)

def moyMarketing(liste):
	pub = 0
	for i in range(len(liste)):
		pub += liste[i].marketing
	return pub/len(liste)

def moyPresident(liste):
	wut = 0
	for i in range(len(liste)):
		wut += liste[i].president
	return wut/len(liste)

def moyOrganisateur(liste):
	scrum = 0
	for i in range(len(liste)):
		scrum += liste[i].organisateur
	return scrum/len(liste)
	
def moyFaiseur(liste):
	doIt = 0
	for i in range(len(liste)):
		doIt += liste[i].faiseur
	return doIt/len(liste)

def moyCreatif(liste):
	art = 0
	for i in range(len(liste)):
		art += liste[i].creatif
	return art/len(liste)
	
def moyEclaireur(liste):
	fusee = 0
	for i in range(len(liste)):
		fusee += liste[i].eclaireur
	return fusee/len(liste)

def moyCoequipier(liste):
	friend = 0
	for i in range(len(liste)):
		friend += liste[i].coequipier
	return friend/len(liste) 

def moyFinisseur(liste):
	finishHim = 0
	for i in range(len(liste)):
		finishHim += liste[i].finisseur
	return finishHim/len(liste)

def moyEvaluateur(liste):
	zero = 0
	for i in range(len(liste)):
		zero += liste[i].evaluateur
	return zero/len(liste)
	
nbPersonne = 300
nbEquipe = 8
nbEquipePlusUn = nbPersonne%nbEquipe
nbParEquipe = int(nbPersonne/nbEquipe)

ListEtudiant = []
# Remplissage d'une liste d'étudiants
for i in range(nbPersonne):
	ListEtudiant.append(Etudiant(i))

ListEtudiantUtilise = []
for i in range(len(ListEtudiant)):
	ListEtudiantUtilise.append(0)
incr = 0
Equipe = []
for i in range(nbEquipe):
	EquipeTmp = []
	if(len(Equipe)<nbEquipePlusUn):
		test = False
		count = 0
		while not test:
			a = incr
			if(ListEtudiantUtilise[a]==0):
				EquipeTmp.append(a)
				count += 1
				ListEtudiantUtilise[a]=1
				incr += 1
			if(count == nbParEquipe+1):
				test = True
	else:
		test = False
		count = 0
		while not test:
			a = incr
			if(ListEtudiantUtilise[a]==0):
				EquipeTmp.append(a)
				count += 1
				ListEtudiantUtilise[a]=1
				incr += 1
			if(count == nbParEquipe):
				test = True
	Equipe.append(EquipeTmp)


trying = False
Equipetmp = copy.deepcopy(Equipe)

#print(Equipe)

def compatible(equipe,liste,Equipetmp):
	equipe = Equipetmp
	countv2 = 0
	end = False
	while((not end) and (countv2<1000)):
		count = 0
		for i in range(len(Equipetmp)):
			for j in range(len(Equipetmp[i])):
				for k in range(len(Equipetmp[i])):
					if(liste[Equipetmp[i][j]].incompatibilite1 == Equipetmp[i][k] or liste[Equipetmp[i][j]].incompatibilite2 == Equipetmp[i][k] or liste[Equipetmp[i][j]].incompatibilite3 == Equipetmp[i][k] or liste[Equipetmp[i][j]].incompatibilite4 == Equipetmp[i][k]):
						count += 1
						if(i>0):
							tmp = equipe[i-1][j]
							Equipetmp[i-1][j] = equipe[i][j]
							Equipetmp[i][j] = tmp
						else:
							tmp = equipe[i+1][j]
							Equipetmp[i+1][j] = equipe[i][j]
							Equipetmp[i][j] = tmp
					elif(liste[Equipetmp[i][k]].incompatibilite1 == Equipetmp[i][j] or liste[Equipetmp[i][k]].incompatibilite2 == Equipetmp[i][j] or liste[Equipetmp[i][k]].incompatibilite3 == Equipetmp[i][j] or liste[Equipetmp[i][k]].incompatibilite4 == Equipetmp[i][j]):
						count += 1
						if(i>0):
							tmp = equipe[i-1][k]
							Equipetmp[i-1][j] = equipe[i][k]
							Equipetmp[i][k] = tmp
						else:
							tmp = equipe[i+1][k]
							Equipetmp[i+1][j] = equipe[i][k]
							Equipetmp[i][k] = tmp
			if(count == 0):
				end = True
#		print(countv2)
		countv2 += 1
	return Equipetmp

Equipe = compatible(Equipe,ListEtudiant,Equipetmp)
		
moyGeneral = []

moyGeneral.append(moyWeb(ListEtudiant))
moyGeneral.append(moybdd(ListEtudiant))
moyGeneral.append(moyProgrammation(ListEtudiant))
moyGeneral.append(moyMetier(ListEtudiant))
moyGeneral.append(moyMarketing(ListEtudiant))
moyGeneral.append(moyPresident(ListEtudiant))
moyGeneral.append(moyOrganisateur(ListEtudiant))
moyGeneral.append(moyFaiseur(ListEtudiant))
moyGeneral.append(moyCreatif(ListEtudiant))
moyGeneral.append(moyEclaireur(ListEtudiant))
moyGeneral.append(moyCoequipier(ListEtudiant))
moyGeneral.append(moyFinisseur(ListEtudiant))
moyGeneral.append(moyEvaluateur(ListEtudiant))

Score = []

def Scoring(equipe,liste,moyenne):
	ScoreFinal = [0]*len(equipe)
	for i in range(len(equipe)):
		Scoretmp = [0]*13
		for j in range(len(equipe[i])):
			Scoretmp[0] += liste[equipe[i][j]].web
			Scoretmp[1] += liste[equipe[i][j]].bdd
			Scoretmp[2] += liste[equipe[i][j]].programmation
			Scoretmp[3] += liste[equipe[i][j]].metier
			Scoretmp[4] += liste[equipe[i][j]].marketing
			
			Scoretmp[5] += liste[equipe[i][j]].president
			Scoretmp[6] += liste[equipe[i][j]].organisateur
			Scoretmp[7] += liste[equipe[i][j]].faiseur
			Scoretmp[8] += liste[equipe[i][j]].creatif
			Scoretmp[9] += liste[equipe[i][j]].eclaireur
			Scoretmp[10] += liste[equipe[i][j]].coequipier
			Scoretmp[11] += liste[equipe[i][j]].finisseur
			Scoretmp[12] += liste[equipe[i][j]].evaluateur
		for j in range(len(Scoretmp)):
			ScoreFinal[i] += (Scoretmp[i]/len(equipe[i]))/moyenne[i]	
	return ScoreFinal

def switch(Equipe,nombreEquipe,nombreEtudiant,nombreParEquipe,moyenne,liste):
	test = False
	Equipetmp = copy.deepcopy(Equipe)
	a = int(random.uniform(0,nombreEquipe))
	b = int(random.uniform(0,nombreEquipe))
	while(a==b):
		b = int(random.uniform(0,nombreEquipe))
	c = int(random.uniform(0,nombreParEquipe))
	d = int(random.uniform(0,nombreParEquipe))
	while(c==d):
		d = int(random.uniform(0,nombreParEquipe))	
	for i in range(len(Equipe[a])):
		if((ListEtudiant[Equipe[a][i]].incompatibilite1 == Equipe[b][d] or ListEtudiant[Equipe[a][i]].incompatibilite1 == Equipe[b][d] or ListEtudiant[Equipe[a][i]].incompatibilite1 == Equipe[b][d] or ListEtudiant[Equipe[a][i]].incompatibilite1 == Equipe[b][d]) and i!=c):
			test = True
	for i in range(len(Equipe[b])):
		if((ListEtudiant[Equipe[b][i]].incompatibilite1 == Equipe[a][c] or ListEtudiant[Equipe[b][i]].incompatibilite1 == Equipe[a][c] or ListEtudiant[Equipe[b][i]].incompatibilite1 == Equipe[a][c] or ListEtudiant[Equipe[b][i]].incompatibilite1 == Equipe[a][c]) and i!=d):
			test = True
	if(test):
		tmp = Equipe[b][d]
		Equipetmp[b][d] = Equipe[a][c]
		Equipetmp[a][c] = tmp
		if(dif(Equipetmp,liste,moyenne)<dif(Equipe,liste,moyenne)):
			return Equipetmp
		else:
			return Equipe
	else:
		return Equipe

def dif(equipe,liste,moyenne):
	Scoring1 = Scoring(equipe,liste,moyenne)
	mini = Scoring1[0]
	maxi = Scoring1[0]
	for i in range(len(Scoring1)):
		if(Scoring1[i]<mini):
			mini = Scoring1[i]
		elif(Scoring1[i]>maxi):
			maxi = Scoring1[i]
	return abs(maxi-mini)
	

while(i<500):
	Equipe = switch(Equipe,nbEquipe,len(ListEtudiant),nbParEquipe,moyGeneral,ListEtudiant)
	i += 1
#	print(i)

#print("Equipe : ")
#print()
#print(Equipe)
Score = Scoring(Equipe,ListEtudiant,moyGeneral)
#print("Score : ")
#print(Score)

#for i in range(len(ListEtudiant)):
#	print("Etudiant" + str(ListEtudiant[i].idPersonne) + " : " + str(ListEtudiant[i].incompatibilite1) + " - " + str(ListEtudiant[i].incompatibilite2) + " - " + str(ListEtudiant[i].incompatibilite3) + " - " + str(ListEtudiant[i].incompatibilite4))

#print("Content-Type: text/plain;charset=UTF-8")
#print()

sys.stdout.write(str(Score))

sys.exit()