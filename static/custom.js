// js file for the app

// waiting the page is fully load to act
$(document).ready(function () {

    // selector for the main page in a variable because it is called several times
    var main_page = $('#main_page');
    var loader = '<div id="loader"><div class="spinner-border spinner-border-lg text-danger" role="status">\
    <span class="sr-only">Loading...</span>\
  </div><h1>Patiente un peu !!</h1></div>'
    // add the homepage before typing a message
    var home_page = '<div id="homepage" class="container-fluid center-block"><img id="img_home" class="img-responsive" src="static/pictures/homepage_img.gif"/><h2>Donne moi un ... BURRRRRP ... lieu ... et je vais peut être avoir la motivation de te raconter des conneries sur l\'endroit</h2></div>'
    main_page.append(home_page);

    // trigger the main function when the user submit a message
    $('#sendsend').on("submit", function (event) {

        // prevent sending the form and reloading the page
        event.preventDefault();

        // remove the homepage
        $('#homepage').remove();

        // add some style for the chat area
        main_page.css("background","url('static/pictures/background-main.png')")
        main_page.css("background-color", "rgba(255,255,255,0.9)");

        // get the input value in the input from the form
        var user_input = $('#chat_input').val();
        
        // appending the main page and the user question
        main_page.append('<div id="main_content" class="container-fluid"><ul id="chat-list"></ul></div>');
        $('#chat-list').append(
            '<li class="row me">\
            <div class="col-md-2 img_chat"><img class="avatar_me_img img-fluid" src="static/pictures/morty.gif"/></div>\
        <div id="display-question"><p class="your-text"><span class="you-chat col-md-10">Vous (Morty) : </span>' +
            user_input +
        '</p></div></li>')

        $('#chat-list').append(loader)

        // scroll automatically when a message appear
        main_page.animate({
            scrollTop: main_page.get(0).scrollHeight
        }, 500);

        // ajax POST call
        $.ajax({
            type: "POST",
            url: "/process",
            data: JSON.stringify(user_input),
            dataType: 'json'

        // when the data are posted and treated we done the following things
        }).done(function (data) {

            $('#loader').remove();

            // remove the value in the input field
            $('#chat_input').val("");

            // append the message of the bot
            $('#chat-list').append('<li class="row bot"><div id="bot-avatar" class="col-md-2 col-sm-12"><img class="avatar_bot_img" src="static/pictures/rickpybot_img.png"/></div><div id="story_chat" class="col-md-6 col-sm-12"><h2>RickPyBot:</h2>' + data["story"] + '</div>\
            <div id="gmap_chat" class="col-md-4 col-sm-12">' +
                data["map"] +
                '</div></li>');
            // scroll automatically when a message appear
            main_page.animate({
                scrollTop: main_page.get(0).scrollHeight
            }, 500);
        })

    })
    // small fun thing
    $('#fun').css("visibility","hidden");
    $( "#chat_input" ).focusin(function() {        
        $('#fun').css("visibility","visible").fadeOut(1000);
    });

    // Calculate the main_page height for a better display. Refresh every second
    setInterval(function(){
        var newHeight1 = parseInt($('main').offset().top);
        var newHeight2 = parseInt($('.fixed-bottom').offset().top);
        var newHeight = newHeight2 - newHeight1;
        main_page.css('height', newHeight);
    },1000)
});