<?php
	include 'message.php';
	include 'connect.php';
	include 'session.php';

	connectBDD();

	$json = json_decode(file_get_contents("php://input"),true);
	//$json = '{ "login": "directeur@imerir.com", "password": "imerir" }';

	$parsed_json = json_decode($json);
	$login =    $parsed_json -> {'login'};
	$password = $parsed_json -> {'password'};

    $result = mysql_query( "SELECT * FROM USER WHERE mail =  '". $login ."'");

    $logOk = false;
    $passOk = false;

    $row = mysql_fetch_assoc($result);
    
    /* If login exist */
    if ($row['mail'] == $login)
    {
    	$logOk = true ;
    }
    else
    {
   		$response = getJSONFromCodeError(300);
    }
    /* If password is correct with good login */
    if($logOk && $row['password']==$password)
    {
    	$passOk = true;
    }
    else if ($logOk && $row['password']!=$password)
    {
    	$response = getJSONFromCodeError(301);
    }
    /* if all is ok */
    if($logOk && $passOk)
    {
    	$name =  $row['name'] ;
    	$nickname =  $row['nickname'] ;
    	$mail =  $row['mail'] ; 

    	createSession(5, $nickname, $name, $mail);
    	$response = getJSONFromCodeError(200);
    }

	echo json_encode($response);

?>