#!/usr/bin/python

import random
from random import randint
import json
import operator
import copy
import sys

class Etudiant:
	def __init__(self,idJean):
		self.idPersonne 		= 	int(idJean)
		self.organisateur		=	0
		self.president			=	0
		self.faiseur			=	0
		self.creatif			=	0
		self.eclaireur			=	0
		self.coequipier			=	0
		self.finisseur			=	0
		self.evaluateur			=	0
		self.web				=	0
		self.bdd				=	0
		self.programmation		=	0
		self.metier				=	0
		self.marketing			=	0
		self.incompatibilite1	=	-1
		self.incompatibilite2	=	-1
		self.incompatibilite3	=	-1
		self.incompatibilite4	=	-1
		

f = open('generator/data.json', 'r')
jsonFile = f.read()
f.close()
#jsonFile = '{"nbGroup":"10","nbIteration":3000,"users":[{"id":"396","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"397","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[]},{"id":"398","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"407"},{"id":"396"},{"id":"467"}]},{"id":"399","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"3","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[]},{"id":"400","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"433"},{"id":"461"}]},{"id":"401","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"427"}]},{"id":"402","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[]},{"id":"403","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"7","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"404","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"6","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"487"},{"id":"418"},{"id":"472"}]},{"id":"405","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"448"}]},{"id":"406","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"3","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"485"},{"id":"494"}]},{"id":"407","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"487"},{"id":"423"}]},{"id":"408","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"409","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"449"}]},{"id":"410","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"411","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"412","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"417"},{"id":"494"},{"id":"400"}]},{"id":"413","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"414","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"4","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[{"id":"401"},{"id":"492"}]},{"id":"415","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"416","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"434"}]},{"id":"417","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"436"},{"id":"433"}]},{"id":"418","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"459"},{"id":"410"}]},{"id":"419","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"420","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[]},{"id":"421","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"400"},{"id":"410"},{"id":"455"}]},{"id":"422","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"437"},{"id":"478"},{"id":"434"}]},{"id":"423","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"488"},{"id":"450"},{"id":"483"}]},{"id":"424","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[]},{"id":"425","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"487"}]},{"id":"426","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"427","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"428","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"427"},{"id":"426"},{"id":"465"}]},{"id":"429","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"465"},{"id":"439"}]},{"id":"430","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"431","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"432","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"7","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"433","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[{"id":"417"},{"id":"422"}]},{"id":"434","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"404"},{"id":"427"},{"id":"399"}]},{"id":"435","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"4","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"423"},{"id":"441"}]},{"id":"436","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"461"}]},{"id":"437","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"438"}]},{"id":"438","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"3","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[]},{"id":"439","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"440","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"0","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"468"}]},{"id":"441","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"6","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[]},{"id":"442","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"491"},{"id":"414"},{"id":"418"}]},{"id":"443","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"444","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"488"},{"id":"491"},{"id":"427"}]},{"id":"445","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"446","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"447","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"473"}]},{"id":"448","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[]},{"id":"449","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"3","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"462"},{"id":"428"}]},{"id":"450","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"466"},{"id":"495"},{"id":"422"}]},{"id":"451","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"452","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"487"}]},{"id":"453","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"7","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"487"}]},{"id":"454","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"455","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"442"},{"id":"479"},{"id":"401"}]},{"id":"456","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[]},{"id":"457","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"419"},{"id":"455"}]},{"id":"458","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[]},{"id":"459","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"460","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"3","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[{"id":"397"}]},{"id":"461","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"450"}]},{"id":"462","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"463","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"6","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"427"},{"id":"424"},{"id":"446"}]},{"id":"464","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"456"},{"id":"445"}]},{"id":"465","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"472"}]},{"id":"466","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"7","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"404"},{"id":"464"},{"id":"435"}]},{"id":"467","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[]},{"id":"468","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"4","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"3","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"420"},{"id":"443"}]},{"id":"469","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"425"},{"id":"480"}]},{"id":"470","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"6","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"448"}]},{"id":"471","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"444"}]},{"id":"472","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"7","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"491"},{"id":"445"}]},{"id":"473","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"474","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"449"}]},{"id":"475","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"3","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"477"},{"id":"434"}]},{"id":"476","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"437"},{"id":"484"}]},{"id":"477","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"3","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[{"id":"397"}]},{"id":"478","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"427"},{"id":"406"}]},{"id":"479","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[]},{"id":"480","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"406"},{"id":"408"}]},{"id":"481","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"3","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"453"},{"id":"472"},{"id":"421"}]},{"id":"482","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"415"}]},{"id":"483","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"481"},{"id":"463"}]},{"id":"484","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"476"}]},{"id":"485","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"4","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"486","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"426"}]},{"id":"487","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"430"},{"id":"407"}]},{"id":"488","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[{"id":"469"}]},{"id":"489","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"457"},{"id":"434"}]},{"id":"490","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"422"},{"id":"465"},{"id":"401"}]},{"id":"491","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"6","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"436"}]},{"id":"492","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[]},{"id":"493","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"432"},{"id":"469"}]},{"id":"494","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"3","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"457"}]},{"id":"495","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"496","belbin":[{"id":"2","value":"0","name":"President"},{"id":"7","value":"0","name":"Coequipier"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"3","value":"0","name":"Faiseur"},{"id":"1","value":"0","name":"Organisateur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"4","value":"0","name":"Creatif"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[{"id":"396"},{"id":"396"},{"id":"396"},{"id":"396"}]},{"id":"497","belbin":[{"id":"2","value":"10","name":"President"},{"id":"7","value":"5","name":"Coequipier"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"3","value":"5","name":"Faiseur"},{"id":"1","value":"5","name":"Organisateur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"4","value":"5","name":"Creatif"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"412"},{"id":"403"}]},{"id":"498","belbin":[{"id":"2","value":"0","name":"President"},{"id":"7","value":"20","name":"Coequipier"},{"id":"5","value":"20","name":"Eclaireur"},{"id":"3","value":"20","name":"Faiseur"},{"id":"1","value":"10","name":"Organisateur"},{"id":"6","value":"10","name":"Evaluateur"},{"id":"4","value":"10","name":"Creatif"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"412"},{"id":"415"},{"id":"495"},{"id":"492"}]}]}'

