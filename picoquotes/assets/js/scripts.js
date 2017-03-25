var ENTER = 13;
var ESCAPE = 27;

$(document).ready(function() {
    $('a.open-search').click(function(e) {
        $('.search-wrap').addClass('show');
        $('#search').focus();

        e.preventDefault();
    });

    $('a.close-search').click(function(e) {
        $('.search-wrap').removeClass('show');

        e.preventDefault();
    });

    $('#search').keyup(function(e) {
        if (e.which === ENTER) {
            window.location.href = $('#search').data('search-url') + '?q=' + $('#search').val();
        }
        else if (e.which === ESCAPE) {
            $('.search-wrap').removeClass('show');
        }
    });
});
