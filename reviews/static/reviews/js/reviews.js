$('.review-form').submit(function(event){
    event.preventDefault()
    var _submitBtn = $('.add_review');

    var _productId = $('.product-id').val();
    var _user = $('.user').val();
    var _content = $('input[name="content"]').val();
    var createReviewUrl = $(this).data('create-review-url');


    // console.log(_productId);
    // console.log(_content);
    // console.log(_user);
    // console.log(token);
    // console.log(createReviewUrl);

        $.ajax({
                url: createReviewUrl ,
                type: 'POST',
                headers: {
                    'X-CSRFToken': $('#csrf').val()
                },
                data: {
                    'user':_user,
                    'product_id': _productId,
                    'content': _content
                },
                dataType:'json',
                beforeSend:function(){
                    _submitBtn.attr('disabled',true);

                },
                success:function(res){
                    var author=res.author
                    var content=res.content
                    var message=res.message
                    console.log(message);
                    _submitBtn.attr('disabled',false);

                    $('.review-form')[0].reset()



                }
        })


})

