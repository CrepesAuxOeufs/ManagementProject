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
#jsonFile = '{"nbGroup":"10","users":[{"id":"396","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"397","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[]},{"id":"398","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"407"},{"id":"396"},{"id":"467"}]},{"id":"399","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"3","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[]},{"id":"400","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"433"},{"id":"461"}]},{"id":"401","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"427"}]},{"id":"402","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[]},{"id":"403","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"7","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"404","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"6","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"487"},{"id":"418"},{"id":"472"}]},{"id":"405","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"448"}]},{"id":"406","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"3","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"485"},{"id":"494"}]},{"id":"407","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"487"},{"id":"423"}]},{"id":"408","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"409","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"449"}]},{"id":"410","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"411","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"412","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"417"},{"id":"494"},{"id":"400"}]},{"id":"413","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"414","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"4","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[{"id":"401"},{"id":"492"}]},{"id":"415","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"416","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"434"}]},{"id":"417","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"436"},{"id":"433"}]},{"id":"418","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"459"},{"id":"410"}]},{"id":"419","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"420","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[]},{"id":"421","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"400"},{"id":"410"},{"id":"455"}]},{"id":"422","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"437"},{"id":"478"},{"id":"434"}]},{"id":"423","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"488"},{"id":"450"},{"id":"483"}]},{"id":"424","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[]},{"id":"425","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"487"}]},{"id":"426","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"427","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"428","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"427"},{"id":"426"},{"id":"465"}]},{"id":"429","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"465"},{"id":"439"}]},{"id":"430","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"431","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"432","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"7","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"433","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[{"id":"417"},{"id":"422"}]},{"id":"434","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"404"},{"id":"427"},{"id":"399"}]},{"id":"435","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"4","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"423"},{"id":"441"}]},{"id":"436","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"461"}]},{"id":"437","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"438"}]},{"id":"438","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"3","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[]},{"id":"439","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"440","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"0","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"468"}]},{"id":"441","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"6","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[]},{"id":"442","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"491"},{"id":"414"},{"id":"418"}]},{"id":"443","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"444","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"488"},{"id":"491"},{"id":"427"}]},{"id":"445","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"446","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"447","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"473"}]},{"id":"448","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[]},{"id":"449","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"3","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"462"},{"id":"428"}]},{"id":"450","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"466"},{"id":"495"},{"id":"422"}]},{"id":"451","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"452","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"487"}]},{"id":"453","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"7","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"487"}]},{"id":"454","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"455","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"442"},{"id":"479"},{"id":"401"}]},{"id":"456","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[]},{"id":"457","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"419"},{"id":"455"}]},{"id":"458","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[]},{"id":"459","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"460","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"3","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[{"id":"397"}]},{"id":"461","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"450"}]},{"id":"462","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"463","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"6","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"427"},{"id":"424"},{"id":"446"}]},{"id":"464","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"456"},{"id":"445"}]},{"id":"465","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"472"}]},{"id":"466","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"7","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"404"},{"id":"464"},{"id":"435"}]},{"id":"467","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[]},{"id":"468","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"4","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"3","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"420"},{"id":"443"}]},{"id":"469","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"425"},{"id":"480"}]},{"id":"470","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"6","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"448"}]},{"id":"471","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"444"}]},{"id":"472","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"7","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"491"},{"id":"445"}]},{"id":"473","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"474","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"449"}]},{"id":"475","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"3","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"477"},{"id":"434"}]},{"id":"476","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"437"},{"id":"484"}]},{"id":"477","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"3","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[{"id":"397"}]},{"id":"478","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"427"},{"id":"406"}]},{"id":"479","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[]},{"id":"480","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"406"},{"id":"408"}]},{"id":"481","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"3","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"453"},{"id":"472"},{"id":"421"}]},{"id":"482","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"415"}]},{"id":"483","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"481"},{"id":"463"}]},{"id":"484","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"476"}]},{"id":"485","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"4","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"486","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"426"}]},{"id":"487","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"430"},{"id":"407"}]},{"id":"488","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[{"id":"469"}]},{"id":"489","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"457"},{"id":"434"}]},{"id":"490","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"422"},{"id":"465"},{"id":"401"}]},{"id":"491","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"6","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"436"}]},{"id":"492","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[]},{"id":"493","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"432"},{"id":"469"}]},{"id":"494","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"3","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"457"}]},{"id":"495","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"496","belbin":[{"id":"2","value":"0","name":"President"},{"id":"7","value":"0","name":"Coequipier"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"3","value":"0","name":"Faiseur"},{"id":"1","value":"0","name":"Organisateur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"4","value":"0","name":"Creatif"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[{"id":"396"},{"id":"396"},{"id":"396"},{"id":"396"}]},{"id":"497","belbin":[{"id":"2","value":"10","name":"President"},{"id":"7","value":"5","name":"Coequipier"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"3","value":"5","name":"Faiseur"},{"id":"1","value":"5","name":"Organisateur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"4","value":"5","name":"Creatif"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"412"},{"id":"403"}]},{"id":"498","belbin":[{"id":"2","value":"0","name":"President"},{"id":"7","value":"20","name":"Coequipier"},{"id":"5","value":"20","name":"Eclaireur"},{"id":"3","value":"20","name":"Faiseur"},{"id":"1","value":"10","name":"Organisateur"},{"id":"6","value":"10","name":"Evaluateur"},{"id":"4","value":"10","name":"Creatif"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"412"},{"id":"415"},{"id":"495"},{"id":"492"}]}]}'
#jsonFile = '{"nbGroup":"7","users":[{"id":"396","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"397","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[]},{"id":"398","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"407"},{"id":"396"},{"id":"467"}]},{"id":"399","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"3","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[]},{"id":"400","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"433"},{"id":"461"}]},{"id":"401","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"427"}]},{"id":"402","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[]},{"id":"403","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"7","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"404","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"6","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"487"},{"id":"418"},{"id":"472"}]},{"id":"405","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"448"}]},{"id":"406","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"3","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"485"},{"id":"494"}]},{"id":"407","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"487"},{"id":"423"}]},{"id":"408","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"409","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"449"}]},{"id":"410","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"411","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"412","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"417"},{"id":"494"},{"id":"400"}]},{"id":"413","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"414","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"4","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[{"id":"401"},{"id":"492"}]},{"id":"415","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"416","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"434"}]},{"id":"417","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"436"},{"id":"433"}]},{"id":"418","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"459"},{"id":"410"}]},{"id":"419","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"420","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[]},{"id":"421","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"400"},{"id":"410"},{"id":"455"}]},{"id":"422","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"437"},{"id":"478"},{"id":"434"}]},{"id":"423","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"488"},{"id":"450"},{"id":"483"}]},{"id":"424","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[]},{"id":"425","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"487"}]},{"id":"426","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"427","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"428","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"427"},{"id":"426"},{"id":"465"}]},{"id":"429","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"465"},{"id":"439"}]},{"id":"430","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"431","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"432","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"7","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"433","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[{"id":"417"},{"id":"422"}]},{"id":"434","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"404"},{"id":"427"},{"id":"399"}]},{"id":"435","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"4","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"423"},{"id":"441"}]},{"id":"436","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"461"}]},{"id":"437","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"438"}]},{"id":"438","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"3","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[]},{"id":"439","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"440","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"0","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"468"}]},{"id":"441","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"6","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[]},{"id":"442","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"491"},{"id":"414"},{"id":"418"}]},{"id":"443","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"444","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"488"},{"id":"491"},{"id":"427"}]},{"id":"445","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"446","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"447","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"473"}]},{"id":"448","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[]},{"id":"449","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"3","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"462"},{"id":"428"}]},{"id":"450","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"466"},{"id":"495"},{"id":"422"}]},{"id":"451","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"452","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"487"}]},{"id":"453","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"7","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"487"}]},{"id":"454","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"455","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"442"},{"id":"479"},{"id":"401"}]},{"id":"456","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[]},{"id":"457","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"419"},{"id":"455"}]},{"id":"458","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[]},{"id":"459","belbin":[{"id":"1","value":"3","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[]},{"id":"460","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"3","name":"Evaluateur"},{"id":"7","value":"2","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[{"id":"397"}]},{"id":"461","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"450"}]},{"id":"462","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"1","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"463","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"6","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"427"},{"id":"424"},{"id":"446"}]},{"id":"464","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"456"},{"id":"445"}]},{"id":"465","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"4","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"7","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"472"}]},{"id":"466","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"7","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"404"},{"id":"464"},{"id":"435"}]},{"id":"467","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[]},{"id":"468","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"4","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"3","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"420"},{"id":"443"}]},{"id":"469","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"4","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"425"},{"id":"480"}]},{"id":"470","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"1","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"6","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"448"}]},{"id":"471","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"6","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"2","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"444"}]},{"id":"472","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"7","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"1","name":"Evaluateur"},{"id":"7","value":"7","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"6","name":"BDD"},{"id":"3","value":"3","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"491"},{"id":"445"}]},{"id":"473","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[]},{"id":"474","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"2","name":"Marketing"}],"uncompatibility":[{"id":"449"}]},{"id":"475","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"3","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"8","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"477"},{"id":"434"}]},{"id":"476","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"437"},{"id":"484"}]},{"id":"477","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"0","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"3","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"2","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"4","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[{"id":"397"}]},{"id":"478","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"2","name":"Faiseur"},{"id":"4","value":"2","name":"Creatif"},{"id":"5","value":"2","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"427"},{"id":"406"}]},{"id":"479","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"1","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"8","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[]},{"id":"480","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"9","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"4","name":"Marketing"}],"uncompatibility":[{"id":"406"},{"id":"408"}]},{"id":"481","belbin":[{"id":"1","value":"2","name":"Organisateur"},{"id":"2","value":"5","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"3","name":"Eclaireur"},{"id":"6","value":"3","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"6","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"453"},{"id":"472"},{"id":"421"}]},{"id":"482","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"3","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"4","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"415"}]},{"id":"483","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"481"},{"id":"463"}]},{"id":"484","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"476"}]},{"id":"485","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"4","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"486","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"7","name":"Finisseur"}],"skills":[{"id":"1","value":"1","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[{"id":"426"}]},{"id":"487","belbin":[{"id":"1","value":"4","name":"Organisateur"},{"id":"2","value":"0","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"8","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"4","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"9","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"2","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"430"},{"id":"407"}]},{"id":"488","belbin":[{"id":"1","value":"6","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"5","name":"Faiseur"},{"id":"4","value":"7","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"2","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[{"id":"469"}]},{"id":"489","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"4","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"5","name":"Eclaireur"},{"id":"6","value":"2","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"5","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"3","name":"Marketing"}],"uncompatibility":[{"id":"457"},{"id":"434"}]},{"id":"490","belbin":[{"id":"1","value":"7","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"3","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"7","value":"1","name":"Coequipier"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"5","name":"BDD"},{"id":"3","value":"4","name":"Programmation"},{"id":"4","value":"3","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"422"},{"id":"465"},{"id":"401"}]},{"id":"491","belbin":[{"id":"1","value":"1","name":"Organisateur"},{"id":"2","value":"8","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"1","name":"Creatif"},{"id":"5","value":"8","name":"Eclaireur"},{"id":"6","value":"8","name":"Evaluateur"},{"id":"7","value":"5","name":"Coequipier"},{"id":"8","value":"6","name":"Finisseur"}],"skills":[{"id":"1","value":"5","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"5","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"436"}]},{"id":"492","belbin":[{"id":"1","value":"9","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"9","name":"Creatif"},{"id":"5","value":"7","name":"Eclaireur"},{"id":"6","value":"5","name":"Evaluateur"},{"id":"7","value":"6","name":"Coequipier"},{"id":"8","value":"1","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"1","name":"Marketing"}],"uncompatibility":[]},{"id":"493","belbin":[{"id":"1","value":"0","name":"Organisateur"},{"id":"2","value":"6","name":"President"},{"id":"3","value":"8","name":"Faiseur"},{"id":"4","value":"5","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"3","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"1","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"5","name":"Metier"},{"id":"5","value":"6","name":"Marketing"}],"uncompatibility":[{"id":"432"},{"id":"469"}]},{"id":"494","belbin":[{"id":"1","value":"8","name":"Organisateur"},{"id":"2","value":"9","name":"President"},{"id":"3","value":"7","name":"Faiseur"},{"id":"4","value":"6","name":"Creatif"},{"id":"5","value":"6","name":"Eclaireur"},{"id":"6","value":"6","name":"Evaluateur"},{"id":"7","value":"9","name":"Coequipier"},{"id":"8","value":"3","name":"Finisseur"}],"skills":[{"id":"1","value":"4","name":"Web"},{"id":"2","value":"4","name":"BDD"},{"id":"3","value":"6","name":"Programmation"},{"id":"4","value":"1","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[{"id":"457"}]},{"id":"495","belbin":[{"id":"1","value":"5","name":"Organisateur"},{"id":"2","value":"2","name":"President"},{"id":"3","value":"9","name":"Faiseur"},{"id":"4","value":"3","name":"Creatif"},{"id":"5","value":"4","name":"Eclaireur"},{"id":"6","value":"9","name":"Evaluateur"},{"id":"7","value":"0","name":"Coequipier"},{"id":"8","value":"2","name":"Finisseur"}],"skills":[{"id":"1","value":"3","name":"Web"},{"id":"2","value":"3","name":"BDD"},{"id":"3","value":"1","name":"Programmation"},{"id":"4","value":"6","name":"Metier"},{"id":"5","value":"5","name":"Marketing"}],"uncompatibility":[]},{"id":"496","belbin":[{"id":"2","value":"0","name":"President"},{"id":"7","value":"0","name":"Coequipier"},{"id":"5","value":"0","name":"Eclaireur"},{"id":"3","value":"0","name":"Faiseur"},{"id":"1","value":"0","name":"Organisateur"},{"id":"6","value":"0","name":"Evaluateur"},{"id":"4","value":"0","name":"Creatif"},{"id":"8","value":"0","name":"Finisseur"}],"skills":[{"id":"1","value":"0","name":"Web"},{"id":"2","value":"0","name":"BDD"},{"id":"3","value":"0","name":"Programmation"},{"id":"4","value":"0","name":"Metier"},{"id":"5","value":"0","name":"Marketing"}],"uncompatibility":[{"id":"396"},{"id":"396"},{"id":"396"},{"id":"396"}]}]}'