jsonParse = json.loads(jsonFile)
jsonUser = jsonParse["users"]
# Parametres a modifier
nbPersonne = int(len(jsonUser))
nbEquipe = int(jsonParse["nbGroup"])
nbIteration = int(jsonParse["nbIteration"])
# Variables interessantes
nbEquipePlusUn = nbPersonne%nbEquipe
nbParEquipe = int(nbPersonne/nbEquipe)

ListEtudiant = []
ListIdentifiant = []

for i in range(len(jsonUser)):
	ListIdentifiant.append(int(jsonUser[i]["id"]))
	ListEtudiant.append(Etudiant(i)) 
	# Belbin
	ListEtudiant[i].organisateur = int(jsonUser[i]["belbin"][0]["value"])
	ListEtudiant[i].president = int(jsonUser[i]["belbin"][1]["value"])
	ListEtudiant[i].faiseur = int(jsonUser[i]["belbin"][2]["value"])
	ListEtudiant[i].creatif = int(jsonUser[i]["belbin"][3]["value"])
	ListEtudiant[i].eclaireur = int(jsonUser[i]["belbin"][4]["value"])
	ListEtudiant[i].evaluateur = int(jsonUser[i]["belbin"][5]["value"])
	#Il en manque 2
	try:
		ListEtudiant[i].finisseur = int(jsonUser[i]["belbin"][6]["value"])
	except IndexError:
		ListEtudiant[i].finisseur = 0
	try:
		ListEtudiant[i].coequipier = int(jsonUser[i]["belbin"][7]["value"])
	except IndexError:
		ListEtudiant[i].coequipier = 0
	#Domaine
	ListEtudiant[i].web = int(jsonUser[i]["skills"][0]["value"])
	ListEtudiant[i].bdd = int(jsonUser[i]["skills"][1]["value"])
	ListEtudiant[i].programmation = int(jsonUser[i]["skills"][2]["value"])
	ListEtudiant[i].metier = int(jsonUser[i]["skills"][3]["value"])
	ListEtudiant[i].marketing = int(jsonUser[i]["skills"][4]["value"])
	try:
		ListEtudiant[i].incompatibilite1 = int(jsonUser[i]["uncompatibility"][0]["id"])
	except IndexError:
		ListEtudiant[i].incompatibilite1 = -1
	try:
		ListEtudiant[i].incompatibilite2 = int(jsonUser[i]["uncompatibility"][1]["id"])
	except IndexError:
		ListEtudiant[i].incompatibilite2 = -1
	try:
		ListEtudiant[i].incompatibilite3 = int(jsonUser[i]["uncompatibility"][2]["id"])
	except IndexError:
		ListEtudiant[i].incompatibilite3 = -1
	try:
		ListEtudiant[i].incompatibilite4 = int(jsonUser[i]["uncompatibility"][3]["id"])
	except IndexError:
		ListEtudiant[i].incompatibilite4 = -1
		
