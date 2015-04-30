function resize_user_img(img, size) {
    if (img.height() > img.width()) {
        img.attr('width', size + 'px').css('margin-top', - ((img.height() / 2 ) - (size / 2)) + 'px');
    } else {
        img.attr('height', size + 'px').css('margin-left', - ((img.width() / 2) - (size / 2)) + 'px');
    }
}

function resize_wrapper() {
    var win_w = window.innerWidth;
    if (win_w > 800) {
        $('#wrapper').css('width', '800px').css('left', '50%').css('margin-left', '-400px');
    } else {
        $('#wrapper').css('width', '100%').css('left', '').css('margin-left', '');
    }
}

function resize_image() {
    $('.newsfeed-image .image img').each(function() {
        var img = $(this);
        img.css("width", "100%").css("height", "auto");
        if (img.height() < 100) {
            img.css("height", "100px").css("width", "auto");
        }
    });
}

function resize_window() {
    resize_image();
    resize_wrapper();
}

function detail_resize() {
    $('.detail-user-image .image img').each(function() {
        var img = $(this);
        resize_user_img(img, 70);
    });

    $('.comment-image .image img').each(function() {
        var img = $(this);
        resize_user_img(img, 40);
    });
}

function base_write() {
    $('input').addClass('light-placeholder');
    $('textarea').addClass('write-border light-placeholder');

    //$('.ui-select').addClass('write-border');
    $('#id_title').attr('placeholder', '제목');
    $('#id_fee').attr('placeholder', '가격 정보');
    $('#id_memo').attr('placeholder', '기타 사항').addClass('write-border');
}

function write(type) {
    base_write();

    if (type == 'default') {
        $('#id_content').addClass('write-border');

        $('#write-submit').click(function() {
            $('#write-submit').closest('form').submit();
        });

    } else if (type == 'car') {
        $('#id_depart').attr('placeholder', '출발');
        $('#id_destination').attr('placeholder', '도착');
        $('#id_transportation').attr('placeholder', '예) 택시');
        $('#id_time').attr('placeholder', '출발 시간');

        $('#write-submit').click(function() {
            var content =
                $('#id_depart').val() + ','
                + $('#id_destination').val() + ','
                + $('#id_memo').val();
            $('#id_content').val(content);
            $('#write-submit').closest('form').submit();
        });

    } else if (type == 'house') {
        $('#id_time').attr('placeholder', '계약기간');

        $('#write-submit').click(function() {
            var content =
                $('#id_title').val() + ','
                + $('span').text() + ','
                + $('#id_memo').val();
            $('#id_content').val(content);
            $('#write-submit').closest('form').submit();
        });

    } else if (type == 'store') {
        $('#id_link').attr('placeholder', '출처');
        $('#id_time').attr('placeholder', '제한 시간');

        $('#write-submit').click(function() {
            var content =
                $('#id_title').val() + ','
                + $('#id_link').val() + ','
                + $('#id_memo').val();
            $('#id_content').val(content);
            $('#write-submit').closest('form').submit();
        });
    }
}

function setting_ready() {
    $('.ui-checkbox').removeClass('ui-checkbox').addClass('setting-blank');
    $('label').removeClass();

    $('input').iCheck({
        checkboxClass: 'icheckbox_flat-pink'
    });
}

function search_show() {
    $('#default').removeClass('showleft').addClass('make_transist').addClass('hideleft');
    $('#search-table').addClass('make_transist').addClass('showleft');
}
function default_show() {
    $('#search-table').removeClass('showleft').addClass('make_transist').addClass('hideleft');
    $('#default').addClass('make_transist').addClass('showleft');
}