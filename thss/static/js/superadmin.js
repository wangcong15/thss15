var dom_score = $("#scores");
var score_record = ""
$("#save_score").click(function(){
	var score_record = dom_score.val();
	var result = split_score(score_record);
	console.log(result);
	$.ajax({
        type: "POST",
        url: "/api/add_score/",
        data: {'stuid': result['stuid'], 'cname': result['cname'], 'score': result['score'], 'weigh': result['weigh'], 'style': result['style'], 'terms': result['terms']},
        dataType: "json",
        success: function(data) {
        	if(data['status'] == 1){
        		window.location.reload();	
        	}
			else{
				alert("Added Fails!")
			}
        }
	});	
});

var split_score = function(score){
	var result = {};
	var stuid_arr = [];
	var cname_arr = [];
	var score_arr = [];
	var weigh_arr = [];
	var style_arr = [];
	var terms_arr = [];
	var scores = score.trim().split("\n");
	var each_score_array;
	for(each_score in scores){
		each_score_array = scores[each_score].split("	");
		var new_score = each_score_array[7].trim();
		if(each_score_array[0].trim()[3] != '5'){
			var score = parseFloat(each_score_array[6].trim());
			if(score >= 95){
				new_score = 4.0;
			}
			else if(score >= 90){
				new_score = 3.7;
			}
			else if(score >= 85){
				new_score = 3.3;
			}
			else if(score >= 80){
				new_score = 3.0;
			}
			else if(score >= 77){
				new_score = 2.7;
			}
			else if(score >= 73){
				new_score = 2.3;
			}
			else if(score >= 70){
				new_score = 2;
			}
			else if(score >= 67){
				new_score = 1.7;
			}
			else if(score >= 63){
				new_score = 1.3;
			}
			else if(score >= 60){
				new_score = 1.0;
			}
			else if(score >= 0){
				new_score = 0;
			}
			else{
				continue;
			}
		}
		else if(new_score == "N/A" || new_score == "*"){
			continue;
		}
		else{
			new_score = parseFloat(new_score);
		}
		stuid_arr.push(each_score_array[0].trim());
		cname_arr.push(each_score_array[4].trim());
		score_arr.push(new_score);
		weigh_arr.push(parseInt(each_score_array[9].trim()));
		style_arr.push(each_score_array[10].trim());
		terms_arr.push(parseInt(each_score_array[8].trim()));
	}
	result['stuid'] = stuid_arr;
	result['cname'] = cname_arr;
	result['score'] = score_arr;
	result['weigh'] = weigh_arr;
	result['style'] = style_arr;
	result['terms'] = terms_arr;
	return result;
}