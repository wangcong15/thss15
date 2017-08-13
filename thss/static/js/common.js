$("#logout").click(function(){
  	$.cookie('qwer', null, {path: '/'});
  	$.cookie('asdf', null, {path: '/'});
  	location.href = "../login/";
});