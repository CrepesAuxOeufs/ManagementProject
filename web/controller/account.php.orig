<?php
	include 'message.php';
	include 'connect.php';
	
	/* 
	*/
	
	$jsonString = '	{
					"request": "save",
					"data": {
						"belbin": [
							{
								"name": "president",
								"value": "0"
							},
							{
								"name": "coequipier",
								"value": "0"
							},
							{
								"name": "eclaireur",
								"value": "0"
							},
							{
								"name": "faiseur",
								"value": "0"
							},
							{
								"name": "organisateur",
								"value": "0"
							},
							{
								"name": "evaluateur",
								"value": "0"
							},
							{
								"name": "creatif",
								"value": "0"
							},
							{
								"name": "finisseur",
								"value": "0"
							}
						],
						"skills": [
							{
								"name": "web",
								"value": "0"
							},
							{
								"name": "bdd",
								"value": "0"
							},
							{
								"name": "programmation",
								"value": "0"
							},
							{
								"name": "metier",
								"value": "0"
							},
							{
								"name": "marketing",
								"value": "0"
							}
						],
						"incompatibility": [
							{
								"id": "0"
							},
							{
								"id": "1"
							},
							{
								"id": "2"
							},
							{
								"id": "3"
							}
						]
					}
				}';

	/* ###########################
	* 			MAIN ACTION
	*  ########################### */
	$connexion = connectBDD();
	
	//$json = json_decode(file_get_contents("php://input"),true);
	
	$json = json_decode($jsonString,true);
	$request = $json["request"];
	$dataResponse = null;
	
	if($request ==  "getAllAccount"){
		$dataResponse = getUserList($json["raw"]);
	}
	else if($request ==  "save"){
		$dataResponse = saveUser($json["data"]);
	}
	else if($request ==  "createUser"){
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
	
	
	function saveUser($data){
		//BelBin
		foreach ($data["belbin"] as $belbin){ // president,coequipier,eclaireur,faiseur,organisateur,evaluateur,creatif,finisseur
			$id_belbin = mysql_query ("SELECT * FROM BELBIN WHERE name = '" . $belbin["name"] . "'");
			mysql_query ("INSERT INTO USER_BELBIN(user_id, belbin_id,value) VALUES ('" . getSessionID() . "','" . $id_belbin . "','" . $belbin["value"] . "')");
		}
		//Skills
		foreach ($data["skills"] as $skill){ // web,bdd,programmation,metier,marketing
			$id_skill = mysql_query ("SELECT * FROM SKILL WHERE name = '" . $skill["name"] . "'");
			mysql_query ("INSERT INTO USER_SKILL(user_id, skill_id,value) VALUES ('" . getSessionID() . "','" . $id_skill . "','" . $skill["value"] . "')");
		}
		//Incompatibility
		foreach ($data["incompatibility"] as $user_id_uncompatibility){ 
			mysql_query ("INSERT INTO USER_UNCOMPATIBILITY(user_id, user_id_uncompatibility) VALUES ('" . getSessionID() . "','" . $user_id_uncompatibility ."')");
		}
		
		return "";
	}
?>