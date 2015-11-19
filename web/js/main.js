

//$(document).ready(getSession);






$(document).ready(main);


function main(){
	$("#LogoutSubmit").click(logout);
	$("#LoginSubmit").click(try_login);

	load_main_page(current_page);
	
	updateSession();
	
}