for i in range(len(ListEtudiant)):
	if(ListEtudiant[i].incompatibilite1 != -1):
		for j in range(len(ListIdentifiant)):
			if(ListIdentifiant[j]==ListEtudiant[i].incompatibilite1):
				ListEtudiant[i].incompatibilite1 = ListEtudiant[j].idPersonne
	if(ListEtudiant[i].incompatibilite2 != -1):
		for j in range(len(ListIdentifiant)):
			if(ListIdentifiant[j]==ListEtudiant[i].incompatibilite2):
				ListEtudiant[i].incompatibilite2 = ListEtudiant[j].idPersonne
	if(ListEtudiant[i].incompatibilite3 != -1):
		for j in range(len(ListIdentifiant)):
			if(ListIdentifiant[j]==ListEtudiant[i].incompatibilite3):
				ListEtudiant[i].incompatibilite3 = ListEtudiant[j].idPersonne
	if(ListEtudiant[i].incompatibilite4 != -1):
		for j in range(len(ListIdentifiant)):
			if(ListIdentifiant[j]==ListEtudiant[i].incompatibilite4):
				ListEtudiant[i].incompatibilite4 = ListEtudiant[j].idPersonne

def valWeb(liste):
	chocapicMin = 6
	chocapic = 0
	chocapicMax = 0
	tmp = []
	for i in range(len(liste)):
		chocapic += liste[i].web
		if(liste[i].web<chocapicMin):
			chocapicMin = liste[i].web
		elif(liste[i].web>chocapicMax):
			chocapicMax = liste[i].web
	tmp.append(chocapicMin)
	tmp.append(chocapic/len(liste))
	tmp.append(chocapicMax)
	return tmp
	
def valbdd(liste):
	lampadaireMin = 6
	lampadaire = 0
	lampadaireMax = 0
	tmp = []
	for i in range(len(liste)):
		lampadaire += liste[i].bdd
		if(liste[i].bdd<lampadaireMin):
			lampadaireMin = liste[i].bdd
		elif(liste[i].bdd>lampadaireMax):
			lampadaireMax = liste[i].bdd
	tmp.append(lampadaireMin)
	tmp.append(lampadaire/len(liste))
	tmp.append(lampadaireMax)
	return tmp
	
def valProgrammation(liste):
	croissantMin = 6
	croissant = 0
	croissantMax = 0
	tmp = []
	for i in range(len(liste)):
		croissant += liste[i].programmation
		if(liste[i].programmation<croissantMin):
			croissantMin = liste[i].programmation
		elif(liste[i].programmation>croissantMax):
			croissantMax = liste[i].programmation
	tmp.append(croissantMin)
	tmp.append(croissant/len(liste))
	tmp.append(croissantMax)
	return tmp

def valMetier(liste):
	chomeurMin = 6
	chomeur = 0
	chomeurMax = 6
	tmp = []
	for i in range(len(liste)):
		chomeur += liste[i].metier
		if(liste[i].metier<chomeurMin):
			chomeurMin = liste[i].metier
		elif(liste[i].metier>chomeurMax):
			chomeurMax = liste[i].metier
	tmp.append(chomeurMin)
	tmp.append(chomeur/len(liste))
	tmp.append(chomeurMax)
	return tmp

