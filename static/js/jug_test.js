jQuery(function($) {

    var jug = new Juggernaut;
    //variable jug_channel must be set before this call
    jug.subscribe(jug_channel, function(data) {
        console.log("Jug got data: " + data);
        $('#posts').append( "<li>" + data + "</li>" );
    });


});
