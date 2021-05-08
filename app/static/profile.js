$(document).ready(function(){

	$(document).on('click','#phone_visibility_yes', function(){

			var modal = document.getElementById('phoneModal');

			var phone_visibility = $(this).attr('phone_visibility');
/*			window.alert(phone_visibility)*/

			var user_id = $(this).attr('user_id');
/*			window.alert(user_id)*/
/*
			window.alert('btn click sucessful')*/

			modal.style.display = "none";

			req = $.ajax({  
				url: 'http://localhost:70/phone_visibility',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'phone_visibility': phone_visibility, 'user_id' : user_id } )

 
			});
/*
			window.alert('ajax query block passed')*/


			req.done(function(data){

				
				



				$("#info_container").fadeIn(1000).fadeOut(4000).html(data);
				
/*				window.alert('req was sucessful')
				window.alert("data:", data)*/

		});


	});







	$(document).on('click','#phone_visibility_no', function(){

			var modal = document.getElementById('phoneModal');

			var phone_visibility = $(this).attr('phone_visibility');
		/*	window.alert(phone_visibility)*/

			var user_id = $(this).attr('user_id');
/*			window.alert(user_id)*/
/*
			window.alert('btn click sucessful')*/

			modal.style.display = "none";

			req = $.ajax({  
				url: 'http://localhost:70/phone_visibility',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'phone_visibility': phone_visibility, 'user_id' : user_id } )

 
			});

			


			req.done(function(data){


				$("#info_container").fadeIn(1000).fadeOut(4000).html(data);
				
/*				window.alert('req was sucessful')
				window.alert("data:", data)*/

		});


	});









	$(document).on('click','#email_visibility_no', function(){

			var modal = document.getElementById('emailModal');

			var email_visibility = $(this).attr('email_visibility');
		/*	window.alert(phone_visibility)*/

			var user_id = $(this).attr('user_id');
/*			window.alert(user_id)*/
/*
			window.alert('btn click sucessful')*/

			modal.style.display = "none";

			req = $.ajax({  
				url: 'http://localhost:70/email_visibility',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'email_visibility': email_visibility, 'user_id' : user_id } )

 
			});

			


			req.done(function(data){


				$("#info_container").fadeIn(1000).fadeOut(4000).html(data);
				
/*				window.alert('req was sucessful')
				window.alert("data:", data)*/

		});


	});






	$(document).on('click','#email_visibility_yes', function(){

			var modal = document.getElementById('emailModal');

			var email_visibility = $(this).attr('email_visibility');
		/*	window.alert(phone_visibility)*/

			var user_id = $(this).attr('user_id');
/*			window.alert(user_id)*/
/*
			window.alert('btn click sucessful')*/

			modal.style.display = "none";

			req = $.ajax({  
				url: 'http://localhost:70/email_visibility',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'email_visibility': email_visibility, 'user_id' : user_id } )

 
			});

			


			req.done(function(data){


				$("#info_container").fadeIn(1000).fadeOut(4000).html(data);
				
/*				window.alert('req was sucessful')
				window.alert("data:", data)*/

		});


	});




	$(document).ready( function(){

    $(".svg-loader").fadeOut(500, function() {
        $("body").fadeIn(500);        
    });



	});













});


			


