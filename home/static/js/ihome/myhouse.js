$(document).ready(function () {
    $(".auth-warn").show();

    $.get('/house/my_house/', function (data) {
        if (data.code == 200) {
            $(".house-title").append()
            $(".auth-warn").hide();
            $("#houses-list").show();
            console.log(data);
            for (var i = 0; i < data.title.length; i++) {
                str_title = '<h3>房屋ID:' + (i + 1) + ' —— ' + data.title[i] + '</h3>';
                str_info = ('<img src="/static/media/' + data.index_image[i] + '">'
                    + '<div class="house-text"><ul><li>位于：' + data.address[i]
                    + '</li><li>价格：￥' + data.price[i] + '/晚</li>' + '<li>发布时间：'
                    + data.create_time[i] + '</li></ul></div>');
                house_info = ('<li><a href="/house/detail/?id=' + data.id[i] + '"><div class="house-title">'
                    + str_title + '</div><div class="house-content">'
                    + str_info + '</div></a></li>');
                $("#houses-list").append(house_info);
            }
        }
        if (data.code == 1009) {
            $(".auth-warn").show();
            $("#houses-list").hide();
        }
    })
})