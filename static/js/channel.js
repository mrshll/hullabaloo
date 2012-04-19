jQuery(function($) {

    //subscribe to the pages' channel
    var jug = new Juggernaut;
    //variable jug_channel must be set before this call
    jug.subscribe(jug_channel, function(data) {
        console.log("Jug got data: " + data);
        $('#posts').append( "<li>" + data + "</li>" );
    });

    var AJAXify = false;
    //ajaxify the post submit
    $('form').submit(function (e) {
        if (!AJAXify) return;
        e.preventDefault();
        $.post( $(this).attr('action') , $(this).serialize() );
    });
});

