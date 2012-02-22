jQuery(function($) {

    var jug = new Juggernaut;
    jug.subscribe("test", function(data) {
        console.log("Jug got data: " + data);
        $('#posts').append( "<li>" + data + "</li>" );
    });


});