def valMarketing(liste):
	pubMin = 6
	pub = 0
	pubMax = 0
	tmp = []
	for i in range(len(liste)):
		pub += liste[i].marketing
		if(liste[i].marketing<pubMin):
			pubMin = liste[i].marketing
		elif(liste[i].marketing>pubMax):
			pubMax = liste[i].marketing
	tmp.append(pubMin)
	tmp.append(pub/len(liste))
	tmp.append(pubMax)
	return tmp

def valPresident(liste):
	wutMin = 20
	wut = 0
	wutMax = 0
	tmp = []
	for i in range(len(liste)):
		wut += liste[i].president
		if(liste[i].president<wutMin):
			wutMin = liste[i].president
		elif(liste[i].president>wutMax):
			wutMax = liste[i].president
	tmp.append(wutMin)
	tmp.append(wut/len(liste))
	tmp.append(wutMax)
	return tmp

def valOrganisateur(liste):
	scrumMin = 20
	scrum = 0
	scrumMax = 20
	tmp = []
	for i in range(len(liste)):
		scrum += liste[i].organisateur
		if(liste[i].organisateur<scrumMin):
			scrumMin = liste[i].organisateur
		elif(liste[i].organisateur>scrumMax):
			scrumMax = liste[i].organisateur
	tmp.append(scrumMin)
	tmp.append(scrum/len(liste))
	tmp.append(scrumMax)
	return tmp
	
def valFaiseur(liste):
	doItMin = 20
	doIt = 0
	doItMax = 0
	tmp = []
	for i in range(len(liste)):
		doIt += liste[i].faiseur
		if(liste[i].faiseur<doItMin):
			doItMin = liste[i].faiseur
		elif(liste[i].faiseur>doItMax):
			doItMax = liste[i].faiseur
	tmp.append(doItMin)
	tmp.append(doIt/len(liste))
	tmp.append(doItMax)
	return tmp

def valCreatif(liste):
	artMin = 20
	art = 0
	artMax = 0
	tmp = []
	for i in range(len(liste)):
		art += liste[i].creatif
		if(liste[i].creatif<artMin):
			artMin = liste[i].creatif
		elif(liste[i].creatif>artMax):
			artMax = liste[i].creatif
	tmp.append(artMin)
	tmp.append(art/len(liste))
	tmp.append(artMax)
	return tmp
	
def valEclaireur(liste):
	fuseeMin = 20
	fusee = 0
	fuseeMax = 0
	tmp = []
	for i in range(len(liste)):
		fusee += liste[i].eclaireur
		if(liste[i].eclaireur<fuseeMin):
			fuseeMin = liste[i].eclaireur
		elif(liste[i].eclaireur>fuseeMax):
			fuseeMax = liste[i].eclaireur
	tmp.append(fuseeMin)
	tmp.append(fusee/len(liste))
	tmp.append(fuseeMax)
	return tmp

def valCoequipier(liste):
	friendMin = 20
	friend = 0
	friendMax = 20
	tmp = []
	for i in range(len(liste)):
		friend += liste[i].coequipier
		if(liste[i].coequipier<friendMin):
			friendMin = liste[i].coequipier
		elif(liste[i].coequipier>friendMax):
			friendMax = liste[i].coequipier
	tmp.append(friendMin)
	tmp.append(friend/len(liste))
	tmp.append(friendMax)
	return tmp

def valFinisseur(liste):
	finishHimMin = 20
	finishHim = 0
	finishHimMax = 0
	tmp = []
	for i in range(len(liste)):
		finishHim += liste[i].finisseur
		if(liste[i].finisseur<finishHimMin):
			finishHimMin = liste[i].finisseur
		elif(liste[i].finisseur>finishHimMax):
			finishHimMax = liste[i].finisseur
	tmp.append(finishHimMin)
	tmp.append(finishHim/len(liste))
	tmp.append(finishHimMax)
	return tmp

def valEvaluateur(liste):
	zeroMin = 20
	zero = 0
	zeroMax = 0
	tmp = []
	for i in range(len(liste)):
		zero += liste[i].evaluateur
		if(liste[i].evaluateur<zeroMin):
			zeroMin = liste[i].evaluateur
		elif(liste[i].evaluateur>zeroMax):
			zeroMax = liste[i].evaluateur
	tmp.append(zeroMin)
	tmp.append(zero/len(liste))
	tmp.append(zeroMax)
	return tmp

