var me = {};
me.avatar = "data:image/png;base64,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";

var you = {};
you.avatar = "https://www.squatties.com/images/avatars/avatar-rick-sanchez-256.png";

function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var strTime = hours + ':' + minutes + ' ' + ampm;
    return strTime;
}            

//-- No use time. It is a javaScript effect.
function insertChat(who, text, time){
    if (time === undefined){
        time = 0;
    }
    var control = "";
    var date = formatAMPM(new Date());
    
    if (who == "me"){
        control = '<li style="width:100%">' +
                        '<div class="msj macro">' +
                        '<div class="avatar"><img class="img-circle" style="width:100%;" src="'+ me.avatar +'" /></div>' +
                            '<div class="text text-l">' +
                                '<p>'+ text +'</p>' +
                                '<p><small>'+date+'</small></p>' +
                            '</div>' +
                        '</div>' +
                    '</li>';                    
    }else{
        control = '<li style="width:100%;">' +
                        '<div class="msj-rta macro">' +
                            '<div class="text text-r">' +
                                '<p>'+text+'</p>' +
                                '<p><small>'+date+'</small></p>' +
                            '</div>' +
                        '<div class="avatar" style="padding:0px 0px 0px 10px !important"><img class="img-circle" style="width:100%;" src="'+you.avatar+'" /></div>' +                                
                  '</li>';
    }
    setTimeout(
        function(){                        
            $("ul").append(control).scrollTop($("ul").prop('scrollHeight'));
        }, time);
    
}

function resetChat(){
    $("ul").empty();
}

$(".mytext").on("keydown", function(e){
    if (e.which == 13){
        var text = $(this).val();
        if (text !== ""){
            insertChat("me", text);              
            $(this).val('');
        }
    }
});

$('body > div > div > div:nth-child(2) > span').click(function(){
    $(".mytext").trigger({type: 'keydown', which: 13, keyCode: 13});
})

//-- Clear Chat
resetChat();

//-- Print Messages

insertChat("you","Test");

//-- NOTE: No use time on insertChat.