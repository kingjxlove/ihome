function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },10000)
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


$(document).ready(function () {
    $.get("/users/pro/", function (data) {
        if (data.code == 200){
            $('.user_icon').attr('src', '/static/media/' + data.icon);
            $('.username').val(data.name);
        }
    });

    $("#form-avatar").submit(function (e) {
        e.preventDefault();
        $(this).ajaxSubmit({
            url: '/users/profile/',
            type: 'POST',
            async: false,
            dataType: 'json',
            success:function (data) {
                if (data.code == 200){
                    $('.user_icon').attr('src', '/static/media/' + data.icon)
                }
            },
            error:function () {
                alert('上传失败')
            }
        })

    });
   $('#form-name') .submit(function (e) {
       e.preventDefault();
       $(this).ajaxSubmit({
           url: '/users/change_name/',
           dataType: 'json',
           type: 'POST',
           success: function (data) {
               alert(data);
               if (data.code == 200){
                   window.location.href = '/users/my/'
               }
           }
       })
   })
});
