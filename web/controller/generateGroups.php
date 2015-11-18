<?php
	include 'message.php';
	include 'connect.php';

	connectBDD();

	/* for test */
    $json = '{
    			"request":"generateGroups",
    			"data":{
    					"nbGroup":"7"
    					}
    		}';

	$parsed_json = json_decode($json);
	$nbGroup = $parsed_json -> {'data'} -> {'nbGroup'};

	echo "json : " . $json . "<br>";
	echo "nbGroup : " . $nbGroup . "<br>";

	
	$userIdList = getIdUserList();
	$usersCaracterisitcs = getUserCaracteristics($userIdList);
	
	$data = array(); 
	$data["nbGroup"] = $nbGroup;
	$data["users"] = $usersCaracterisitcs;
	$response = getJSONFromCodeError(200);
	$response["data"] = $data;
	
	echo json_encode($response);
	

function getIdUserList()
{		
    $result = mysql_query("SELECT id FROM USER WHERE admin = 0");

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