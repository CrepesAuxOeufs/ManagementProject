<?php
	include 'message.php';
	include 'connect.php';
	include 'session.php';
	
	error_reporting(0);
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
								"value": "1"
							},
							{
								"name": "eclaireur",
								"value": "0"
							},
							{
								"name": "faiseur",
								"value": "10"
							},
							{
								"name": "organisateur",
								"value": "0"
							},
							{
								"name": "evaluateur",
								"value": "3"
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
								"value": "6"
							},
							{
								"name": "programmation",
								"value": "3"
							},
							{
								"name": "metier",
								"value": "1"
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
	
	$json = json_decode(file_get_contents("php://input"),true);
	//$json = json_decode($jsonString,true);
	
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
	else if ($request == "saveGroups"){
		$dataResponse = saveGroups($json["data"]);
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
		
		return "{}";
	}
	
	
	function saveUser($data){
		//BelBin
		foreach ($data["belbin"] as $belbin){ // president,coequipier,eclaireur,faiseur,organisateur,evaluateur,creatif,finisseur
			$id_belbin = mysql_fetch_assoc(mysql_query ("SELECT id FROM BELBIN WHERE name = '" . $belbin["name"] . "' limit 1"));
			mysql_query ("INSERT INTO USER_BELBIN(user_id, belbin_id,value) VALUES ('" . getSessionID() . "','" . $id_belbin["id"] . "','" . $belbin["value"] . "')");
		}
		//Skills
		foreach ($data["skills"] as $skill){ // web,bdd,programmation,metier,marketing
			$id_skill = mysql_fetch_assoc(mysql_query ("SELECT id FROM SKILL WHERE name = '" . $skill["name"] . "' limit 1"));
			mysql_query ("INSERT INTO USER_SKILL(user_id, skill_id,value) VALUES ('" . getSessionID() . "','" . $id_skill["id"] . "','" . $skill["value"] . "')");
		}
		//Incompatibility
		foreach ($data["incompatibility"] as $user_id_uncompatibility){ 
			mysql_query ("INSERT INTO USER_UNCOMPATIBILITY(user_id, user_id_uncompatibility) VALUES ('" . getSessionID() . "','" . $user_id_uncompatibility["id"] ."')");
		}
		
		return "{}";
	}
	
		function saveGroups($data)
	{
		//GROUP
		foreach($data["groups"] as $groups){ // Save group in BDD
			mysql_query ("INSERT INTO `GROUP`( `project_id`, `name`) VALUES ('".$groups["project_id"]."','".$groups["name"]."')");
			$id_group = mysql_fetch_assoc(mysql_query ("SELECT id FROM `GROUP` WHERE name = '" . $groups["name"] . "' limit 1"));
			echo "Id du group:			".$id_group["id"]."			";
			//USER_GROUP
			foreach($groups["user"] as $user){
				mysql_query ("INSERT INTO `USER_GROUP`( `user_id`, `group_id`) VALUES ('".$user["id"]."','".$id_group["id"]."')");
			}
		
		}
		return "{}";
	}
?>