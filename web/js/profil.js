
var params_allUsers = {
							request: "getAllAccount",
							raw: ["id","name","nickname"]
						};
						
						
$(document).ready(function(){
	// Remplissage des listes d'incompatibilité
	$.ajax(	{
		type: "POST",
		url: "../controller/account.php",
		data: JSON.stringify(params_allUsers),
		dataType: 'json',
		success: function(msg){
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
		}
	});
	
	//Remplissage infos profils
	
	var params_Info = {
								request: "getAllAccount",
								raw: ["id","name","nickname","mail","password"],
								"userId" : -1
							};
	$.ajax(	{
		type: "POST",
		url: "../controller/account.php",
		data: JSON.stringify(params_allUsers),
		dataType: 'json',
		success: function(msg){
			var userInfo = msg.data;
			console.log(userInfo);
			/*{"success":true,"code":200,"message":"ok",
			"data":[{"id":"421","name":"EtudiantName26","nickname":"EtudiantNickname26",
					"mail":"etudiant26@imerir.com","password":"password26",
					"belbin":[{"id":"1","value":"4","name":"Organisateur"},
								{"id":"2","value":"3","name":"President"},
								{"id":"3","value":"6","name":"Faiseur"},
								{"id":"4","value":"9","name":"Creatif"},
								{"id":"5","value":"3","name":"Eclaireur"},
								{"id":"6","value":"0","name":"Evaluateur"},
								{"id":"7","value":"1","name":"Coequipier"},
								{"id":"8","value":"7","name":"Finisseur"}],
					"skills":[{"id":"1","value":"1","name":"Web"},
						{"id":"2","value":"3","name":"BDD"},
						{"id":"3","value":"2","name":"Programmation"},
						{"id":"4","value":"2","name":"Metier"},
						{"id":"5","value":"6","name":"Marketing"}],
					"uncompatibility":[{"id":"400"},{"id":"410"},{"id":"455"}]}]} */
					
			document.getElementById("profile_belbin_president").value 	= userInfo.belbin[0].value;
			document.getElementById("profile_belbin_coequipier").value 	= userInfo.belbin[1].value;
			document.getElementById("profile_belbin_eclaireur").value 	= userInfo.belbin[2].value;
			document.getElementById("profile_belbin_faiseur").value 	= userInfo.belbin[3].value;
			document.getElementById("profile_belbin_organsiateur").value = userInfo.belbin[4].value;
			document.getElementById("profile_belbin_evaluateur").value 	= userInfo.belbin[5].value;
			document.getElementById("profile_belbin_creatif").value 	= userInfo.belbin[6].value;
			document.getElementById("profile_belbin_finisseur").value 	= userInfo.belbin[7].value;
			
			document.getElementById("profile_skill_web").value 			= userInfo.skills[0].value;
			document.getElementById("profile_skill_bdd").value 			= userInfo.skills[1].value;
			document.getElementById("profile_skill_programmation").value = userInfo.skills[2].value;
			document.getElementById("profile_skill_metier").value 		= userInfo.skills[3].value;
			document.getElementById("profile_skill_marketing").value 	= userInfo.skills[4].value;
			
			
			var table = document.getElementById("profile_tab_incompatibility");
			for(uncompatibility in userInfo.uncompatibility){
				var row = table.insertRow();
				var cell0 = row.insertCell(0); cell0.innerHTML = uncompatibility[0].id;
				//var cell1 = row.insertCell(1); cell1.innerHTML = selected.profile_name;
				//var cell2 = row.insertCell(2); cell2.innerHTML = selected.profile_nickname;
			}
		}
	});
})

$("#profile_sumbit_incompatibility").click(function() {
	var table = document.getElementById("profile_tab_incompatibility");
	if(table.rows.length <= 4){
		var selected = document.getElementById("select_incompatibility").options[document.getElementById("select_incompatibility").selectedIndex];
		
		var row = table.insertRow();
		var cell0 = row.insertCell(0); cell0.innerHTML = selected.profile_id;
		var cell1 = row.insertCell(1); cell1.innerHTML = selected.profile_name;
		var cell2 = row.insertCell(2); cell2.innerHTML = selected.profile_nickname;
	}
});



$("#profile_sumbit_save").click(function() {
	var incompatibilities = document.getElementById("profile_tab_incompatibility").rows;
	
	var data_belbin = [];
	data_belbin.push({name : "president", value: document.getElementById("profile_belbin_president").value});
	data_belbin.push({name : "coequipier", value: document.getElementById("profile_belbin_coequipier").value});
	data_belbin.push({name : "eclaireur", value: document.getElementById("profile_belbin_eclaireur").value});
	data_belbin.push({name : "faiseur", value: document.getElementById("profile_belbin_faiseur").value});
	data_belbin.push({name : "organisateur", value: document.getElementById("profile_belbin_organsiateur").value});
	data_belbin.push({name : "evaluateur", value: document.getElementById("profile_belbin_evaluateur").value});
	data_belbin.push({name : "creatif", value: document.getElementById("profile_belbin_creatif").value});
	data_belbin.push({name : "finisseur", value: document.getElementById("profile_belbin_finisseur").value});
	
	var data_skills = [];
	data_skills.push({name : "web", value: document.getElementById("profile_skill_web").value});
	data_skills.push({name : "bdd", value: document.getElementById("profile_skill_bdd").value});
	data_skills.push({name : "programmation", value: document.getElementById("profile_skill_programmation").value});
	data_skills.push({name : "metier", value: document.getElementById("profile_skill_metier").value});
	data_skills.push({name : "marketing", value: document.getElementById("profile_skill_marketing").value});
	
	var data_imcompatibility = [];
	for(row in incompatibilities)
		if(incompatibilities[row].cells != null && incompatibilities[row].cells[0].innerHTML != "#")
			data_imcompatibility.push({id : incompatibilities[row].cells[0].innerHTML});
			
			
	
	var data = {
							request: "save",
							data: {
									belbin: data_belbin,
									skills: data_skills,
									incompatibility: data_imcompatibility
									}
				};	
		
	$.ajax(	{
			type: "POST",
			url: "../controller/account.php",
			data: JSON.stringify(data),
			dataType: 'json',
			success: function(msg){
				current_page = Page.alreadyRegistred;
				load_main_page(current_page);
				console.log(msg);
			}
	});
});

function removeOptions(selectbox)
{
    var i;
    for(i=selectbox.options.length-1;i>=0;i--)
    {
        selectbox.remove(i);
    }
}