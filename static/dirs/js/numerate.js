$(".answer-text").on('keyup', function(){
    var v = $(".answer-text").val().length;
    $(".tracker-answer").html(v);
});

$(".ask-text").on('keyup', function(){
    var v = $(".ask-text").val().length;
    $(".tracker-question").html(v);
});