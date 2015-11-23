<?php
	include 'connect.php';

	connectBDD(); 

	$ligne = 0;

	$separateur = ";";
	 
	//Premiere ligne = nom des champs (
	$xls_output = 	"ID". $separateur .
					"Web". $separateur .
					"BDD". $separateur .
					"Programmation". $separateur .
					"Metier". $separateur .
					"Marketing". $separateur .
					"Organisateur". $separateur .
					"President". $separateur .
					"Faiseur". $separateur .
					"Creatif". $separateur .
					"Eclaireur". $separateur .
					"Evaluateur". $separateur .
					"Coequipier". $separateur .
					"Finisseur". $separateur .
					"Eleve Incompatible 1". $separateur .
					"Eleve Incompatible 2". $separateur .
					"Eleve Incompatible 3". $separateur .
					"Eleve Incompatible 4". $separateur .
					$separateur .
					"Nombre d eleves". $separateur .
					"15". $separateur .
					"Nombre de groupe". $separateur .
					"4". $separateur .
					"\n";

	$ligne++;


	/*************************************************************************************************************************/
	/*********************************************************** DATA ********************************************************/
	/*************************************************************************************************************************/
	$premierEleve = $ligne + 1;

	$query="SELECT id, name, nickname
			FROM USER
			WHERE admin = 0";
	$result = mysql_query($query) or die(mysql_error());

	while($row = mysql_fetch_array($result))
	{

		/* $$$$$ ID $$$$$ */
		$idUser = $row["id"];
		$xls_output .= $row["id"]. $separateur ;

		/* $$$$$ SKILL $$$$$ */
		$skill = mysql_query("	SELECT value
								FROM `USER_SKILL` 
								WHERE user_id = '" . $idUser . "'
								ORDER BY  `USER_SKILL`.`user_id` ,  `USER_SKILL`.`skill_id` ASC ");

		while($rew = mysql_fetch_array($skill))
		{
			$xls_output .= $rew["value"]. $separateur;
		}

		/* $$$$$ BELBIN $$$$$ */
		$belbin = mysql_query("	SELECT value
								FROM `USER_BELBIN` 
								WHERE user_id = '" . $idUser . "'
								ORDER BY  `USER_BELBIN`.`user_id` ,  `USER_BELBIN`.`belbin_id` ASC ");

		while($raw = mysql_fetch_array($belbin))
		{
			$xls_output .= $raw["value"]. $separateur;
		}

		/* $$$$$ UNCOMPATIBILITY $$$$$ */
		$uncompatibility = mysql_query("	SELECT user_id_uncompatibility
											FROM `USER_UNCOMPATIBILITY` 
											WHERE user_id = '" . $idUser . "'");
		$nbUncomp = 0;
		while($riw = mysql_fetch_array($uncompatibility))
		{
			$xls_output .= $riw["user_id_uncompatibility"]. $separateur;
			$nbUncomp = $nbUncomp + 1;
		}

		switch ($nbUncomp) 
		{
			case 0 :
				$xls_output .= $separateur;
				$xls_output .= $separateur;
				$xls_output .= $separateur;
				$xls_output .= $separateur;
				break;
			case 1 :
				$xls_output .= $separateur;
				$xls_output .= $separateur;
				$xls_output .= $separateur;
				break;
			case 2 :
				$xls_output .= $separateur;
				$xls_output .= $separateur;
				break;
			case 3 :
				$xls_output .= $separateur;
				break;
		}
		$xls_output .= $separateur;
		$xls_output .= $row["name"] . $separateur;
		$xls_output .= $separateur;
		$xls_output .= $row["nickname"] . $separateur;

		/* $$$$$ Fin de ligne $$$$$ */
		$xls_output .= "\n";
		$ligne++;

	}

	$dernierEleve = $ligne;

	$nbEleve = $dernierEleve - $premierEleve;


	/*************************************************************************************************************************/
	/******************************************************** GROUPES ********************************************************/
	/*************************************************************************************************************************/


	// $xls_output .= "\n";
	// $ligne++;

	// $nbGroup = 5;

	// $xls_output .= $separateur;

	// for ($i = 1 ; $i <= $nbGroup ; $i++)
	// {
	// 	$xls_output .= "Groupe".$i. $separateur;
	// }

	// $xls_output .= "\n";
	// $ligne++;

	// /*************************************************************************************************************************/
	// /***************************************************** VARIABLES *********************************************************/
	// /*************************************************************************************************************************/

	// $ligneDebutVar = $ligne+1;

	// $query="SELECT id
	// 		FROM USER
	// 		WHERE admin = 0";
	// $result = mysql_query($query) or die(mysql_error());
	 
	// //Boucle sur les resultats
	// while($row = mysql_fetch_array($result))
	// {

	// 	/* $$$$$ SKILL $$$$$ */

	// 	$idUser = $row["id"];

	// 	$xls_output .= $row["id"]. $separateur;

	// 	$xls_output .= "\n";
	// 	$ligne++;
	// }
	// $ligneFinVar = $ligne;


	// /*************************************************************************************************************************/
	// *************************************************** CALCULS ***********************************************************
	// /*************************************************************************************************************************/


	// $Alpha = array("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","W","X","Y","Z");

	// $xls_output .= "SOMME:". $separateur;

	// for ($i = 1 ; $i <= $nbGroup ; $i++)
	// {
	// 	$xls_output .= "=SOMME(". $Alpha[$i] . $ligneDebutVar .":". $Alpha[$i] . $ligneFinVar .")". $separateur;
	// }
	// $xls_output .= "\n";
	// $ligne++;

	// $xls_output .= "SCORE:". $separateur;



	// // for ($i = 1 ; $i <= $nbGroup ; $i++)
	// // {
	// // 	for($j = 1 ; $j <=  $nbEleve ; $j++)
	// // 	{
	// // 		if ($j == 1)
	// // 		{
	// // 			$xls_output .= "=(B108*(SOMME(B2:F2)+(SOMME(G2:N2)*4)))+";
	// // 		}
	// // 		else if ( $j != $nbEleve)
	// // 		{
	// // 			$xls_output .= "(B108*(SOMME(B2:F2)+(SOMME(G2:N2)*4)))+";
	// // 		}
	// // 		else if ( $j == $nbEleve)
	// // 		{
	// // 			$xls_output .= "(B108*(SOMME(B2:F2)+(SOMME(G2:N2)*4)))+";
	// // 		}
	// // 	}
	// // 	$xls_output = $separateur;
	// // }
	// // $xls_output .= "\n";
	// // $ligne++;

	 
	header("Content-Type: application/octet-stream");
	header("Content-disposition: attachment; filename=Table" . date("Ymd").".csv");
	print $xls_output;
	exit;
?>