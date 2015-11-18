<?
	include 'connect.php';

	connectBDD(); 
	 
	//Premiere ligne = nom des champs (
	$xls_output = "ID;Web;BDD;Programmation;Metier;Marketing;Organisateur;President;Faiseur;Creatif;Eclaireur;Evaluateur;Coequipier;Finisseur;Eleve Incompatible 1;Eleve Incompatible 2;Eleve Incompatible 3;Eleve Incompatible 4 \n";
	 
	//Requete SQL
	$query="SELECT id
			FROM USER
			WHERE admin = 0";
	$result = mysql_query($query) or die(mysql_error());
	 
	//Boucle sur les resultats
	while($row = mysql_fetch_array($result))
	{

		/* $$$$$ SKILL $$$$$ */

		$idUser = $row["id"];

		$xls_output .= $row["id"].";";

		/* $$$$$ SKILL $$$$$ */

		$skill = mysql_query("	SELECT value
								FROM `USER_SKILL` 
								WHERE user_id = '" . $idUser . "'
								ORDER BY  `USER_SKILL`.`user_id` ,  `USER_SKILL`.`skill_id` ASC ");


		while($rew = mysql_fetch_array($skill))
		{
			$xls_output .= $rew["value"].";";
		}

		/* $$$$$ BELBIN $$$$$ */

		$belbin = mysql_query("	SELECT value
								FROM `USER_BELBIN` 
								WHERE user_id = '" . $idUser . "'
								ORDER BY  `USER_BELBIN`.`user_id` ,  `USER_BELBIN`.`belbin_id` ASC ");


		while($raw = mysql_fetch_array($belbin))
		{
			$xls_output .= $raw["value"].";";
		}

		/* $$$$$ UNCOMPATIBILITY $$$$$ */

		$uncompatibility = mysql_query("	SELECT user_id_uncompatibility
											FROM `USER_UNCOMPATIBILITY` 
											WHERE user_id = '" . $idUser . "'");


		while($riw = mysql_fetch_array($uncompatibility))
		{
			$xls_output .= $riw["user_id_uncompatibility"].";";
		}

		$xls_output .= "\n";

	}
	 
	header("Content-Type: application/octet-stream");
	header("Content-disposition: attachment; filename=Table" . date("Ymd").".csv");
	print $xls_output;
	exit;
?>