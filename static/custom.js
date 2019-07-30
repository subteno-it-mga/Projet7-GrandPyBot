$(document).ready(function () {

    var home_page = '<div id="homepage" class="container-fluid center-block"><img id="img_home" class="img-responsive" src="static/homepage_img.gif"/><h2>Donne moi un ... BURRRRRP ... lieu ... et je vais peut être avoir la motivation de te raconter des conneries sur l\'endroit</h2></div>'
    $('#main_page').append(home_page);
    $('#sendsend').on("submit", function (event) {
        event.preventDefault();
        $('#homepage').remove();
        var user_input = $('#chat_input').val();
        $('#main_page').css("background-color", "rgba(255,255,255,0.9)");
        $('#main_page').append('<div id="main_content" class="container-fluid"><ul id="chat_list"></ul></div>');
        $('#chat_list').append(
            '<li class="row me">\
            <div class="col-md-2 img_chat"><img class="avatar_me_img img-fluid" src="static/morty.gif"/></div>\
        <div id="display-question"><p class="text-input"><span class="you-chat col-md-10">Vous (Morty) : </span>' +
            user_input +
        '</p></div></li>')
        $.ajax({
            type: "POST",
            url: "/process",
            data: JSON.stringify(user_input),
            dataType: 'json'

        }).done(function (data) {
            $('#chat_input').val("");
            $('#chat_list').append('<li class="row bot"><div id="bot-avatar" class="col-md-2 col-sm-12"><img class="avatar_bot_img" src="static/rickpybot_img.png"/></div><div id="story_chat" class="col-md-6 col-sm-12"><h2>RickPyBot:</h2>' + data["story"] + '</div>\
            <div id="gmap_chat" class="col-md-4 col-sm-12">' +
                data["map"] +
                '</div></li>');
            // Calculate the main_page height
            var newHeight1 = parseInt($('main').offset().top);
            var newHeight2 = parseInt($('.fixed-bottom').offset().top);
            var newHeight = newHeight2 - newHeight1;
            $('#main_page').css('height', newHeight);
            $('#main_page').animate({
                scrollTop: $('#main_page').get(0).scrollHeight
            }, 500);
        })

    })
    $('#fun').css("visibility","hidden");
    $( "#chat_input" ).focusin(function() {        
        $('#fun').css("visibility","visible").fadeOut(1000);
    });


});