jsonParse = json.loads(jsonFile)
jsonUser = jsonParse["users"]
# Parametres a modifier
nbPersonne = int(len(jsonUser))
nbEquipe = int(jsonParse["nbGroup"])
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

listOrganisateur 	= 	[]
listPresident	 	= 	[]
listFaiseur 		= 	[]
listCreatif 		= 	[]
listEclaireur 		= 	[]
listCoequipier 		= 	[]
listFinisseur 		= 	[]
listEvaluateur 		= 	[]
listWeb 			= 	[]
listbdd 			= 	[]
listProgrammation 	= 	[]
listMetier 			= 	[]
listMarketing 		= 	[]

# Ajoute l'id des etudiants avec leurs evaluations associees aux domaines
for i in range(len(ListEtudiant)):
	test = []
	test.append(ListEtudiant[i].idPersonne)
	test.append(ListEtudiant[i].organisateur)
	listOrganisateur.append(test)
	test = []
	test.append(ListEtudiant[i].idPersonne)
	test.append(ListEtudiant[i].president)
	listPresident.append(test)
	test = []
	test.append(ListEtudiant[i].idPersonne)
	test.append(ListEtudiant[i].faiseur)
	listFaiseur.append(test)
	test = []
	test.append(ListEtudiant[i].idPersonne)
	test.append(ListEtudiant[i].creatif)
	listCreatif.append(test)
	test = []
	test.append(ListEtudiant[i].idPersonne)
	test.append(ListEtudiant[i].eclaireur)
	listEclaireur.append(test)
	test = []
	test.append(ListEtudiant[i].idPersonne)
	test.append(ListEtudiant[i].coequipier)
	listCoequipier.append(test)
	test = []
	test.append(ListEtudiant[i].idPersonne)
	test.append(ListEtudiant[i].finisseur)
	listFinisseur.append(test)
	test = []
	test.append(ListEtudiant[i].idPersonne)
	test.append(ListEtudiant[i].evaluateur)
	listEvaluateur.append(test)	
	test = []
	test.append(ListEtudiant[i].idPersonne)
	test.append(ListEtudiant[i].web)
	listWeb.append(test)	
	test = []
	test.append(ListEtudiant[i].idPersonne)
	test.append(ListEtudiant[i].bdd)
	listbdd.append(test)	
	test = []
	test.append(ListEtudiant[i].idPersonne)
	test.append(ListEtudiant[i].programmation)
	listProgrammation.append(test)	
	test = []
	test.append(ListEtudiant[i].idPersonne)
	test.append(ListEtudiant[i].metier)
	listMetier.append(test)	
	test = []
	test.append(ListEtudiant[i].idPersonne)
	test.append(ListEtudiant[i].marketing)
	listMarketing.append(test)	

