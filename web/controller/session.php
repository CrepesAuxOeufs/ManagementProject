<?php
	/* 
	* Create session (login): createSession(5,"Sarah","CROCHE","sarah.croche@imerir.com");
	* Destroy current session (logout) : destroySession();
	* Test is user online : isConnected();
	*/
	session_start(); 
		
	function createSession($id,$name,$nickName,$mail){
		$_SESSION['id'] = $id;
		$_SESSION['name'] = $name;
		$_SESSION['nickname'] = $nickName;
		$_SESSION['mail'] = $mail;
		$_SESSION['connect'] = true;
		//echo 'Session created ' . $_SESSION['name'] .  ' ' . $_SESSION['nickName'] . '!<br>';
	}
	
	function destroySession(){
		$_SESSION['connect'] = false;
		session_destroy();
		//echo 'Session destroyed !<br>'
	}
	
	function isConnected(){
		if($_SESSION != null && $_SESSION['connect'] != null  && $_SESSION['connect'])
			return true;
		else
			return false;
	}
	
	function getSessionID(){
		return $_SESSION['id'];
	}
	function getSessionName(){
		return $_SESSION['name'];
	}
	function getSessionNickname(){
		return $_SESSION['nickname'];
	}
	function getSessionMail(){
		return $_SESSION['mail'];
	}
?>