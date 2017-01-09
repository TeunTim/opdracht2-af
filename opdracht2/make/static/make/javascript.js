/**
 * Created by s138721 on 7-1-2017.
 */
$(document).ready(function() {

$.ajaxSetup({
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
})
    var breads = 0
    var cheeses = 0
    var bacons = 0
    var hams = 0
    var tomatos = 0
    var price = 0
    $('#cheese').click(function () {
        cheeses= cheeses+1
        price = price+0.25
        $("#ingredient-list").append("Cheese ");
    })

    $('#bread').click(function () {
        breads=breads+1
        price=price+0.10
		$("#ingredient-list").append("Bread ");
    })

    $('#bacon').click(function () {
        bacons=bacons+1
		$("#ingredient-list").append("Bacon ");
        price=price+0.20
    })

    $('#ham').click(function () {
        hams=hams+1
		$("#ingredient-list").append("Ham ");
        price=price + 0.15
    })

    $('#tomato').click(function () {
        tomatos=tomatos+1
		$("#ingredient-list").append("Tomato ");
        price= price + 0.15
        console.log(price)
    })
    
    $('#submit').click(function () {
        console.log('werkt')
        price = Math.round(price*100)/100
        var name = document.getElementById("name").value;
        $.ajax({
            type:'POST',
            url:'save/',
            data:{
                'name': name.toString(),
                'rating': 0,
                'price': price.toString(),
                'bread': breads.toString(),
                'ham': hams.toString(),
                'bacon': bacons.toString(),
                'tomato': tomatos,
                'cheese': cheeses
            },

        })
        return false;
        console.log(data)

    })
    
})




