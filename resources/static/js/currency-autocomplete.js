$(function(){
    var places = [
        { value: '포항고터' },
        { value: '포항시터' },
        { value: '포항역' },
        { value: '한동대학교' },
        { value: '서울' },
        { value: '용인' },
        { value: '분당' },
        { value: '광주' },
        { value: '대전' },
        { value: '대구' },
        { value: '경주' },
    ];
    var trans = [
        { value: '카풀' },
        { value: '택시' },
    ];

    $('#id_depart').autocomplete({
        lookup: places,
        onSelect: function (suggestion) {
            $('#id_depart').html(suggestion.value);
        }
    });

    $('#id_destination').autocomplete({
        lookup: places,
        onSelect: function (suggestion) {
            $('#id_destination').html(suggestion.value);
        }
    });

    $('#id_transportation').autocomplete({
        lookup: trans,
        onSelect: function (suggestion) {
            $('#id_transportation').html(suggestion.value);
        }
    });


});