# Remplissage d'une liste d'etudiants
Evaluation = []
Evaluation.append(valWeb(ListEtudiant))
Evaluation.append(valbdd(ListEtudiant))
Evaluation.append(valProgrammation(ListEtudiant))
Evaluation.append(valMetier(ListEtudiant))
Evaluation.append(valMarketing(ListEtudiant))
Evaluation.append(valPresident(ListEtudiant))
Evaluation.append(valOrganisateur(ListEtudiant))
Evaluation.append(valFaiseur(ListEtudiant))
Evaluation.append(valCreatif(ListEtudiant))
Evaluation.append(valEclaireur(ListEtudiant))
Evaluation.append(valCoequipier(ListEtudiant))
Evaluation.append(valFinisseur(ListEtudiant))
Evaluation.append(valEvaluateur(ListEtudiant))

ListEtudiantUtilise = []
for i in range(nbPersonne):
	ListEtudiantUtilise.append(0)

Equipe = []
incr = 0

# Remplissage aleatoire des etudiants dans des groupes
for i in range(nbEquipe):
	EquipeTmp = []
	if(len(Equipe)<nbEquipePlusUn):
		test = False
		count = 0
		while not test:
			a = int(random.randint(0,nbPersonne-1))
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
			a = int(random.randint(0,nbPersonne-1))
			if(ListEtudiantUtilise[a]==0):
				EquipeTmp.append(a)
				count += 1
				ListEtudiantUtilise[a]=1
				incr += 1
			if(count == nbParEquipe):
				test = True
	Equipe.append(EquipeTmp)

#print(Equipe)

def compatible(idPersonne,Groupe,Liste):
	for i in range(len(Groupe)):
		if(Liste[idPersonne].incompatibilite1 == Groupe[i] or Liste[idPersonne].incompatibilite2 == Groupe[i] or Liste[idPersonne].incompatibilite3 == Groupe[i] or Liste[idPersonne].incompatibilite4 == Groupe[i]):
			return False
		elif(Liste[Groupe[i]].incompatibilite1 == idPersonne or Liste[Groupe[i]].incompatibilite2 == idPersonne or Liste[Groupe[i]].incompatibilite3 == idPersonne or Liste[Groupe[i]].incompatibilite4 == idPersonne):
			return False
		else:
			return True

def supDoublons(liste):
	delete = False
	while(not delete):
		count = 0	
		casse = False
		for i in range(len(liste)-1):
			for j in range(i+1,len(liste)):
				if(liste[i]==liste[j]):
					count += 1
					liste.pop(j)
					casse = True
					break;
			if(casse):
				break;
		if(count == 0):
			delete = True

def combienIncompatibles(liste,equipe):
	count = 0
	IncompTmp = []
	Equipetmp = copy.deepcopy(equipe)
	for i in range(len(equipe)):
		for j in range(len(equipe[i])):
			for k in range(len(equipe[i])):
				if(liste[Equipetmp[i][j]].incompatibilite1 == Equipetmp[i][k] or liste[Equipetmp[i][j]].incompatibilite2 == Equipetmp[i][k] or liste[Equipetmp[i][j]].incompatibilite3 == Equipetmp[i][k] or liste[Equipetmp[i][j]].incompatibilite4 == Equipetmp[i][k]):
					if(j != k):
						IncompTmp.append(liste[Equipetmp[i][j]].idPersonne)
				elif(liste[Equipetmp[i][k]].incompatibilite1 == Equipetmp[i][j] or liste[Equipetmp[i][k]].incompatibilite2 == Equipetmp[i][j] or liste[Equipetmp[i][k]].incompatibilite3 == Equipetmp[i][j] or liste[Equipetmp[i][k]].incompatibilite4 == Equipetmp[i][j]):
					if(j != k):
						IncompTmp.append(liste[Equipetmp[i][k]].idPersonne)
	supDoublons(IncompTmp)
	return IncompTmp


