<?php
	include 'message.php';
	include 'connect.php';
	include 'session.php';

	connectBDD();

	//$json = json_decode(file_get_contents("php://input"),true);
	$json = '{  "request": "showGroupsByProjectID", 
                "project_id": 1, 
                "name": "Group 1"
            }';


	$parsed_json = json_decode($json);

	$request =    $parsed_json -> {'request'};
	$project_id = $parsed_json -> {'project_id'};
    $name =   $parsed_json -> {'name'};

    echo '$json: ' . $json . ' <br> ';
    echo '$request: ' . $request . ' <br> ';
    echo '$project_id: ' . $project_id . ' <br> ';
    echo '$group_id: '. $name . ' <br> ';

    if ($request == 'showGroups')
    {
        getOneGroup($project_id, $name);
    }
    else if ($request == 'showGroupsByProjectID')
    {
        getAllGroup($project_id);
    }

    
    function getOneGroup($idProject, $nameGroup)
    {
        $result = mysql_query( "SELECT `GROUP`.name, `USER`.name
                            FROM `GROUP`, `USER`, `USER_GROUP` 
                            WHERE `GROUP`.id = `USER_GROUP`.group_id 
                            AND `USER`.id = `USER_GROUP`.user_id 
                            AND `GROUP`.project_id = '". $idProject ."'
                            AND `GROUP`.name = '" . $nameGroup . "'");

        if (!$result) 
        {
            echo "Impossible d'exécuter la requête dans la base : " . mysql_error();
            exit;
        }
        /*while($row = mysql_fetch_row($result))
        {
            echo $row[0] . ' ' . $row[1] . ' <br>';
        }*/


    }

    function getAllGroup($idProject)
    {
        $result = mysql_query( "SELECT `GROUP`.name, `USER`.name
                            FROM `GROUP`, `USER`, `USER_GROUP` 
                            WHERE `GROUP`.id = `USER_GROUP`.group_id 
                            AND `USER`.id = `USER_GROUP`.user_id 
                            AND `GROUP`.project_id = '". $idProject . "'");

        if (!$result) 
        {
            echo "Impossible d'exécuter la requête dans la base : " . mysql_error();
            exit;
        }

        /*while($row = mysql_fetch_row($result))
        {
            echo $row[0] . ' ' . $row[1] . ' <br>';
        }*/

        $groupArray = array();
        while($row = mysql_fetch_row($result))
        {

            $nameGroup = $row[0];

            $search = array_search($nameGroup, $groupArray);
            
            if ($search == false) 
            {
                array_push($groupArray, $nameGroup);
            }        
        }

        print_r($groupArray);

        return $groupArray;
    }



?>