
var params_allGroups = {
							request: "showGroups",
							data: {project_id:1}
						};
						
						

$.ajax(	{
		type: "POST",
		url: "../controller/recupgroup.php",
		data: JSON.stringify(params_allUsers),
		dataType: 'json',
		success: function(msg){
			console.log(msg);
			/*
			var users = msg.data;
			removeOptions(document.getElementById("select_incompatibility"));
			for(user in users){
				var user_id = users[user].id;
				var user_name = users[user].name;
				var user_nickname = users[user].nickname;
				
				var option = document.createElement("option");
				option.text = user_name + " " + user_nickname;
				option.profile_name = user_name;
				option.profile_nickname = user_nickname;
				option.profile_id = user_id;
				document.getElementById("select_incompatibility").add(option);
			}
			*/
		}
});
