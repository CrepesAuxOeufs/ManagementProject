<?php
	include 'message.php';
	include 'connect.php';
	include 'session.php';

	connectBDD();
	
	/* On vide les tables sauf belbin, project & skill */
	mysql_query("DELETE FROM `USER`");
	mysql_query("DELETE FROM `GROUP`");
	mysql_query("DELETE FROM `USER_GROUP`");
	mysql_query("DELETE FROM `USER_UNCOMPATIBILITY`");
	mysql_query("DELETE FROM `USER_BELBIN`");
	mysql_query("DELETE FROM `USER_SKILL`");

	/* Creation du Directeur ou dit "Admin" */
	mysql_query("INSERT INTO `USER`(`name`, `nickname`, `mail`, `password`, `admin`, `profil`) 
				 VALUES ('Denet','Laurent','directeur@imerir.com','imerir', '1', '1')");

	mysql_query("UPDATE  `USER` SET  `id` ='0' WHERE name =  'Denet' AND nickname =  'Laurent'");	

	$nbEleve = 100;
	$nbGroup = 5;

	$nbGroupSup = ($nbEleve % $nbGroup);
	$nbGroupNormal = $nbGroup - $nbGroupSup;
	$nbEleveDivisible= $nbEleve - $nbGroupSup;
	$nbEleveGroupe = $nbEleveDivisible / $nbGroup;
	$nbEleveGroupeSup = $nbEleveGroupe + 1;

	$idPremierEtudiant = 0;
	$idDernierEtudiant = 0;

	/* Creation de i eleves */
	for ($i = 1 ; $i <= $nbEleve ; $i++)
	{
		/* Creation des informations de l'etudiant */
		$name = "EtudiantName" . $i;
		$nickname = "EtudiantNickname" . $i;
		$mail = "etudiant". $i ."@imerir.com";
		$password = "password". $i;
		$admin = "0";
		$profil = "1";

		/* On ajoute une nouvel Etudiant */
		mysql_query("INSERT INTO `USER`(`name`, `nickname`, `mail`, `password`, `admin`, `profil`) 
				 	VALUES ('". $name ."','". $nickname ."','". $mail ."','". $password ."', '". $admin ."', '". $profil ."')");

		/* On recherche l'id de l'etudiant en cours */
		$result = mysql_query("SELECT id FROM `USER` WHERE name = '".$name."' AND nickname = '". $nickname . "'");
		$row = mysql_fetch_assoc($result);
		$id = $row['id']; 

		/* Nous avons 8 belbins */
		for ($j = 1 ; $j <= 8 ; $j++ )
		{
			$lvlBelbin = rand(0, 9);

			mysql_query("INSERT INTO `USER_BELBIN` (`user_id`, `belbin_id`, `value`) 
						VALUES ('". $id ."','". $j ."','". $lvlBelbin ."')");
		}
		/* Nous avons 5 domaines de competences */
		for ($k = 1 ; $k <= 5 ; $k++ )
		{
			$lvlSkill = rand(0, 6);

			mysql_query("INSERT INTO `USER_SKILL` (`user_id`, `skill_id`, `value`) 
						VALUES ('". $id ."','". $k ."','". $lvlSkill ."')");
		}

		if ($i == 1)
		{
			$idPremierEtudiant = $id;
		}
		else if($i == $nbEleve)
		{
			$idDernierEtudiant = $id;
		}
	} 

	/* Creation des incompatibilites */

	for ($a = $idPremierEtudiant ; $a <= $idDernierEtudiant ; $a++)
	{
		$nbIncompatibilite = rand (0,4);

		$Incomp1 = 0;
		$Incomp2 = 0;
		$Incomp3 = 0;

		if ($nbIncompatibilite != 0)
		{
			for ($b = 1; $b < $nbIncompatibilite ; $b++) 
			{ 
				$idIncompatible = rand($idPremierEtudiant , $idDernierEtudiant);

				/* Verifie que l'etudiant n'est pas incompatible avec lui même et avec ces derniere incompatibilites deja sauvegarder */
				if (($idIncompatible != $a) && ($idIncompatible != $Incomp1) && ($idIncompatible != $Incomp2) && ($idIncompatible != $Incomp3))
				{
					mysql_query("INSERT INTO `USER_UNCOMPATIBILITY` (`user_id`, `user_id_uncompatibility`) 
								VALUES ('". $a ."','". $idIncompatible ."')");
				}

				switch ($b) 
				{
				    case 1:
				        $Incomp1 = $idIncompatible ;
				        break;
				    case 2:
				        $Incomp2 = $idIncompatible ;
				        break;
				    case 3:
				        $Incomp3 = $idIncompatible ;
				        break;
				}
			}
		}
	}

	/* Creation de groupes bidon */

	$idEtudiantEnCour = $idPremierEtudiant;

	for ($c = 1 ; $c <= $nbGroupNormal ; $c++)
	{
		/* Creation des informations du group */
		$project_id = "1";
		$name = "Group" . $c;

		/* On ajoute une nouvel Etudiant */
		mysql_query("INSERT INTO `GROUP`(`project_id`, `name`) 
				 	VALUES ('". $project_id ."','". $name ."')");

		$resultGroup = mysql_query("SELECT id FROM `GROUP` WHERE name = '".$name."'");
		$row = mysql_fetch_assoc($resultGroup);
		$idGroup = $row['id']; 

		for ($d = 1 ; $d <=$nbEleveGroupe ; $d++)
		{
			/* On ajoute une nouvel Etudiant */
			mysql_query("INSERT INTO `USER_GROUP`(`user_id`, `group_id`) 
					 	VALUES ('". $idEtudiantEnCour ."','". $idGroup ."')");

			$idEtudiantEnCour = $idEtudiantEnCour + 1 ;
		}
	}
	if ($nbGroupSup != 0)
	{
		for ($e = 1 ; $e <= $nbGroupSup ; $e++)
		{
			/* Creation des informations du group */
			$project_id = "1";
			$number = $c + $e;
			$name = "Group" . $number ;

			/* On ajoute une nouvel Etudiant */
			mysql_query("INSERT INTO `GROUP`(`project_id`, `name`) 
					 	VALUES ('". $project_id ."','". $name ."')");

			$resultGroup = mysql_query("SELECT id FROM `GROUP` WHERE name = '".$name."'");
			$row = mysql_fetch_assoc($resultGroup);
			$idGroup = $row['id']; 

			for ($f = 1 ; $f <=$nbEleveGroupeSup ; $f++)
			{
				/* On ajoute une nouvel Etudiant */
				mysql_query("INSERT INTO `USER_GROUP`(`user_id`, `group_id`) 
						 	VALUES ('". $idEtudiantEnCour ."','". $idGroup ."')");

				$idEtudiantEnCour = $idEtudiantEnCour + 1 ;
			}
		}
	}
	
?>