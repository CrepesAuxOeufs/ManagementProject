<?php
	include 'message.php';
	include 'connect.php';
	include 'session.php';

	error_reporting(0);
	connectBDD();

	$json = json_decode(file_get_contents("php://input"),true);
	$login =    $json['login'];
    $password = $json['password'];

    /* for test*/
    //$json = '{ "login": "directeur@imerir.com", "password": "imerir" }';
	//$parsed_json = json_decode($json);
	//$login =    $parsed_json -> {'login'};
	//$password = $parsed_json -> {'password'};

    $result = mysql_query( "SELECT * FROM USER WHERE mail =  '". $login ."'");

    $logOk = false;
    $passOk = false;

    $row = mysql_fetch_assoc($result);
    
    /* If login exist */
    if ($row['mail'] == $login && $login != null)
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
    	$id =  $row['id'] ;
    	$name =  $row['name'] ;
    	$nickname =  $row['nickname'] ;
    	$mail =  $row['mail'] ; 
    	$admin =  $row['admin'] ; 

        $isCo = isConnected();
        if(!$isCo)
        {
            createSession($id, $nickname, $name, $mail, $admin);
            $response = getJSONFromCodeError(200);           
        }
        else
        {
            $response = getJSONFromCodeError(303); 
        }
    }

	echo json_encode($response);

?>