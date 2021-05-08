$(document).ready(function(){

	
	$(document).on('click','button#send_chat_button', function(){

			var chat_body = $('textarea#chat_portal').val();
			/*window.alert(chat_body)*/

			var post_id = $(this).attr('post_id');

			var recipient = $(this).attr('recipient');
			// window.alert(recipient)

			req = $.ajax({  
				url: 'http://localhost:70/post/chat_with_claimers',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'post_id': post_id, 'chat_body' : chat_body, 'recipient' : recipient } )

 
			});
/*
			window.alert('ajax query block passed')*/


			req.done(function(data){

				/*$("#comment_case").fadeIn(800).html(data);*/

				setTimeout(function() { $("#comment_case").html(data) }, 300)

				$("#comment_case").fadeIn(800)

			/*	$("#comment_case").load(location.href + "#comment_case");*/
				/*
				window.alert('req was sucessful')
				window.alert("data:", data) */

			});


	});










	$(document).ready( function(){

    $(".svg-loader").fadeOut(2000, function() {
        $("body").fadeIn(1000);        
    });



	});







/*
	$(document).ready( function(){



            setInterval(function() { 	$("#comment_case").load(location.href + " #comment_case"); }, 20000000);


	});
*/











});


			