# Classement Belbin croissant [id,note]
listOrganisateur 	= 	sorted(listOrganisateur, key=operator.itemgetter(1))
listPresident 		= 	sorted(listPresident, key=operator.itemgetter(1))
listFaiseur 		= 	sorted(listFaiseur, key=operator.itemgetter(1))
listCreatif 		= 	sorted(listCreatif, key=operator.itemgetter(1))
listEclaireur 		= 	sorted(listEclaireur, key=operator.itemgetter(1))
listCoequipier		= 	sorted(listCoequipier, key=operator.itemgetter(1))
listFinisseur 		= 	sorted(listFinisseur, key=operator.itemgetter(1))
listEvaluateur 		= 	sorted(listEvaluateur, key=operator.itemgetter(1))
# Classement competence croissant [id,note]
listWeb 			= 	sorted(listWeb, key=operator.itemgetter(1))
listbdd 			= 	sorted(listbdd, key=operator.itemgetter(1))
listProgrammation 	= 	sorted(listProgrammation, key=operator.itemgetter(1))
listMetier 			= 	sorted(listMetier, key=operator.itemgetter(1))
listMarketing 		= 	sorted(listMarketing, key=operator.itemgetter(1))

ListEtudiantUtilise = []
for i in range(nbPersonne):
	ListEtudiantUtilise.append(0)

