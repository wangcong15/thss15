$("#save_pass").click(function(){
        var new_password = $("#new_pass").val();
	$.ajax({
                type: "POST",
                url: "/api/new_pass/",
                data: {'new_pass': new_password},
                dataType: "json",
                success: function(data) {
                	if(data['status'] == 1){
                		$.cookie('asdf', data['new_password'], {path: '/'});
                		window.location.reload();
                	}
        			else{
        				alert("Fails!")
        			}
                        }
        });	
});

$("#update_profile").click(function(){
        var new_telep = $("#tel").val();
        var new_email = $("#email").val();
        $.ajax({
                type: "POST",
                url: "/api/update_profile/",
                data: {'new_telep': new_telep, 'new_email': new_email},
                dataType: "json",
                success: function(data) {
                        if(data['status'] == 1){
                                window.location.reload();
                        }
                                else{
                                        alert("Fails!")
                                }
                        }
        });
});

$("#update_info").click(function(){
        $.ajax({
        type: "GET",
        url: "/api/get_profile/",
        data: {},
        dataType: "json",
        success: function(data) {
                if(data['status'] == 1){
                        profile = data['profile'];
                        $("#tel").val(profile['tel']);
                        $("#email").val(profile['email']);
                }
        }
        });     
});

$('#send_fb').click(function(){
        var feed_back = $("#new_feedback").val();
        $.ajax({
        type: "GET",
        url: "/api/new_fb/",
        data: {'fb': feed_back},
        dataType: "json",
        success: function(data) {
                if(data['status'] == 1){
                        alert("Thanks for your suggestion!");
                        window.location.reload();
                }
        }
        }); 
})