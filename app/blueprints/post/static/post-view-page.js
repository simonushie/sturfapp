$(document).ready(function(){

	$(document).on('click','button#follow_button', function(){

			var post_id = $(this).attr('post_id');
/*			window.alert(post_id)*/

			var email = $(this).attr('email');
/*			window.alert(email)*/


			req = $.ajax({  
				url: 'http://localhost:70/post/follow-user',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'post_id': post_id, 'email' : email } )

 
			});
/*
			window.alert('ajax query block passed')*/


			req.done(function(data){

				$("#follow_buttons_container").fadeOut(800).fadeIn(800).fadeOut(800).fadeIn(800).fadeOut(800).fadeIn(800).html(data);
				/*
				window.alert('req was sucessful')
				window.alert("data:", data)*/

			});


	});








	$(document).on('click','button#un_follow_button', function(){

			var post_id = $(this).attr('post_id');
/*			window.alert(post_id)*/

			var email = $(this).attr('email');
/*			window.alert(email)*/


			req = $.ajax({  
				url: 'http://localhost:70/post/un-follow-user',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'post_id': post_id, 'email' : email } )

 
			});
/*
			window.alert('ajax query block passed')*/


			req.done(function(data){
/**/
				
				



				$("#follow_buttons_container").fadeOut(800).fadeIn(800).html(data);
				/*
				window.alert('req was sucessful')
				window.alert("data:", data)*/

			});


	});






	$(document).on('click','button#submit_comment_button', function(){

			var comment_body = $('textarea#comment_portal').val();
/*			window.alert(comment_body)*/

			var post_id = $(this).attr('post_id');
/*			window.alert(post_id)*/

			req = $.ajax({  
				url: 'http://localhost:70/post/add-comment',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'post_id': post_id, 'comment_body' : comment_body } )

 
			});
/*
			window.alert('ajax query block passed')*/


			req.done(function(data){

				$("#comment_case").fadeOut(400).fadeIn(800).html(data);
				/*
				window.alert('req was sucessful')
				window.alert("data:", data) */

			});


	});



	$(document).on('click','button#delete_comment_button', function(){


			var post_id = $(this).attr('post_id');
/*			window.alert(post_id)*/



			var comment_id = $(this).attr('comment_id');
/*			window.alert(comment_id)*/


			req = $.ajax({  
				url: 'http://localhost:70/post/delete-comment',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'post_id': post_id, 'comment_id' : comment_id } )

 
			});

/*			window.alert('ajax query block passed')*/


			req.done(function(data){

				$("#comment_case").fadeOut(400).fadeIn(800).html(data);
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
















});


			


