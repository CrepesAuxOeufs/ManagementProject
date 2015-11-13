<?php
	/* 
	* connexion: connectBDD()
	* disable avertissment message for mysql in the future depreciated : ini_set('display_errors','off') // on off
	*/
	function connectBDD(){
		ini_set('display_errors','off');
		$connexion = mysql_connect("mysql.imerir.com", "parcevaux3a05","dharV6DSSx88x5MK");
		mysql_select_db("parcevaux3a05", $connexion);
		mysql_set_charset("utf8", $connexion);
		
		/*
        $result=mysql_query("SELECT * FROM USER");
        while($row = mysql_fetch_assoc($result))
        {
			echo $row['id'] . '> ' . $row['name'] . ' ' . $row['nickname'] . '  ( ' . $row['mail'] . ' )<br>';
		}*/
		ini_set('display_errors','on');
		return $connexion;
	}
	
?>