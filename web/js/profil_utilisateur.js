var ObligatoryLogin = true;
var AutoHide = false;
var loadDashboard = true;
var loadUserListe = true;






$(document).ready(getSession);





$("#LogoutSubmit").click(function() {
	$.ajax(	{
			type: "GET",
			url: "../controller/logout.php",
			success: function(msg){
				console.log(msg);
				window.location.replace("index.html");
			}
	});
});

$("#LoginSubmit").click(function() {
//twitter bootstrap script
	
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
					setInterval(function()	{$('#myModal').modal('hide');window.location.replace("index.html"); },2000);
					logingHeaderAddMessage("Vous êtes maintenant connecté","success");
				}
				else
					logingHeaderAddMessage("erreur (" + msg.code + "): " + msg.message , "warning");
			},
			error: function(jqXHR, textStatus, errorThrown){
				logingHeaderAddMessage("erreur : " + jqXHR["status"]+" " + errorThrown , "warning");
			}
	});
	
});

//type info warning danger success
function logingHeaderAddMessage(msg,type){
	var uuid = generateUUID();
	console.log(uuid);
	$("#loginHeader").append('<div class="alert alert-'+type+' alert-dismissable" id="' + uuid+ '" style="margin:5px 5px 0px 5px;"> \
	<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>\
	'+msg+'. </div>');
	setInterval(function()	{document.getElementById(uuid).remove();},5000);
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

function getSession (){
	$.ajax(	{
			type: "POST",
			url: "../controller/session_req.php",
			dataType: 'json',
			success: function(msg){
				
				if(msg.data["admin"] == null )		$('#myModal').modal({backdrop:'static',keyboard:false, show:true});
				
				
				if(msg.data["admin"] == 1){
					$("#side-menu").load("module/menu-administration.html");
				}
				
				if(msg.data["admin"] == 0){
					//window.location.replace("profile.html");
					
				}
				

				if(AutoHide) 		{setInterval(function(){ $('#myModal').modal('hide');},2000);}

				//if(loadDashboard) {$('#contentContainer').load("module/dashboardAdmin.html");}
				//if(loadUserListe) {$('#contentContainer').load("module/listegroup.html");}
				
				
				
				
				console.log(msg);
				return msg;
			},
			error: function(jqXHR, textStatus, errorThrown){
				return null;
			}
	});
}


