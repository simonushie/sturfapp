$(document).ready(function(){

	$(document).on('click','div#feed.menu-item.active', function(){

			var action_type = 'feed'
			// window.alert(post_type)

			/*initialise the loader*/
			$(".svg-loader").fadeIn(1)

			req = $.ajax({  
				url: '/general',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'action_type' : action_type } )

 
			});

	/*		window.alert('ajax query block passed')*/

			req.done(function(data){

				
				
			    $(".svg-loader").fadeOut(1000, function() {
			        $("#everything").fadeIn(800).html(data);        
			    });

			});

	});



	$(document).on('click','div#sections.menu-item.active', function(){

			var action_type = 'sections'
			// window.alert(post_type)

			/*initialise the loader*/
			$(".svg-loader").fadeIn(1)

			req = $.ajax({  
				url: '/general',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'action_type' : action_type } )

 
			});

	/*		window.alert('ajax query block passed')*/

			req.done(function(data){

				
				
			    $(".svg-loader").fadeOut(1000, function() {
			        $("#everything").fadeIn(800).html(data);        
			    });

			});

	});



	$(document).on('click','div#requests.menu-item.active', function(){


			var action_type = 'requests'
			// window.alert(post_type)

			/*initialise the loader*/
			$(".svg-loader").fadeIn(1)

			req = $.ajax({  
				url: '/general',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'action_type' : action_type } )

 
			});

	/*		window.alert('ajax query block passed')*/

			req.done(function(data){

				
				
			    $(".svg-loader").fadeOut(1000, function() {
			        $("#everything").fadeIn(800).html(data);        
			    });

			});


	});















	$(document).ready( function(){


    $(".svg-loader").fadeOut(1000, function() {
        $("body").fadeIn(1000);        
    });



	});











});


			


