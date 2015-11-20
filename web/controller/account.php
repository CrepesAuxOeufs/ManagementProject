<?php
	include 'message.php';
	include 'connect.php';
	include 'session.php';
	
	error_reporting(0);

	/* ###########################
	* 			MAIN ACTION
	*  ########################### */
	$connexion = connectBDD();
	
		
	/*
	$jsonString = '{
								"request": "removeUserFromGroup",
								"data": {"user_id":481}
							}';
	$jsonString = '{
								"request": "addUserToGroup",
								"data": {"user_id":481,"group_id":9}
							}';
	$jsonString = '{
								"request": "getUsersUngroup",
								"data": {}
							}';
	$jsonString = '{
								"request": "removeGroup",
								"data": {"group_id":9}
							}';
	$jsonString = '{
								"request": "createGroup",
								"data": {"group_name":"nouveau groupe"}
							}';
			*/	
	/*$jsonString = '{
								"request": "createGroup",
								"data": {"group_name":"nouveau groupe"}
							}';*/
			

	//$json = json_decode($jsonString,true);
	
	
	
	$json = json_decode(file_get_contents("php://input"),true);
	
	$request = $json["request"];
	$response = null;

	if($request ==  "getAllAccount"){
		$response = getUserList($json["userId"],$json["raw"],false);
	}
	else if($request ==  "getAllAccountReady"){
		$response = getUserList($json["userId"],$json["raw"],true);
	}
	else if($request ==  "save"){
		$response = saveUser($json["data"]);
	}
	else if($request ==  "createUser"){
		$response = createUser($json["raw"]);
	}
	else if ($request == "saveGroups"){
		$response = saveGroups($json["data"]);
	}
	else if ($request == "removeUserFromGroup"){
		$response = removeUserFromGroup($json["data"]);
	}
	else if ($request == "addUserToGroup"){
		$response = addUserToGroup($json["data"]);
	}
	else if ($request == "getUsersUngroup"){
		$response = getUsersUngroup($json["data"]);
	}
	else if ($request == "removeGroup"){
		$response = removeGroup($json["data"]);
	}
	else if ($request == "createGroup"){
		$response = createGroup($json["data"]);
	}
	else
		$response = getJSONFromCodeError(202);
	
	
	
	echo json_encode($response);
	
	
	/* ###########################
	* 			FUNCTIONS
	*  ########################### */
	
	function getUserList($userId,$data,$isReady){
		$users = array();
		$raw = "";
		$belbin = false;
		$skills = false;
		$uncompatibility = false;
		foreach ($data as $value)
			if($value == "belbin")
				$belbin = true;
			else if($value == "skills")
				$skills = true;
			else if($value == "uncompatibility")
				$uncompatibility = true;
			else
				$raw = $raw . $value .',';
		$raw = substr($raw,0,-1);
			
		if($userId != null)
			if($userId == -1 && getSessionID() != null)
				$result = mysql_query("SELECT ". $raw ." FROM USER WHERE USER.id = '". getSessionID() . "' AND admin = 0");
			else
				$result = mysql_query("SELECT ". $raw ." FROM USER WHERE USER.id = '". $userId . "' AND admin = 0");
		else
			if($isReady)
				$result = mysql_query("SELECT ". $raw ." FROM USER WHERE admin = 0 AND profil = 1");
			else
				$result = mysql_query("SELECT ". $raw ." FROM USER WHERE admin = 0");
			
        while($row = mysql_fetch_assoc($result))
        {
			$userInfo = array();
			foreach ($data as $value)
				if($value != "belbin" && $value != "skills" && $value != "uncompatibility")
					$userInfo[$value] = $row[$value];
					
			//BELBIN
			if($belbin){
				$belbins = array();
				$resultBelbin = mysql_query( "SELECT USER.id,USER.admin, USER.name,USER.nickname,BELBIN.id as belbin_id, USER_BELBIN.value as belbin_value,BELBIN.name as belbin_name
										FROM `USER`
										INNER JOIN `USER_BELBIN` ON USER.id = USER_BELBIN.user_id
										INNER JOIN `BELBIN` ON BELBIN.id  =  USER_BELBIN.belbin_id
										WHERE USER.id = '". $userInfo["id"] . "'");

				while($rowBelbin = mysql_fetch_assoc($resultBelbin))
				{
					$belbin = array();
					$belbin["id"] = $rowBelbin["belbin_id"];
					$belbin["value"] = $rowBelbin["belbin_value"];
					$belbin["name"] = $rowBelbin["belbin_name"];
					array_push($belbins, $belbin);
				}
				//print_r($belbins);
				$userInfo["belbin"] = $belbins;
			}
			
			//SKILL
			if($skills){
				$skills = array();
				$resultSkill = mysql_query( "SELECT USER.id,USER.name,USER.nickname,SKILL.id as skill_id, USER_SKILL.value as skill_value, SKILL.name as skill_name
											FROM `USER`
											INNER JOIN `USER_SKILL` ON USER.id =USER_SKILL.user_id
											INNER JOIN `SKILL` ON SKILL.id  =  USER_SKILL.skill_id
											WHERE USER.id = '". $userInfo["id"] . "'");

				while($rowSkill = mysql_fetch_assoc($resultSkill))
				{
					$skill = array();
					$skill["id"] = $rowSkill["skill_id"];
					$skill["value"] = $rowSkill["skill_value"];
					$skill["name"] = $rowSkill["skill_name"];
					array_push($skills, $skill);
				}
				//print_r($skills);
				$userInfo["skills"] = $skills;
			}
			//UNCOMPATIBILITY
			if($uncompatibility){
				$uncompatibilities = array();
				$resultUncompatibility = mysql_query( "SELECT USER_UNCOMPATIBILITY.user_id_uncompatibility,USERU.name,USERU.nickname
														FROM `USER`
														INNER JOIN `USER_UNCOMPATIBILITY` ON USER.id =USER_UNCOMPATIBILITY.user_id
														INNER JOIN `USER` as USERU ON USER_UNCOMPATIBILITY.user_id_uncompatibility =USERU.id

														WHERE USER.id = '". $userInfo["id"] . "'");

				while($rowUncompatibility = mysql_fetch_assoc($resultUncompatibility))
				{
					$uncompatibility = array();
					$uncompatibility["id"] = $rowUncompatibility["user_id_uncompatibility"];
					$uncompatibility["name"] = $rowUncompatibility["name"];
					$uncompatibility["nickname"] = $rowUncompatibility["nickname"];
					array_push($uncompatibilities, $uncompatibility);
				}
				$userInfo["uncompatibility"] = $uncompatibilities;
			}
		
			array_push($users, $userInfo);
			
		}
		
		if(	$users == null)
			$response = getJSONFromCodeError(202);
		else{
			$response = getJSONFromCodeError(200);
			$response["data"] = $users;
		}
		return $response;
	}
	
	function createUser($data){
		$name=$data['name'];
		$nickname=$data['nickname'];
		$mail=$data['mail'];
        $passwd=$data['password'];
		
		$result = mysql_query("INSERT INTO `USER`(`name`, `nickname`, `mail`, `password`) VALUES ('". $name ."','".$nickname."','". $mail ."','".$passwd."')");
		
		$response = getJSONFromCodeError(200);
		$response["data"] = "{}";
		return $response;
	}
	
	
	function saveUser($data){
		if(getSessionID() != null){
			$result = mysql_query( "SELECT profil FROM USER WHERE id =  '". getSessionID() ."'");
			$row = mysql_fetch_assoc($result);
			if($row['profil'] == 0){
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
				
				mysql_query ("UPDATE USER SET profil=true WHERE id='" . getSessionID() . "'");
				$_SESSION['profil'] = 1;
				$response = getJSONFromCodeError(200);
				return $response;
			}
			else{
				$response = getJSONFromCodeError(305);
				return $response;
			}
		}
		$response = getJSONFromCodeError(304);
		return $response;
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
		$response = getJSONFromCodeError(200);
		$response["data"] = "{}";
		return $response;
	}

	
	function removeGroup($data){
		mysql_query ("DELETE `USER_GROUP` WHERE group_id='" . $data["group_id"] . "'");
		mysql_query ("DELETE `GROUP` WHERE id='" . $data["group_id"] . "'");
		$response = getJSONFromCodeError(200);
		return $response;
	}
	function createGroup($data){
		$group  = mysql_fetch_assoc(mysql_query ("SELECT MAX( id ) AS group_id_max FROM `GROUP` WHERE 1"));
		$group_id = $group["group_id_max"] +1;
		mysql_query ("INSERT INTO `GROUP`(`id`,`project_id`,`name`) VALUES ('".$group_id."','1','".$data["group_name"]."')");
		$response = getJSONFromCodeError(200);
		return $response;
	}
	function addUserToGroup($data){
		$group  = mysql_fetch_assoc(mysql_query ("SELECT group_id AS group_id FROM `USER_GROUP` WHERE user_id = '". $data["user_id"] ."'"));
		$group_id = $group["group_id"];
		if($group_id == null){
			mysql_query ("INSERT INTO `USER_GROUP`( `group_id`, `user_id`) VALUES ('".$data["group_id"]."','".$data["user_id"]."')");
			calculGroupScore($data["group_id"]);
			}
		else{
			mysql_query ("UPDATE USER_GROUP SET group_id='" . $data["group_id"] . "' WHERE user_id='" . $data["user_id"] . "'");
			calculGroupScore($group_id);
			calculGroupScore($data["group_id"]);
			}
			
		$response = getJSONFromCodeError(200);
		return $response;
	}
	function removeUserFromGroup($data){
		$group_id = mysql_fetch_assoc(mysql_query("SELECT group_id FROM `USER_GROUP` WHERE user_id = '". $data["user_id"] ."'"));
		mysql_query ("DELETE `USER_GROUP` WHERE user_id='" . $data["user_id"] . "'");
		$response = getJSONFromCodeError(200);
		calculGroupScore($group_id);
		return $response;
	}

	function getUsersUngroup($data){
		$result = mysql_query("SELECT `USER`.id,`USER`.name,`USER`.nickname FROM `USER`
								LEFT JOIN USER_GROUP ON USER.id = USER_GROUP.user_id
								WHERE USER_GROUP.user_id IS NULL
								and USER.admin = 0 AND USER.profil = 1");
		$users = array();			
        while($row = mysql_fetch_assoc($result))
        {
			$userInfo = array();
			$userInfo["id"] = $row["id"];
			$userInfo["name"] = $row["name"];
			$userInfo["nickname"] = $row["nickname"];
			array_push($users,$userInfo);
		}
		$response = getJSONFromCodeError(200);
		$response["data"] = $users;
		return $response;
	}
	
		
	function calculGroupScore($group_id){
		$result = mysql_query( "SELECT `USER`.id
                            FROM `GROUP`, `USER`, `USER_GROUP` 
                            WHERE `GROUP`.id = `USER_GROUP`.group_id 
                            AND `USER`.id = `USER_GROUP`.user_id 
                            AND `GROUP`.project_id = '". $data["project_id"] . "'
							AND `GROUP`.id = '". $group_id . "'");
							
		$scoreGlobal = 0;
		$belbinScore = 0;
		$skillScore = 0;
		$nbUsers = 0;
		
        while($row = mysql_fetch_row($result))
        {
            $userID = $row[0];
			
			//BELBIN
			$resultBelbin = mysql_query( "SELECT USER.id,USER.admin, USER.name,USER.nickname,BELBIN.id as belbin_id, USER_BELBIN.value as belbin_value,BELBIN.name as belbin_name
									FROM `USER`
									INNER JOIN `USER_BELBIN` ON USER.id = USER_BELBIN.user_id
									INNER JOIN `BELBIN` ON BELBIN.id  =  USER_BELBIN.belbin_id
									WHERE USER.id = '". $userID . "'");

			while($rowBelbin = mysql_fetch_assoc($resultBelbin))
				$belbinScore += $rowBelbin["belbin_value"];
				
			//SKILLS
			$resultSkill = mysql_query( "SELECT USER.id,USER.name,USER.nickname,SKILL.id as skill_id, USER_SKILL.value as skill_value, SKILL.name as skill_name
										FROM `USER`
										INNER JOIN `USER_SKILL` ON USER.id =USER_SKILL.user_id
										INNER JOIN `SKILL` ON SKILL.id  =  USER_SKILL.skill_id
										WHERE USER.id = '". $userID . "'");

			while($rowSkill = mysql_fetch_assoc($resultSkill))
				$skillScore += $rowSkill["skill_value"] * 4;
			
			$nbUsers++;
        }
		
		$belbinScore = round( ($belbinScore / $nbUsers) * 100 ) /100;
		$skillScore = round( ($skillScore/ $nbUsers) * 100 ) /100;
		$scoreGlobal = round($belbinScore + $skillScore);
		
		mysql_query ("UPDATE `GROUP` SET score='" . $scoreGlobal . "' WHERE id='" . $group_id . "'");
		
	}
?>