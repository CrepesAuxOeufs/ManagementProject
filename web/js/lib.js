var AccountType = { unconnected:0,admin:1,classic:2};
var Page = {none:0, login:1, profile:2, admin:3};

current_user = AccountType.unconnected;
current_page = Page.login;

function updateSession (){
	$.ajax(	{
			type: "POST",
			url: "../controller/session_req.php",
			dataType: 'json',
			success: function(msg){
				
				/*if(msg.data["admin"] == null )		$('#myModal').modal({backdrop:'static',keyboard:false, show:true});
				
				
				if(msg.data["admin"] == 1){
					console.log("show");
					$("#menu_admin").show();
					//window.location.replace("users.html");
				}
				
				if(msg.data["admin"] == 0){
					//window.location.replace("profil_utilisateur.html");
					
				}
				

				if(AutoHide) 		{setInterval(function(){ $('#myModal').modal('hide');},2000);}

				if(loadDashboard) {$('#contentContainer').load("module/dashboardAdmin.html");}
				if(loadUserListe) {$('#contentContainer').load("module/listegroup.html");}
				
				*/
				
				if(msg.data["admin"] == null)
					current_user = AccountType.unconnected;
				else if (msg.data["admin"] == 0)
					current_user = AccountType.classic;
				else
					current_user = AccountType.admin;
				
				displayAccountPage();
				
				console.log(current_user);
				
				console.log(msg);
				return msg;
			},
			error: function(jqXHR, textStatus, errorThrown){
				return null;
			}
	});
}

function generateUUID(){
    var d = new Date().getTime();
    if(window.performance && typeof window.performance.now === "function"){
        d += performance.now();; //use high-precision timer if available
    }
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (d + Math.random()*16)%16 | 0;
        d = Math.floor(d/16);
        return (c=='x' ? r : (r&0x3|0x8)).toString(16);
    });
    return uuid;
}



//type info warning danger success
function logingHeaderAddMessage(msg,type){
	var uuid = generateUUID();
	console.log(uuid);
	$("#loginHeader").append('<div class="alert alert-'+type+' alert-dismissable" id="' + uuid+ '" style="margin:5px 5px 0px 5px;"> \
	<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>\
	'+msg+'. </div>');
	setTimeout(function()	{document.getElementById(uuid).remove();},5000);
}

function generateUUID(){
    var d = new Date().getTime();
    if(window.performance && typeof window.performance.now === "function"){
        d += performance.now();; //use high-precision timer if available
    }
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (d + Math.random()*16)%16 | 0;
        d = Math.floor(d/16);
        return (c=='x' ? r : (r&0x3|0x8)).toString(16);
    });
    return uuid;
}

function logout(){
	$.ajax(	{
			type: "GET",
			url: "../controller/logout.php",
			success: function(msg){
				console.log(msg);
				window.location.replace("index.html");
			}
	});
}

function try_login(){
	console.log("try_login");
	
	if(document.getElementById("login_email").value == "" || document.getElementById("login_password").value == ""){
				logingHeaderAddMessage("erreur : Email ou mot de passe non rempli", "warning");
				return;
	}
	
	var arr = { login: document.getElementById("login_email").value, password: document.getElementById("login_password").value };
	
	$.ajax(	{
			type: "POST",
			url: "../controller/login.php",
			data: JSON.stringify(arr),
			dataType: 'json',
			success: function(msg){
				console.log(msg);
				if(msg["success"] == true){
					setTimeout(function()	{$('#myModal').modal('hide');window.location.replace("index.html"); },2000);
					logingHeaderAddMessage("Vous êtes maintenant connecté","success");
					updateSession();
					load_main_page(Page.none);
					
					
				}
				else{
					logingHeaderAddMessage("erreur (" + msg.code + "): " + msg.message , "warning");
					updateSession();
					load_main_page(Page.none);
				}
					
			},
			error: function(jqXHR, textStatus, errorThrown){
				logingHeaderAddMessage("erreur : " + jqXHR["status"]+" " + errorThrown , "warning");
			}
	});
}

function load_main_page(page){
	switch(page){
		case Page.none:
			$('#contentContainer').load("module/blank.html");
		break;
		case Page.login:
			
			$('#contentContainer').load("module/login.html");
			
		break;
		
		case Page.profile:
		$('#contentContainer').load("module/profil.html");
		
		break;
		
		case Page.admin:
		$('#contentContainer').load("module/user.html");
		
		break;
		
		
	}
}


function displayAccountPage(){
		if(current_user == AccountType.classic)
			current_page = Page.profile;
		else if(current_user == AccountType.admin)
			current_page = Page.admin;
		
		console.log(current_user);
		console.log(current_page);
		update_menu();
		load_main_page(current_page);
}

function update_menu(){
	if(current_user == AccountType.classic){
		display_navbar(true);
		display_sidebar(true);
		display_menuAdmin(false);
	}
	else if(current_user == AccountType.admin){
		display_navbar(true);
		display_sidebar(true);
		display_menuAdmin(true);
	}
}





function display_navbar(display){
	if (display == true){
		$("#navbar").show();
	}
	else
		$("#navbar").hide();
}
function display_sidebar(display){
	if (display == true){
		$("#sidebar").show();
	}
	else
		$("#sidebar").hide();
}
function display_menuAdmin(display){
	
	if (display == true){
		$("#menu_admin").show();
	}
	else
		$("#menu_admin").hide();
}




