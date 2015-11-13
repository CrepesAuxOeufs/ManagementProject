var ObligatoryLogin = true;
var AutoHide = true;
var loadDashboard = true;


if(ObligatoryLogin)		$('#myModal').modal({backdrop:'static',keyboard:false, show:true});

if(AutoHide) 		{setInterval(function(){ $('#myModal').modal('hide');},2000);}

if(loadDashboard) {$('#page-wrapper>div>div').load("module/dashboardAdmin.html");}




$("#LoginSubmit").click(function() {
//twitter bootstrap script
	
		
	var arr = { login: $("#Loginlogin").value, password: $("#Loginpassword").value }
	$.ajax(	{
			type: "POST",
			url: "../controller/login.php",
			data: JSON.stringify(arr),
			contentType: 'application/json; charset=utf-8',
			dataType: 'json',
			success: function(msg){
				console.log(msg);
				logingHeaderAddMessage(msg,"success");
				
				if(msg["success"] == true){
					setInterval(function()	{
												$('#myModal').modal('hide');
											},2000);
					
				}
				
			},
			error: function(jqXHR, textStatus, errorThrown){
				console.log(jqXHR);
				console.log(textStatus);
				console.log(errorThrown);
				
				logingHeaderAddMessage("erreur : " + jqXHR["status"]+" " + errorThrown , "warning");
				
			}
	});
	
});
//type info warning danger success
function logingHeaderAddMessage(msg,type){
	
	$("#loginHeader").append('<div class="alert alert-'+type+' alert-dismissable" style="margin:5px 5px 0px 5px;"> \
	<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>\
	'+msg+'. </div>');
				
}


