var dom_date_period = $("#date_period");
var dom_rank_container = $("#rank_container");
var flag_first_click = 1;

dom_date_period.change(function(){
	var new_date = dom_date_period.val();
	if(new_date == "All The Terms"){
		rank_it(0);
	}
	else if(new_date == "Last Year"){
		rank_it(1);
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