$(document).ready(function(){

	$(document).on('click','button#load_more', function(){

			var count = $(this).attr('count');
/*			window.alert(count)
*/

			/*initialise the loader*/
			$(".svg-loader").fadeIn(1)

			req = $.ajax({  
				url: 'load_more_avatars',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'count': count } )

			});

	/*		window.alert('ajax query block passed')*/


			req.done(function(data){
/**/
				
				
			    $(".svg-loader").fadeOut(1000, function() {
			        $("#encapsulator").fadeOut(600).fadeIn(1000).html(data);        
			    });



			});


	});











	$(document).ready( function(){

    $(".svg-loader").fadeOut(300, function() {
        $("body").fadeIn(300);        
    });



	});











});


			


