function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function() {
    $("#mobile").focus(function(){
        $("#mobile-err").hide();
    });
    $("#password").focus(function(){
        $("#password-err").hide();
    });
    $(".form-login").submit(function(e){
        e.preventDefault();
        mobile = $("#mobile").val();
        passwd = $("#password").val();
        if (!mobile) {
            $("#mobile-err span").html("请填写正确的手机号！");
            $("#mobile-err").show();
            return;
        } 
        if (!passwd) {
            $("#password-err span").html("请填写密码!");
            $("#password-err").show();
            return;
        }
        $.ajax({
            url: '/users/login/',
            type: 'POST',
            data: {'mobile': mobile, 'passwd': passwd},
            dataType: 'json',
            success:function (data) {
                if(data.code == 200){
                    window.location.href='/users/my/'
                }
                else {
                    for(var i = 1000; i<1100; i++){
                        if(data.code == i){
                            alert(data.msg);
                            passwd = $("#password").val('');
                            return;
                        }
                    }
                }
            }
        })
    });
})