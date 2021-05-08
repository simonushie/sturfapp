$(document).ready(function(){

	$(document).on('click','button#followed_button', function(){

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
				url: 'posts-page-jq-update',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'page': page, 'post_type' : post_type } )

 
			});

	/*		window.alert('ajax query block passed')*/




			req.done(function(data){
/**/
				
				
			    $(".svg-loader").fadeOut(1000, function() {
			        $("#encapsulator").fadeOut(600).fadeIn(1000).html(data);        
			    });



/*

				$("#encapsulator").fadeOut(800).fadeIn(800).html(data);
				*/
				/*
				window.alert('req was sucessful')
				window.alert("data:", data)*/

			});


	});





	$(document).on('click','button#normal_button.active', function(){

			var page = $(this).attr('page');
			// window.alert(page)

			var post_type = $(this).attr('post_type');
			// window.alert(post_type)

/*			var dict = {page: 'page', post_type : 'post_type'}
			window.alert(dict)*/

/*			var name = $('nameInput' + member_id).val();

			var email = $('emailInput' + member_id).val();*/

			req = $.ajax({  
				url: 'posts-page-jq-update',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'page': page, 'post_type' : post_type } )

 
			});

	/*		window.alert('ajax query block passed')*/



			/*initialise the loader*/
			$(".svg-loader").fadeIn(1)

			req.done(function(data){
/**/
				
			    $(".svg-loader").fadeOut(1000, function() {
			        $("#encapsulator").fadeOut(600).fadeIn(1000).html(data);        
			    });				



/*				$("#encapsulator").fadeOut(800).fadeIn(800).html(data);

*/				/*
				window.alert('req was sucessful')
				window.alert("data:", data)*/

			});

	});








	$(document).on('click','button#lost_item_button', function(){

			var page = $(this).attr('page');
/*			window.alert(page)*/

			var post_type = $(this).attr('post_type');
/*			window.alert(post_type)*/

/*			var dict = {page: 'page', post_type : 'post_type'}
			window.alert(dict)*/

/*			var name = $('nameInput' + member_id).val();

			var email = $('emailInput' + member_id).val();*/



			/*initialise the loader*/
			$(".svg-loader").fadeIn(1)

			req = $.ajax({  
				url: 'posts-page-jq-update',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'page': page, 'post_type' : post_type } )

 
			});

	/*		window.alert('ajax query block passed')*/


			req.done(function(data){
/**/
				


		    $(".svg-loader").fadeOut(1000, function() {
		        $("#encapsulator").fadeOut(600).fadeIn(1000).html(data);        
		    });				



/*
				$("#encapsulator").fadeOut(800).fadeIn(800).html(data);

*/				/*
				window.alert('req was sucessful')
				window.alert("data:", data)*/

			});

	});









	$(document).on('click','button#found_item_button', function(){

			var page = $(this).attr('page');
/*			window.alert(page)*/

			var post_type = $(this).attr('post_type');
/*			window.alert(post_type)*/

/*			var dict = {page: 'page', post_type : 'post_type'}
			window.alert(dict)*/

/*			var name = $('nameInput' + member_id).val();

			var email = $('emailInput' + member_id).val();*/


			/*initialise the loader*/
			$(".svg-loader").fadeIn(1)

			req = $.ajax({  
				url: 'posts-page-jq-update',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( {'page': page, 'post_type' : post_type } )

 
			});

/*			window.alert('ajax query block passed')*/


			req.done(function(data){
/**/
				
							
			    $(".svg-loader").fadeOut(1000, function() {
			        $("#encapsulator").fadeOut(600).fadeIn(1000).html(data);        
			    });


/*
				$("#encapsulator").fadeOut(800).fadeIn(800).html(data);*/
				/*
				window.alert('req was sucessful')
				window.alert("data:", data)*/

			});

	});








	$(document).on('click','input#foundbtn', function(){

			var each = $('option:selected').val();

			var page = $('#lost_item_category').attr('page');
		/*	window.alert(each)*/

			var item_type = each
/*			window.alert(item_type)*/

/*			var dict = {page: 'page', post_type : 'post_type'}
			window.alert(dict)*/

/*			var name = $('nameInput' + member_id).val();

			var email = $('emailInput' + member_id).val();*/


			/*initialise the loader*/
			$(".svg-loader").fadeIn(1)

			req = $.ajax({  
				url: 'posts-found-category',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( { 'page' : page , 'item_type' : item_type } )

 
			});

/*			window.alert('ajax query block passed')

*/
			req.done(function(data){
/**/
				
							
			    $(".svg-loader").fadeOut(1000, function() {
			        $("#small_content").fadeOut(600).fadeIn(1000).html(data);        
			    });




			});

	});










	$(document).on('click','input#filterbtn', function(){

			var each = $('option:selected').val();

			var page = $('#lost_item_category').attr('page');
		/*	window.alert(each)*/

			var item_type = each
/*			window.alert(item_type)*/

/*			var dict = {page: 'page', post_type : 'post_type'}
			window.alert(dict)*/

/*			var name = $('nameInput' + member_id).val();

			var email = $('emailInput' + member_id).val();*/


			/*initialise the loader*/
			$(".svg-loader").fadeIn(1)

			req = $.ajax({  
				url: 'posts-lost-item-category',
				type : 'POST',
				contentType: 'application/json',
				data : JSON.stringify ( { 'page' : page , 'item_type' : item_type } )

 
			});

/*			window.alert('ajax query block passed')

*/
			req.done(function(data){
/**/
				
							
			    $(".svg-loader").fadeOut(1000, function() {
			        $("#small_content").fadeOut(600).fadeIn(1000).html(data);        
			    });




			});

	});











	$(document).ready( function(){

    $(".svg-loader").fadeOut(2000, function() {
        $("body").fadeIn(1000);        
    });



	});











});


			


