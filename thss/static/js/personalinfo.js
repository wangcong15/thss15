var dom_username = $("#user_name");
var dom_score_container = $("#score_container")
var user_name = "";
var dom_table = $("#search_table");
var dom_date_period = $("#date_period");
var dom_rank_container = $("#rank_container");

$("#search_score").click(function(){
	user_name = dom_username.val();
	$.ajax({
        type: "GET",
        url: "/api/stu_scores/",
        data: {'stuname': user_name},
        dataType: "json",
        success: function(data) {
        	if(data['status'] == 1){
        		dom_score_container.children().remove();
        		var data_arr = data['scores'];
        		for(i in data_arr){
        			var dom_td = "<tr><td>" + data_arr[i]['StuId'] + "</td><td>" + data_arr[i]['StuName'] + "</td><td>" + data_arr[i]['CourseName'] + "</td><td>" + data_arr[i]['Score'] + "</td><td>" + data_arr[i]['Weigh'] + "</td><td>" + data_arr[i]['Style'] + "</td></tr>";
        			dom_score_container.append(dom_td);
        		}
        		dom_table.fadeIn();
        	}
			else{
				alert("Fails!")
			}
        }
	});	
});

dom_date_period.change(function(){
	var new_date = dom_date_period.val();
	if(new_date == "All The Time"){
		rank_it(0);
	}
	else{
		rank_it(2);
	}
});

$("#show_rank").one("click", function(){
	rank_it(0)
});

var rank_it = function(flag){
	$.ajax({
        type: "GET",
        url: "/api/stu_rank/",
        data: {'flag': flag},
        dataType: "json",
        success: function(data) {
        	if(data['status'] == 1){
        		dom_rank_container.children().remove();
	    		data_arr = data['rank']
	    		for(i in data_arr){
	    			if(data_arr[i]['failNum'] == 0){
		    			var dom_td = "<tr style='color:blue'><td>" + data_arr[i]['stuName'] + "</td><td>" + data_arr[i]['averScore'] + "</td><td>" + data_arr[i]['rank'] + "</td><td>" + data_arr[i]['failNum'] + "</td><td>" + data_arr[i]['totalWeigh'] + "</td></tr>";
		    		}
		    		else{
		    			var dom_td = "<tr style='color:red'><td>" + data_arr[i]['stuName'] + "</td><td>" + data_arr[i]['averScore'] + "</td><td>" + data_arr[i]['rank'] + "</td><td>" + data_arr[i]['failNum'] + "</td><td>" + data_arr[i]['totalWeigh'] + "</td></tr>";
		    		}
	    			dom_rank_container.append(dom_td);
	    		}
	    	}
	    	else{
	    		alert('Fails!');
	    	}
        }
	});	
}