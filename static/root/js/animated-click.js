$("#submit-question").on('click', function(){
    $(this).html("done !");

    $(this).fadeOut(4000, "swing");
    $("#ask").fadeOut(4000, "swing", function(){
        $("#submit-question").html("Ask");
        $("#submit-question").fadeIn(100, "swing");
        $(".ask-text").val("");
        $(".tracker-question").html("0");
        $("#ask").fadeIn(100, "swing");
    });

});

$("#submit-answer").on('click', function(){
    $(this).html("done !");

    $(this).fadeOut(4000, "swing");
    $("#answer").fadeOut(4000, "swing", function(){
        $("#submit-answer").html("Answer");
        $("#submit-answer").fadeIn(100, "swing");
        $(".answer-text").val("");
        $(".tracker-answer").html("0");
        $("#answer").fadeIn(100, "swing");
    });

});



$(".mybtn").on('click', function(){
    var i = $(this).attr('id');

    $("#" + i).fadeOut(500, "swing");
    for(var j = 0; j < all; j++)
    {
        if(buff[j].id == i)
        {
            if($("#" + i).html() == 'got clicked !')
            {
                $("#" + i).html(buff[j].text);
            } else {
                $("#" + i).html('got clicked !');
            } 
        }
    }
    $("#" + i).fadeIn(500, "swing");
});