$(document).ready(function(){

    $(window).resize(function(){
        if ($(window).width() >= 921) {
            $('.menu_aside').css({
                left: 0,
            });
        }
        else {
            $('.menu_aside').css({
                left: '-100%',
            });
        }
    });

    function menu_slidein() {
        $('.menu_aside').css({
            left: 0,
        });
        $('.shadow').css({
            opacity: '1',
        });
    }
    function menu_slideout() {
        $('.menu_aside').css({
            left: '-100%',
        });
        $('.shadow').css({
            opacity: 0,
        });
    }

    $('.nav_menu').click(function() {
        if ($(window).width() <= 920) {
            if ($('.menu_aside').position().left == 0) {
                menu_slideout();
            }
            else {
                menu_slidein();
            }
        }
    });






});

