function hrefBack() {
    history.go(-1);
}

function decodeQuery() {
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function (result, item) {
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

$(document).ready(function () {


    var url = location.search;
    id = url.split('=')[1];
    $.get('/house/detail_get/' + id + '/', function (data) {
        var house_info_script = template('house_info_script', {
            house_info: data.house_info,
            facilities: data.facilities,
        });
        for (var i = 0; i < data.img.length; i++) {
            str1 = '<li class="swiper-slide"><img src="/static/media/' + data.img[i] + '"></li>';
            $('.swiper-wrapper').append(str1);
        }
        $('.landlord-pic img').attr('src', '/static/media/' + data.user_info[0]);
        $('.landlord-name span').text(data.user_info[1]);
        $('.house-title').text(data.user_info[2]);
        $('.detail-con').append(house_info_script);
        $('.house-price span').text(data.house_info.price);
        $('.book-house').attr('href', '/house/booking/?house_id=' + id).show();


        var mySwiper = new Swiper('.swiper-container', {
            loop: true,
            autoplay: 2000,
            autoplayDisableOnInteraction: false,
            pagination: '.swiper-pagination',
            paginationType: 'fraction'
        })
    })
})