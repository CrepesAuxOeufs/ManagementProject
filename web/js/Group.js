
var params_allGroups = {
							request: "getAllGroup",
							raw: ["name","user"]
						};
						
						

$.ajax(	{
		type: "POST",
		url: "../controller/account.php",
		data: JSON.stringify(params_allGroups),
		dataType: 'json',
		success: function(msg){
			console.log(msg);
			var groups = msg.data;
			for(group in groups){
				var group_id = groups[group].name;
				var group_name = groups[group].user;
				
			}
		}
});


//button for print list group
$("#profile_sumbit_incompatibility").click(function() {
	
});

