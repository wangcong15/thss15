var current_user = ""
$("#create_new").click(function(){
  	new_username = $("#new_username").val();
  	new_rank = $("#new_rank option:selected").index();
  	$.ajax({
        type: "POST",
        url: "/api/create_new/",
        data: {'new_username': new_username, 'new_rank': new_rank},
        dataType: "json",
        success: function(data) {
        	if(data['status'] == 1){
        		window.location.reload();	
        	}
			else{
				alert("Creation Fails!")
			}
        }
	});	
});

$("#update_profile").click(function(){
  	mstuid = $("#stuid").val();
	mclass = $("#class").val();
	mtel = $("#tel").val();
	memail = $("#email").val();
  	$.ajax({
        type: "POST",
        url: "/api/update_profile/",
        data: {'stuid': mstuid, 'class': mclass, 'tel': mtel, 'email': memail, 'current_user': current_user},
        dataType: "json",
        success: function(data) {
        	if(data['status'] != 1){
				alert("Update Fails!")
			}
			$('#myModal2').modal('hide')
        }
	});	
});

$(".delete_user").click(function(){
	deleted_user = $(this).attr("data");
	$.ajax({
        type: "POST",
        url: "/api/delete_user/",
        data: {'username': deleted_user},
        dataType: "json",
        success: function(data) {
        	if(data['status'] == 1){
        		window.location.reload();
        	}
			else{
				alert("Deleting Fails!")
			}
        }
	});	
});

$(".reset_pass").click(function(){
    reset_user = $(this).attr("data");
    $.ajax({
        type: "POST",
        url: "/api/reset_pass/",
        data: {'username': reset_user},
        dataType: "json",
        success: function(data) {
            if(data['status'] == 1){
                alert("Reset Succeeds!")
            }
            else{
                alert("Deleting Fails!")
            }
        }
    }); 
});

$(".edit_profile").click(function(){
	username = $(this).text();
	current_user = username;
	$.ajax({
        type: "GET",
        url: "/api/get_profile/",
        data: {'username': username},
        dataType: "json",
        success: function(data) {
        	if(data['status'] == 1){
	        	profile = data['profile'];
	        	$("#stuid").val(profile['stuid']);
	        	$("#class").val(profile['class']);
	        	$("#tel").val(profile['tel']);
	        	$("#email").val(profile['email']);
	        }
        }
	});	
});