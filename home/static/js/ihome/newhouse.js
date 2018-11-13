function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function () {
    $.get('/house/new_house/', function (data) {
        for (var i = 0; i < data.area_id.length; i++) {
            area_id = data.area_id[i];
            area_address = data.area_address[i];
            str1 = '<option value="' + area_id + '">' + area_address + '</option>';
            $("#area-id").append(str1)
        }
        for (var j = 0; j < data.fac_id.length; j++) {
            str2 = '<li><div class="checkbox"><label><input type="checkbox" name="facility" value="' + data.fac_id[j] + '">' + data.fac_name[j] + '</label></div></li>'
            $(".house-facility-list").append(str2)
        }
    })
    $("#form-house-info").submit(function (e) {
        e.preventDefault()
        $(this).ajaxSubmit({
            url: '/house/newhouse/',
            type: 'POST',
            dataType: 'json',
            success: function (data) {
                if (data.code == 200) {

                    $("#form-house-info").hide();
                    $('#form-house-image').show();
                    $("#house-id").attr('value', data.house_id)
                }
            }
        })
    });
    $("#form-house-image").submit(function (e) {
        e.preventDefault()
        $(this).ajaxSubmit({
            url: '/house/img/',
            type: 'POST',
            dataType: 'json',
            success: function (data) {
                if (data.code == 200) {
                    for (var i = 0; i < data.imgs.length; i++) {
                        str1 = '<img class="house_img" src="/static/media/' + data.imgs[i] + '">';
                        $('.house-image-cons').append(str1)
                    }
                }
            }
        })
    })
})