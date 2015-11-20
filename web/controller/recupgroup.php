<?php
	include 'message.php';
	include 'connect.php';
	include 'session.php';

	connectBDD();

	$json = json_decode(file_get_contents("php://input"),true);
	
	$request = $json["request"];
	$dataResponse = null;
	

    if ($request == 'showGroups'){
        $dataResponse = getAllGroup($json["data"]);
    }
    if ($request == 'showGroupsOnly'){
        $dataResponse = getAllGroupOnly($json["data"]);
    }

   if($dataResponse == null)
		$response = getJSONFromCodeError(202);
	else{
		$response = getJSONFromCodeError(200);
		$response["data"] = $dataResponse;
	}
	
	echo json_encode($response);

	
    function getAllGroup($data)
    {
        $result = mysql_query( "SELECT `GROUP`.id,`GROUP`.name,`GROUP`.score, `USER`.id,`USER`.name,`USER`.nickname
                            FROM `GROUP`, `USER`, `USER_GROUP` 
                            WHERE `GROUP`.id = `USER_GROUP`.group_id 
                            AND `USER`.id = `USER_GROUP`.user_id 
                            AND `GROUP`.project_id = '". $data["project_id"] . "'");

        if (!$result) 
        {
            echo "Impossible d'exécuter la requête dans la base : " . mysql_error();
            exit;
        }

        $groupArrayName = array();
        $groupArray = array();
		
        while($row = mysql_fetch_row($result))
        {
            $idGroup = $row[0];
            $nameGroup = $row[1];
            $scoreGroup = $row[2];
            $userID = $row[3];
            $useName = $row[4];
            $userNickname = $row[5];
			//BELBIN
			$belbins = array();
			$belbinScore = 0;
			$resultBelbin = mysql_query( "SELECT USER.id,USER.admin, USER.name,USER.nickname,BELBIN.id as belbin_id, USER_BELBIN.value as belbin_value,BELBIN.name as belbin_name
									FROM `USER`
									INNER JOIN `USER_BELBIN` ON USER.id = USER_BELBIN.user_id
									INNER JOIN `BELBIN` ON BELBIN.id  =  USER_BELBIN.belbin_id
									WHERE USER.id = '". $userID . "'");

			while($rowBelbin = mysql_fetch_assoc($resultBelbin))
			{
				$belbin = array();
				$belbin["id"] = $rowBelbin["belbin_id"];
				$belbin["value"] = $rowBelbin["belbin_value"];
				$belbin["name"] = $rowBelbin["belbin_name"];
				$belbinScore += $rowBelbin["belbin_value"];
				array_push($belbins, $belbin);
			}
			//SKILLS
			$skills = array();
			$skillScore = 0;
			$resultSkill = mysql_query( "SELECT USER.id,USER.name,USER.nickname,SKILL.id as skill_id, USER_SKILL.value as skill_value, SKILL.name as skill_name
										FROM `USER`
										INNER JOIN `USER_SKILL` ON USER.id =USER_SKILL.user_id
										INNER JOIN `SKILL` ON SKILL.id  =  USER_SKILL.skill_id
										WHERE USER.id = '". $userID . "'");

			while($rowSkill = mysql_fetch_assoc($resultSkill))
			{
				$skill = array();
				$skill["id"] = $rowSkill["skill_id"];
				$skill["value"] = $rowSkill["skill_value"];
				$skill["name"] = $rowSkill["skill_name"];
				$skillScore += $rowSkill["skill_value"] * 4;
				array_push($skills, $skill);
			}			
				
				
			$found = null;
			foreach($groupArray as &$group){
				if($group["name"] == $nameGroup){
					$found=$group;
				}
			}
			
			if($found == null){
				$found = array();
				$found["id"] = $idGroup;
				$found["name"] = $nameGroup;
				$found["users"] = array(); 
				$found["scoreGlobal"] = $scoreGroup;
				$found["scoreBelbin"] = 0 ;
				$found["scoreSkill"] = 0 ;
				array_push($groupArray, $found);
			}
				
				
			$user = array();
			$user["id"] = $userID;
			$user["name"] = $useName;
			$user["nickname"] = $userNickname;
			$user["belbin"] = $belbins;
			$user["skills"] = $skills;
			
			foreach($groupArray as &$group){
				if($group["name"] == $nameGroup){
					$group["scoreBelbin"] += $belbinScore;
					$group["scoreSkill"] += $skillScore;
					array_push($group["users"], $user);
				}
			}
			
        }
		
		foreach($groupArray as &$group){
			$group["scoreBelbin"] = round( ($group["scoreBelbin"] / count($group["users"])) * 100 ) /100;
			$group["scoreSkill"] = round( ($group["scoreSkill"] / count($group["users"])) * 100 ) /100;
		}
		
        return $groupArray;
    }

    function getAllGroupOnly($data)
    {
        $result = mysql_query( "SELECT id,name FROM `GROUP` WHERE project_id = '". $data["project_id"] . "'");
        $groupArray = array();
		
        while($row = mysql_fetch_assoc($result))
        {
			$group = array();
            $group["id"]  = $row["id"];
            $group["name"]  = $row["name"];
			array_push($groupArray, $group);
        }
        return $groupArray;
    }



?>