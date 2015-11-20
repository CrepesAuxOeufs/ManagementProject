<?php
	include 'message.php';
	include 'connect.php';

	connectBDD();

	/* for test */
	/*
    $jsonString = '{
    			"request":"generateGroups",
    			"data":{
    					"nbGroup":"10",
						"type":"basic"
    					}
    		}';

	$json = json_decode($jsonString,true);
	*/
	
	$json = json_decode(file_get_contents("php://input"),true);
	$request = $json["request"];
	if($request !=  "generateGroups"){
		$response = getJSONFromCodeError(202);
		echo json_encode($response);
		return;
	}
	
	$nbGroup = $json["data"]["nbGroup"];
	// Preparation
	$userIdList = getIdUserList();
	$usersCaracterisitcs = getUserCaracteristics($userIdList);
	
	$data = array(); 
	$data["nbGroup"] = $nbGroup;
	$data["nbIteration"] = $json["data"]["nbIteration"];
	$data["users"] = $usersCaracterisitcs;
	$response = getJSONFromCodeError(200);
	$response["data"] = $data;
	$file = 'generator/data.json';
	$current = file_get_contents($file);
	$current = json_encode($data,true);
	file_put_contents($file, $current);
	// Generation + sauvegarde
	$data = exec("py ./generator/".$json["data"]["type"].".py");
	// Reponse
	
	if($data == null || $data == "")
		$response = getJSONFromCodeError(600);
	else{
		saveGroup(json_decode($data, true));
		$response = getJSONFromCodeError(200);
	}
	echo json_encode($response);
	
function saveGroup($data){
	mysql_query("DELETE FROM `GROUP`");
	mysql_query("DELETE FROM `USER_GROUP`");
	foreach ($data["groups"] as $group){
		mysql_query("INSERT INTO `GROUP`(`id`,`project_id`, `name`, `score`) VALUES ('". $group["id"] ."','". 1 ."','". $group["name"] ."', '". $group["score"] ."')");
	}
	foreach ($data["users"] as $user){
		mysql_query("INSERT INTO `USER_GROUP`(`user_id`, `group_id`) VALUES ('". $user["id"] ."','". $user["groupId"] ."')");
	}
}


function getIdUserList()
{		
    $result = mysql_query("SELECT id FROM USER WHERE admin = 0 AND profil = 1");

	$users = array();

    while($row = mysql_fetch_assoc($result))
    {
		$user = array();
		$user["id"] = $row['id'];
		$user["belbin"] = array();
		$user["skills"] = array();
		$user["uncompatibility"] = array();
		array_push($users, $user);
	}
	
	return $users;
}

function getUserCaracteristics($userIdList)
{		
	$users = array();
	foreach($userIdList as &$user){
		//BELBIN
        $resultBelbin = mysql_query( "SELECT USER.id,USER.name,USER.nickname,BELBIN.id as belbin_id, USER_BELBIN.value as belbin_value,BELBIN.name as belbin_name
								FROM `USER`
								INNER JOIN `USER_BELBIN` ON USER.id =USER_BELBIN.user_id
								INNER JOIN `BELBIN` ON BELBIN.id  =  USER_BELBIN.belbin_id
								WHERE USER.id = '". $user["id"] . "'");

		while($rowBelbin = mysql_fetch_assoc($resultBelbin))
		{
			$belbin = array();
			$belbin["id"] = $rowBelbin["belbin_id"];
			$belbin["value"] = $rowBelbin["belbin_value"];
			$belbin["name"] = $rowBelbin["belbin_name"];
			array_push($user["belbin"], $belbin);
		}
		//SKILL
		$resultSkill = mysql_query( "SELECT USER.id,USER.name,USER.nickname,SKILL.id as skill_id, USER_SKILL.value as skill_value, SKILL.name as skill_name
									FROM `USER`
									INNER JOIN `USER_SKILL` ON USER.id =USER_SKILL.user_id
									INNER JOIN `SKILL` ON SKILL.id  =  USER_SKILL.skill_id
									WHERE USER.id = '". $user["id"] . "'");

		while($rowSkill = mysql_fetch_assoc($resultSkill))
		{
			$skill = array();
			$skill["id"] = $rowSkill["skill_id"];
			$skill["value"] = $rowSkill["skill_value"];
			$skill["name"] = $rowSkill["skill_name"];
			array_push($user["skills"], $skill);
		}
		
		//UNCOMPATIBILITY
		$resultUncompatibility = mysql_query( "SELECT USER.id,USER.name,USER.nickname, USER_UNCOMPATIBILITY.user_id_uncompatibility
									FROM `USER`
									INNER JOIN `USER_UNCOMPATIBILITY` ON USER.id =USER_UNCOMPATIBILITY.user_id
									WHERE USER.id = '". $user["id"] . "'");

		while($rowUncompatibility = mysql_fetch_assoc($resultUncompatibility))
		{
			$uncompatibility = array();
			$uncompatibility["id"] = $rowUncompatibility["user_id_uncompatibility"];
			array_push($user["uncompatibility"], $uncompatibility);
		}
		
		//echo json_encode($users) . '<br><br>';
		array_push($users, $user);
	}
	return $users;
}

?>