def etesVousCompatibles(equipe,liste,equipeTest):
	incompTmp = combienIncompatibles(liste,equipeTest) 
	countTest = 0
	a = len(incompTmp)
	while(a>0 and countTest < 5000):
		if(a>1 and countTest%100!=0):
			switchI1 = 0
			switchI2 = 0
			switchJ1 = 0
			switchJ2 = 0
			test1 = randint(0,int(len(incompTmp)-1))
			test2 = randint(0,int(len(incompTmp)-1))
			while(test1==test2):
				test2 = randint(0,int(len(incompTmp)-1))
			
			for i in range(len(equipeTest)):
				for j in range(len(equipeTest[i])):
					if(incompTmp[test1]==equipeTest[i][j]):
						switchI1 = i
						switchJ1 = j
					if(incompTmp[test2]==equipeTest[i][j]):
						switchI2 = i
						switchJ2 = j
			tmp = equipe[switchI1][switchJ1]
			equipeTest[switchI1][switchJ1] = equipe[switchI2][switchJ2]
			equipeTest[switchI2][switchJ2] = tmp
			#print("Arrangement des incompatibilites : " + str(countTest) + "/5000")
			incompTmp = []
			incompTmp = combienIncompatibles(liste,equipeTest)
			equipe = copy.deepcopy(equipeTest)
			a = len(incompTmp)
		elif(countTest%100==0 or a==1):
			incompTmp = combienIncompatibles(liste,equipeTest)
			if(a == 1):
				test2 = 0
			else:
				test2 = randint(0,len(incompTmp)-1)
			for i in range(len(equipeTest)):
				for j in range(len(equipeTest[i])):
					try:
						if(incompTmp[test2]==equipeTest[i][j]):
							switchI2 = i
							switchJ2 = j
					except IndexError:
						a = len(incompTmp)
			switchI1 = randint(0,int(len(Equipe)-1))
			switchJ1 = randint(0,nbParEquipe-1)
			tmp = equipe[switchI1][switchJ1]
			equipeTest[switchI1][switchJ1] = equipe[switchI2][switchJ2]
			equipeTest[switchI2][switchJ2] = tmp
			a = len(incompTmp)
		equipe = copy.deepcopy(equipeTest)
		countTest += 1
#	print()
	#print(str(countTest) + " - " + str(a))
#	print(incompTmp)
#	print()
	return equipeTest


EquipeTmp = copy.deepcopy(Equipe)
count = 0
while(len(combienIncompatibles(ListEtudiant,Equipe))>2 and count<100):
	Equipe = etesVousCompatibles(Equipe,ListEtudiant,EquipeTmp)
	#print("Count : " + str(count))
	count+=1

moyGeneral = []

moyGeneral.append(valWeb(ListEtudiant)[1])
moyGeneral.append(valbdd(ListEtudiant)[1])
moyGeneral.append(valProgrammation(ListEtudiant)[1])
moyGeneral.append(valMetier(ListEtudiant)[1])
moyGeneral.append(valMarketing(ListEtudiant)[1])
moyGeneral.append(valPresident(ListEtudiant)[1])
moyGeneral.append(valOrganisateur(ListEtudiant)[1])
moyGeneral.append(valFaiseur(ListEtudiant)[1])
moyGeneral.append(valCreatif(ListEtudiant)[1])
moyGeneral.append(valEclaireur(ListEtudiant)[1])
moyGeneral.append(valCoequipier(ListEtudiant)[1])
moyGeneral.append(valFinisseur(ListEtudiant)[1])
moyGeneral.append(valEvaluateur(ListEtudiant)[1])

Score = []

def Scoring(equipe,liste,moyenne):
	ScoreFinal = [0]*(len(equipe))
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
		for j in range(len(moyenne)):
			#print()
			ScoreFinal[i] += (Scoretmp[j]/len(equipe[i]))/moyenne[j]
			#print("HI !")
	return ScoreFinal

def totalMoyenneEquipe(equipe,liste,moyenne,equipe2):
	Score1 = Scoring(equipe,liste,moyenne)
	Score2 = Scoring(equipe2,liste,moyenne)
	valeur1 = 0
	valeur2 = 0
	for i in range(len(Score1)):
		valeur1 += Score1[i]
	for i in range(len(Score2)):
		valeur2 += Score2[i]
	if(valeur1 <= valeur2):
		return True
	else:
		return False

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
		if(totalMoyenneEquipe(Equipetmp,liste,moyenne,Equipe)):
			return Equipetmp
		else:
			return Equipe
	else:
		return Equipe