Equipe = []

# Creation d'emplacement libre pour les equipes
for i in range(nbEquipe):
	Equipetmp = []
	for j in range(nbParEquipe):
		Equipetmp.append(-2)
	Equipe.append(Equipetmp)
for i in range(nbEquipePlusUn):
	Equipe[i].append(-2)
# Fin de la creation

def compatible(idPersonne,Groupe,Liste):
	for i in range(len(Groupe)):
		if(Liste[idPersonne].incompatibilite1 == Groupe[i] or Liste[idPersonne].incompatibilite2 == Groupe[i] or Liste[idPersonne].incompatibilite3 == Groupe[i] or Liste[idPersonne].incompatibilite4 == Groupe[i]):
			return False
		elif(Liste[Groupe[i]].incompatibilite1 == idPersonne or Liste[Groupe[i]].incompatibilite2 == idPersonne or Liste[Groupe[i]].incompatibilite3 == idPersonne or Liste[Groupe[i]].incompatibilite4 == idPersonne):
			return False
		else:
			return True
			
# Integration des personnes dans l'equipe
for i in range(nbParEquipe):
	for j in range(nbEquipe):
		if(i%13==0):
			if(ListEtudiantUtilise[listWeb[-j-1][0]] == 0 and compatible(listWeb[-j-1][0],Equipe[j],ListEtudiant)):
				Equipe[j][i] = listWeb[-j-1][0]
				ListEtudiantUtilise[listWeb[-j-1][0]] = 1
			else:
				try:
					jTmp = j
					while(ListEtudiantUtilise[listWeb[-jTmp-1][0]] == 1 or not compatible(listWeb[-jTmp-1][0],Equipe[j],ListEtudiant)):
						jTmp += 1
					Equipe[j][i] = listWeb[-jTmp-1][0]
					ListEtudiantUtilise[listWeb[-jTmp-1][0]] = 1
				except IndexError:
					jTmp = j
					while(ListEtudiantUtilise[listWeb[-jTmp-1][0]] == 1):
						jTmp += 1
					Equipe[j][i] = listWeb[-jTmp-1][0]
					ListEtudiantUtilise[listWeb[-jTmp-1][0]] = 1
		elif(i%13==1):
			if(ListEtudiantUtilise[listbdd[-j-1][0]]==0 and compatible(listbdd[-j-1][0],Equipe[j],ListEtudiant)):
				Equipe[j][i] = listbdd[-j-1][0]
				ListEtudiantUtilise[listbdd[-j-1][0]] = 1
			else:
				try:
					jTmp = j
					while(ListEtudiantUtilise[listbdd[-jTmp-1][0]] == 1 or not compatible(listbdd[-jTmp-1][0],Equipe[j],ListEtudiant)):
						jTmp += 1
					Equipe[j][i] = listbdd[-jTmp-1][0]
					ListEtudiantUtilise[listbdd[-jTmp-1][0]] = 1
				except IndexError:
					jTmp = j
					while(ListEtudiantUtilise[listbdd[-jTmp-1][0]] == 1):
						jTmp += 1
					Equipe[j][i] = listbdd[-jTmp-1][0]
					ListEtudiantUtilise[listbdd[-jTmp-1][0]] = 1
		elif(i%13==2):
			if(ListEtudiantUtilise[listProgrammation[-j-1][0]]==0 and compatible(listProgrammation[-j-1][0],Equipe[j],ListEtudiant)):
				Equipe[j][i] = listProgrammation[-j-1][0]
				ListEtudiantUtilise[listProgrammation[-j-1][0]] = 1
			else:
				try:
					jTmp = j
					while(ListEtudiantUtilise[listProgrammation[-jTmp-1][0]] == 1 or not compatible(listProgrammation[-jTmp-1][0],Equipe[j],ListEtudiant)):
						jTmp += 1
					Equipe[j][i] = listProgrammation[-jTmp-1][0]
					ListEtudiantUtilise[listProgrammation[-jTmp-1][0]] = 1
				except IndexError:
					jTmp = j
					while(ListEtudiantUtilise[listProgrammation[-jTmp-1][0]] == 1):
						jTmp += 1
					Equipe[j][i] = listProgrammation[-jTmp-1][0]
					ListEtudiantUtilise[listProgrammation[-jTmp-1][0]] = 1
		elif(i%13==3):
			if(ListEtudiantUtilise[listMetier[-j-1][0]]==0 and compatible(listMetier[-j-1][0],Equipe[j],ListEtudiant)):
				Equipe[j][i] = listMetier[-j-1][0]
				ListEtudiantUtilise[listMetier[-j-1][0]] = 1
			else:
				try:
					jTmp = j
					while(ListEtudiantUtilise[listMetier[-jTmp-1][0]] == 1 or not compatible(listMetier[-jTmp-1][0],Equipe[j],ListEtudiant)):
						jTmp += 1
					Equipe[j][i] = listMetier[-jTmp-1][0]
					ListEtudiantUtilise[listMetier[-jTmp-1][0]] = 1
				except IndexError:
					jTmp = j
					while(ListEtudiantUtilise[listMetier[-jTmp-1][0]] == 1):
						jTmp += 1
					Equipe[j][i] = listMetier[-jTmp-1][0]
					ListEtudiantUtilise[listMetier[-jTmp-1][0]] = 1		
		elif(i%13==4):
			if(ListEtudiantUtilise[listMarketing[-j-1][0]]==0 and compatible(listMarketing[-j-1][0],Equipe[j],ListEtudiant)):
				Equipe[j][i] = listMarketing[-j-1][0]
				ListEtudiantUtilise[listMarketing[-j-1][0]] = 1
			else:
				try:
					jTmp = j
					while(ListEtudiantUtilise[listMarketing[-jTmp-1][0]] == 1 or not compatible(listMarketing[-jTmp-1][0],Equipe[j],ListEtudiant)):
						jTmp += 1
					Equipe[j][i] = listMarketing[-jTmp-1][0]
					ListEtudiantUtilise[listMarketing[-jTmp-1][0]] = 1
				except IndexError:
					jTmp = j
					while(ListEtudiantUtilise[listMarketing[-jTmp-1][0]] == 1):
						jTmp += 1
					Equipe[j][i] = listMarketing[-jTmp-1][0]
					ListEtudiantUtilise[listMarketing[-jTmp-1][0]] = 1		
		elif(i%13==5):
			if(ListEtudiantUtilise[listOrganisateur[-j-1][0]]==0 and compatible(listOrganisateur[-j-1][0],Equipe[j],ListEtudiant)):
				Equipe[j][i] = listOrganisateur[-j-1][0]
				ListEtudiantUtilise[listOrganisateur[-j-1][0]] = 1
			else:
				try:
					jTmp = j
					while(ListEtudiantUtilise[listOrganisateur[-jTmp-1][0]] == 1 or not compatible(listOrganisateur[-jTmp-1][0],Equipe[j],ListEtudiant)):
						jTmp += 1
					Equipe[j][i] = listOrganisateur[-jTmp-1][0]
					ListEtudiantUtilise[listOrganisateur[-jTmp-1][0]] = 1
				except IndexError:
					jTmp = j
					while(ListEtudiantUtilise[listOrganisateur[-jTmp-1][0]] == 1):
						jTmp += 1
					Equipe[j][i] = listOrganisateur[-jTmp-1][0]
					ListEtudiantUtilise[listOrganisateur[-jTmp-1][0]] = 1		
		elif(i%13==6):
			if(ListEtudiantUtilise[listPresident[-j-1][0]]==0 and compatible(listPresident[-j-1][0],Equipe[j],ListEtudiant)):
				Equipe[j][i] = listPresident[-j-1][0]
				ListEtudiantUtilise[listPresident[-j-1][0]] = 1
			else:
				try:
					jTmp = j
					while(ListEtudiantUtilise[listPresident[-jTmp-1][0]] == 1 or not compatible(listPresident[-jTmp-1][0],Equipe[j],ListEtudiant)):
						jTmp += 1
					Equipe[j][i] = listPresident[-jTmp-1][0]
					ListEtudiantUtilise[listPresident[-jTmp-1][0]] = 1
				except IndexError:
					jTmp = j
					while(ListEtudiantUtilise[listPresident[-jTmp-1][0]] == 1):
						jTmp += 1
					Equipe[j][i] = listPresident[-jTmp-1][0]
					ListEtudiantUtilise[listPresident[-jTmp-1][0]] = 1	
		elif(i%13==7):
			if(ListEtudiantUtilise[listFaiseur[-j-1][0]]==0 and compatible(listFaiseur[-j-1][0],Equipe[j],ListEtudiant)):
				Equipe[j][i] = listFaiseur[-j-1][0]
				ListEtudiantUtilise[listFaiseur[-j-1][0]] = 1
			else:
				try:
					jTmp = j
					while(ListEtudiantUtilise[listFaiseur[-jTmp-1][0]] == 1 or not compatible(listFaiseur[-jTmp-1][0],Equipe[j],ListEtudiant)):
						jTmp += 1
					Equipe[j][i] = listFaiseur[-jTmp-1][0]
					ListEtudiantUtilise[listFaiseur[-jTmp-1][0]] = 1
				except IndexError:
					jTmp = j
					while(ListEtudiantUtilise[listFaiseur[-jTmp-1][0]] == 1):
						jTmp += 1
					Equipe[j][i] = listFaiseur[-jTmp-1][0]
					ListEtudiantUtilise[listFaiseur[-jTmp-1][0]] = 1	
		elif(i%13==8):
			if(ListEtudiantUtilise[listCreatif[-j-1][0]]==0 and compatible(listCreatif[-j-1][0],Equipe[j],ListEtudiant)):
				Equipe[j][i] = listCreatif[-j-1][0]
				ListEtudiantUtilise[listCreatif[-j-1][0]] = 1
			else:
				try:
					jTmp = j
					while(ListEtudiantUtilise[listCreatif[-jTmp-1][0]] == 1 or not compatible(listCreatif[-jTmp-1][0],Equipe[j],ListEtudiant)):
						jTmp += 1
					Equipe[j][i] = listCreatif[-jTmp-1][0]
					ListEtudiantUtilise[listCreatif[-jTmp-1][0]] = 1
				except IndexError:
					jTmp = j
					while(ListEtudiantUtilise[listCreatif[-jTmp-1][0]] == 1):
						jTmp += 1
					Equipe[j][i] = listCreatif[-jTmp-1][0]
					ListEtudiantUtilise[listCreatif[-jTmp-1][0]] = 1
		elif(i%13==9):
			if(ListEtudiantUtilise[listEclaireur[-j-1][0]]==0 and compatible(listEclaireur[-j-1][0],Equipe[j],ListEtudiant)):
				Equipe[j][i] = listEclaireur[-j-1][0]
				ListEtudiantUtilise[listEclaireur[-j-1][0]] = 1
			else:
				try:
					jTmp = j
					while(ListEtudiantUtilise[listEclaireur[-jTmp-1][0]] == 1 or not compatible(listEclaireur[-jTmp-1][0],Equipe[j],ListEtudiant)):
						jTmp += 1
					Equipe[j][i] = listEclaireur[-jTmp-1][0]
					ListEtudiantUtilise[listEclaireur[-jTmp-1][0]] = 1
				except IndexError:
					jTmp = j
					while(ListEtudiantUtilise[listEclaireur[-jTmp-1][0]] == 1):
						jTmp += 1
					Equipe[j][i] = listEclaireur[-jTmp-1][0]
					ListEtudiantUtilise[listEclaireur[-jTmp-1][0]] = 1
		elif(i%13==10):
			if(ListEtudiantUtilise[listCoequipier[-j-1][0]]==0 and compatible(listCoequipier[-j-1][0],Equipe[j],ListEtudiant)):
				Equipe[j][i] = listCoequipier[-j-1][0]
				ListEtudiantUtilise[listCoequipier[-j-1][0]] = 1
			else:
				try:
					jTmp = j
					while(ListEtudiantUtilise[listCoequipier[-jTmp-1][0]] == 1 or not compatible(listCoequipier[-jTmp-1][0],Equipe[j],ListEtudiant)):
						jTmp += 1
					Equipe[j][i] = listCoequipier[-jTmp-1][0]
					ListEtudiantUtilise[listCoequipier[-jTmp-1][0]] = 1
				except IndexError:
					jTmp = j
					while(ListEtudiantUtilise[listCoequipier[-jTmp-1][0]] == 1):
						jTmp += 1
					Equipe[j][i] = listCoequipier[-jTmp-1][0]
					ListEtudiantUtilise[listCoequipier[-jTmp-1][0]] = 1
		elif(i%13==11):
			if(ListEtudiantUtilise[listFinisseur[-j-1][0]]==0 and compatible(listFinisseur[-j-1][0],Equipe[j],ListEtudiant)):
				Equipe[j][i] = listFinisseur[-j-1][0]
				ListEtudiantUtilise[listFinisseur[-j-1][0]] = 1
			else:
				try:
					jTmp = j
					while(ListEtudiantUtilise[listFinisseur[-jTmp-1][0]] == 1 or not compatible(listFinisseur[-jTmp-1][0],Equipe[j],ListEtudiant)):
						jTmp += 1
					Equipe[j][i] = listFinisseur[-jTmp-1][0]
					ListEtudiantUtilise[listFinisseur[-jTmp-1][0]] = 1
				except IndexError:
					jTmp = j
					while(ListEtudiantUtilise[listFinisseur[-jTmp-1][0]] == 1):
						jTmp += 1
					Equipe[j][i] = listFinisseur[-jTmp-1][0]
					ListEtudiantUtilise[listFinisseur[-jTmp-1][0]] = 1
		elif(i%13==12):
			if(ListEtudiantUtilise[listEvaluateur[-j-1][0]]==0 and compatible(listEvaluateur[-j-1][0],Equipe[j],ListEtudiant)):
				Equipe[j][i] = listEvaluateur[-j-1][0]
				ListEtudiantUtilise[listEvaluateur[-j-1][0]] = 1
			else:
				try:
					jTmp = j
					while(ListEtudiantUtilise[listEvaluateur[-jTmp-1][0]] == 1 or not compatible(listEvaluateur[-jTmp-1][0],Equipe[j],ListEtudiant)):
						jTmp += 1
					Equipe[j][i] = listEvaluateur[-jTmp-1][0]
					ListEtudiantUtilise[listEvaluateur[-jTmp-1][0]] = 1
				except IndexError:
					jTmp = j
					while(ListEtudiantUtilise[listEvaluateur[-jTmp-1][0]] == 1):
						jTmp += 1
					Equipe[j][i] = listEvaluateur[-jTmp-1][0]
					ListEtudiantUtilise[listEvaluateur[-jTmp-1][0]] = 1
