$(document).ready(function(){
    $('.js--nav-icon').click(function() {
        var nav = $('.js--main-nav');
        var icon = $('.js--nav-icon i');
        
        nav.toggle(5);
        
        if (icon.hasClass('ion-md-menu')) {
            icon.addClass('ion-md-close')
            icon.removeClass('ion-md-menu')
        } else {
            icon.addClass('ion-md-menu')
            icon.removeClass('ion-md-close')
        }
        
        
    })
    

});