#def dif2(MoyenneGlobale):
	

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
	

while(i<nbIteration):
	Equipe = switch(Equipe,nbEquipe,len(ListEtudiant),nbParEquipe,moyGeneral,ListEtudiant)
	i += 1
	#print("Optimisation des groupes : " + str(i) + "/10000")

#print("Equipe : ")
#print()
#print(Equipe)
Score = Scoring(Equipe,ListEtudiant,moyGeneral)
#print("Score : ")
#print(Score)


ScoreDomaineParEquipe = []

for i in range(len(Equipe)):
	Scoretmp = []
	for j in range(13):
		Scoretmp.append(0)
	ScoreDomaineParEquipe.append(Scoretmp)

for i in range(len(Equipe)):
	for j in range(len(Equipe[i])):
		ScoreDomaineParEquipe[i][0] += ListEtudiant[Equipe[i][j]].organisateur
		ScoreDomaineParEquipe[i][1] += ListEtudiant[Equipe[i][j]].president
		ScoreDomaineParEquipe[i][2] += ListEtudiant[Equipe[i][j]].faiseur
		ScoreDomaineParEquipe[i][3] += ListEtudiant[Equipe[i][j]].creatif
		ScoreDomaineParEquipe[i][4] += ListEtudiant[Equipe[i][j]].eclaireur
		ScoreDomaineParEquipe[i][5] += ListEtudiant[Equipe[i][j]].coequipier
		ScoreDomaineParEquipe[i][6] += ListEtudiant[Equipe[i][j]].finisseur
		ScoreDomaineParEquipe[i][7] += ListEtudiant[Equipe[i][j]].evaluateur
		ScoreDomaineParEquipe[i][8] += ListEtudiant[Equipe[i][j]].web
		ScoreDomaineParEquipe[i][9] += ListEtudiant[Equipe[i][j]].bdd
		ScoreDomaineParEquipe[i][10] += ListEtudiant[Equipe[i][j]].programmation
		ScoreDomaineParEquipe[i][11] += ListEtudiant[Equipe[i][j]].metier
		ScoreDomaineParEquipe[i][12] += ListEtudiant[Equipe[i][j]].marketing
		
#print("Score Domaine/equipe : ")
#for i in range(len(Equipe)):
	#print(ScoreDomaineParEquipe[i])		

ScoreParEquipe = [0]*nbEquipe
for i in range(len(ScoreDomaineParEquipe)):
	for j in range(13):
		if(j<8):
			ScoreParEquipe[i] += ScoreDomaineParEquipe[i][j]
		else:
			ScoreParEquipe[i] += int(ScoreDomaineParEquipe[i][j] * 4)
	ScoreParEquipe[i] /= len(Equipe[i])

#print("Score par equipe : " + str(ScoreParEquipe))

#print("Evaluation : " + str(Evaluation))

for i in range(len(ListEtudiant)):
	ListEtudiant[i].idPersonne = ListIdentifiant[i]
	#print(ListEtudiant[i].idPersonne)

for i in range(len(Equipe)):
	for j in range(len(Equipe[i])):
		for k in range(len(ListEtudiant)):
			if(Equipe[i][j] == k):
				Equipe[i][j] = ListIdentifiant[k] 
			

users = []
for i in range(len(Equipe)):
	for j in range(len(Equipe[i])):
		user = {}
		user['id'] = Equipe[i][j]
		user['groupId'] = i
		users.append(user)

groups = []
for i in range(len(Equipe)):
	group = {}
	group['id'] = i
	group['name'] = str("Groupe " + str(i+1))
	group['score'] = ScoreParEquipe[i]
	groups.append(group)

data = {
	'users':users,
	'groups':groups
}

jsonSend = json.dumps(data)

#f = open('generator/result.json', 'w')
#f.write(json.dumps(data))
#f.close()
#sys.stdout.write(str(jsonSend))
#sys.exit()
print("json envoye :")
print(jsonSend)
