<?php
	include 'message.php';
	include 'connect.php';
	/* 
	*/

	/* ###########################
	* 			MAIN ACTION
	*  ########################### */
	$connexion = connectBDD();
	$json = json_decode(file_get_contents("php://input"),true);
	$request = $json["request"];
	$dataResponse = null;
	
	if($request ==  "getAllAccount"){
		$dataResponse = getUserList($json["raw"]);
	}
	if($request ==  "createUser"){
		$dataResponse = createUser($json["raw"]);
	}
	if($dataResponse == null)
		$response = getJSONFromCodeError(202);
	else{
		$response = getJSONFromCodeError(200);
		$response["data"] = $dataResponse;
	}
	echo json_encode($response);
	
	
	/* ###########################
	* 			FUNCTIONS
	*  ########################### */
	
	function getUserList($data){
		$raw = "";
		foreach ($data as $value)
			$raw = $raw . $value .',';
		$raw = substr($raw,0,-1);
		
        $result = mysql_query("SELECT ". $raw ." FROM USER");
		$users = array();
        while($row = mysql_fetch_assoc($result))
        {
			$userInfo = array();
			foreach ($data as $value)
				$userInfo[$value] = $row[$value];
			array_push($users, $userInfo);
		}
		
		return $users;
	}
	
	function createUser($data){
		$name=$data['name'];
		$nickname=$data['nickname'];
		$mail=$data['mail'];
        $passwd=$data['password'];
		
		$result = mysql_query("INSERT INTO `USER`(`name`, `nickname`, `mail`, `password`) VALUES ('". $name ."','".$nickname."','". $mail ."','".$passwd."')");
		
		return "";
	}
	
	
?>