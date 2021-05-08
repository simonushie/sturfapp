$(document).ready(function(){

	$(document).on('click','button#other_claim_attempts', function(){

			var page = $(this).attr('page');
			// window.alert(page)

			var post_type = $(this).attr('post_type');
			// window.alert(post_type)

/*			var dict = {page: 'page', post_type : 'post_type'}
			window.alert(dict)*/

/*			var name = $('nameInput' + member_id).val();

			var email = $('emailInput' + member_id).val();*/


			/*initialise the loader*/
			$(".svg-loader").fadeIn(1)

			req = $.ajax({  
				url: 'my_claim_attempts',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'page': page, 'post_type' : post_type } )

 
			});
/*
			window.alert('ajax query block passed')
*/



			req.done(function(data){
/**/
				
				
			    $(".svg-loader").fadeOut(1000, function() {
			        $(".entire_content").fadeOut(600).fadeIn(1000).html(data);        
			    });

			});


/*			req.fail(function(data) {
                window.alert('something went wrong!')
            });
*/

	});





	$(document).on('click','button#my_claim_attempts.active', function(){

			var page = $(this).attr('page');
			// window.alert(page)

			var post_type = $(this).attr('post_type');
			// window.alert(post_type)

			req = $.ajax({  
				url: 'my_claim_attempts',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'page': page, 'post_type' : post_type } )

 
			});
/*
			window.alert('ajax query block passed')
*/


			/*initialise the loader*/
			$(".svg-loader").fadeIn(1)

			req.done(function(data){
/**/
				
				
			    $(".svg-loader").fadeOut(1000, function() {
			        $(".entire_content").fadeOut(600).fadeIn(1000).html(data);        
			    });

			});

/*
			req.fail(function(data) {
                window.alert('something went wrong!')
            });*/

	});










	$(document).ready( function(){

    $(".svg-loader").fadeOut(2000, function() {
        $("body").fadeIn(1000);        
    });



	});











});


			