for j in range(nbEquipePlusUn):
	for k in range(len(ListEtudiantUtilise)):
		if(ListEtudiantUtilise[k]==0):
			Equipe[j][i+1] = k
			ListEtudiantUtilise[k] = 1
			break;

def supDoublons(liste):
	delete = False
	while(not delete):
		count = 0	
		casse = False
		for i in range(len(liste)-2):
			for j in range(i+1,len(liste)-1):
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
		for j in range(len(equipe[i])-1):
			for k in range(j,len(equipe[i])-1):
				if(liste[Equipetmp[i][j]].incompatibilite1 == Equipetmp[i][k] or liste[Equipetmp[i][j]].incompatibilite2 == Equipetmp[i][k] or liste[Equipetmp[i][j]].incompatibilite3 == Equipetmp[i][k] or liste[Equipetmp[i][j]].incompatibilite4 == Equipetmp[i][k]):
					if(j != k):
						IncompTmp.append(liste[Equipetmp[i][j]].idPersonne)
				elif(liste[Equipetmp[i][k]].incompatibilite1 == Equipetmp[i][j] or liste[Equipetmp[i][k]].incompatibilite2 == Equipetmp[i][j] or liste[Equipetmp[i][k]].incompatibilite3 == Equipetmp[i][j] or liste[Equipetmp[i][k]].incompatibilite4 == Equipetmp[i][j]):
					if(j != k):
						IncompTmp.append(liste[Equipetmp[i][k]].idPersonne)
	supDoublons(IncompTmp)
	#print(IncompTmp)
	return IncompTmp


