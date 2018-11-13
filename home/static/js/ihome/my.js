function logout() {
    $.get("/users/logout", function(data){
       if(data.code == 200){
           window.location.href = '/users/login/'
       }
    })
}


$(document).ready(function(){
    $.get("/users/my_get/", function (data) {
        if (data.code == 200){
            $('#user-avatar').attr('src', '/static/media/' + data.avatar);
            $('#user-name').text(data.name);
            $('#user-mobile').text(data.phone);
        }
    });
})