function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },10000)
    });
}


$(document).ready(function(){

    $.get('/users/auth_get/', function (data) {
        if(data.code == 200){
            $("#real-name").val(data.id_name);
            $("#id-card").val(data.id_card);
            $('.btn-success').hide();
        }
    })



    $("#form-auth").submit(function (e) {
        e.preventDefault();
        $(this).ajaxSubmit({
            url: '/users/auth_info/',
            type: 'POST',
            dataType: 'json',
            success: function (data) {
                if(data.code == 200){
                    alert('认证成功');
                    $('.btn-success').hide()
                }
                else {
                    for(var i = 1000; i<1100; i++){
                        if(data.code == i){
                            alert(data.msg);
                            return;
                        }
                    }
                }
            }
        })
    })
});