incr = 0
count = 0
EquipeTmp = copy.deepcopy(Equipe)
while(len(combienIncompatibles(ListEtudiant,Equipe))!=0 and count!=1000):
	switchI1 = 0
	switchI2 = 0
	switchJ1 = 0
	switchJ2 = 0
	
	a = combienIncompatibles(ListEtudiant,Equipe)
	if(len(a)>1):
		first = 0
		second = 0
		for i in range(len(Equipe)):
			for j in range(len(Equipe[i])):
				if(Equipe[i][j]==a[0]):
					switchI1 = i
					switchJ1 = j
				if(Equipe[i][j]==a[incr]):
					switchI2 = i
					switchJ2 = j	
		#print(len(combienIncompatibles(ListEtudiant,Equipe)))
		tmp = Equipe[switchI1][switchJ1]
		EquipeTmp[switchI1][switchJ1] = Equipe[switchI2][switchJ2]
		EquipeTmp[switchI2][switchJ2] = tmp
		Equipe = copy.deepcopy(EquipeTmp)
		a = combienIncompatibles(ListEtudiant,Equipe)
		if(switchI1 == switchI2):
			if(len(a)-1<incr):
				incr=0
			else:
				incr += 1
		else:
			incr = 0
	else:
		for i in range(len(Equipe)):
			for j in range(len(Equipe[i])):
				if(Equipe[i][j]==a[0]):
					switchI2 = i
					switchJ2 = j
		if(switchI1 == 0):
			switchI1 += 1
		tmp = Equipe[switchI1][switchJ1]
		EquipeTmp[switchI1][switchJ1] = Equipe[switchI2][switchJ2]
		EquipeTmp[switchI2][switchJ2] = tmp
		Equipe = copy.deepcopy(EquipeTmp)
		a = combienIncompatibles(ListEtudiant,Equipe)
	count+=1

if(count==1000):
	sys.exit()									
#print("Equipe : " + str(Equipe))

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
			
#print(Equipe)

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
sys.stdout.write(str(jsonSend))
sys.exit()
#print("json envoye :")
#print(jsonSend)