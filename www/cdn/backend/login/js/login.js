$.fn.serializeObject = function(){
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};
 
$(function() {
        var API_URL = "/elcano-iepg/backend-api";
        
        function goApp() {
            //user already logged in, go to app
            location.pathname = location.pathname.substring(0,location.pathname.lastIndexOf("/"));
        }
        
        // this will call goApp if the user is logged in. 
        $.getJSON(API_URL + "/user", function(user){
            if (user.id) 
                goApp();
        });  
             
        function doLogin(){
            $.ajax({
                url : API_URL + "/user/login",
                method: "POST",
                dataType: "json",
                contentType: "application/json",
                data: JSON.stringify($('form').serializeObject()),
                success: function(json){
                    if (json.Login) {
                        goApp();
                    }
                    else{
                        alert("Bad user or password");
                    }
                }
            });
        }
        
        $("form").submit(function(e){
            e.preventDefault();
            doLogin();
            
        });
});
        