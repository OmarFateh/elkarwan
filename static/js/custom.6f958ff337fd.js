/*global $, $  ,WOW */

$(function () {
    
    'use strict';
    
	
	
   // Animate loader off screen
    $(".se-pre-con").fadeOut("slow");
    
    
	// wow 
	
    new WOW().init();
	
    
   
});
















































































/*
 $('.navbar li a').click(function (e) {
        
        e.preventDefault();
        
        $('body,html').animate({
            
            
            scrollTop: $('#' + $(this).data('scroll')).offset().top
            
            
        }, 2000);
        
        
        
        
        
        
        
    });
    */