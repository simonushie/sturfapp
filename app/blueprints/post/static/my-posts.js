$(document).ready(function(){


	$(document).on('click','input#filterbtn', function(){

			var each = $('option:selected').val();

			var page = $('#lost_item_category').attr('page');
			/*window.alert(page)*/

			var post_type = each
			/*window.alert(each)*/


			/*initialise the loader*/

		/*initialise the loader*/
			$(".svg-loader").fadeIn(1)

			req = $.ajax( 

			{  
				url: 'sort_your_posts',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( { 'page' : page , 'post_type' : post_type } )

 
			}

			);


/*			window.alert('ajax query block passed')
*/

			req.done(function(data){
/**/
				
							
				$(".svg-loader").fadeOut(1000, function() {
			        $(".bio-content").fadeOut(600).fadeIn(1000).html(data);        

			    });


			});

	});











	$(document).ready( function(){

    $(".svg-loader").fadeOut(2000, function() {
        $("body").fadeIn(1000);        
    });



	});











});


			


