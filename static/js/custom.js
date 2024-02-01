


$(document).ready(function(){


    $('.thumbs a').click(function(e){
        e.preventDefault();
        $('.mainImage img').attr('src',$(this).attr('href'));
    })
})




