// filtering functionality on product pages
$('#sort-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);

    var selectedVal = selector.val();
    if(selectedVal != "reset"){
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
})



$('.back-to-top').click(function(e) {
    window.scrollTo(0,0)
})




function updateCartTotal() {
    $.ajax({
        url: '/get_cart_total/',
        dataType: 'json',
        success: function (res) {
            $('.cart-total').text(res.total_items);


        }
    });
}

// new try


// new try



$('#addToCartBtn').on('click', function(){
    var _addBtn = $(this);
    var _qty = $('.product-qty').val();
    var _productId = $('.product-id').val();
    var _productName = $('.product-name').text();
    var _productImage = $('.product-image').val();
    var _productPrice = $('.product-price').val();

    console.log(_productPrice);

    if (_qty > 10 || _qty <= 0) {
        // code taken from https://djangocentral.com/django-ajax-with-jquery/
        // $('#addToCartBtn').addClass('active')
        _addBtn.removeClass('active').blur();
        $('.product-qty').removeClass('is-valid').addClass('is-invalid');
        $('.product-qty').blur();
        $('#Error').remove()
        $('.error-qty').before('<div class="invalid-feedback d-block" id="Error">quantity must be range 1 -10!</div>');

        return


    }


    // Ajaxs
    $.ajax({
        url:'/add_to_cart/',
        type : 'POST',
        headers: {
            'X-CSRFToken': $('#csrf_token').val()
        },
        data:{
            'id':_productId,
            'image':_productImage,
            'qty':_qty,
            'name':_productName,
            'price':_productPrice,
        },

        dataType:'json',
        beforeSend:function(){

            _addBtn.attr('disabled',true);
        },
        success:function(res){

            updateCartTotal()
            console.log(res.data);
            $('.product-qty').removeClass('is-invalid')
            $('#Error').remove()
            $('.product-qty').val(1)

            _addBtn.attr('disabled',false);
            //
            // updateCartTotal()
            // $('.product-qty').removeClass('is-invalid')
            // $('#Error').remove()
            // $('.product-qty').val(1)
            // _addBtn.attr('disabled',false);




        }
    });



})

$('.addToCartBtn').on('click', function(){
    var _addBtn = $(this);
    var _qty = 1;
    var _productName = $(this).closest('.all_products').find('.product-name').val();
    var _productId = $(this).closest('.all_products').find('.product-id').val();
    var _productName = $(this).closest('.all_products').find('.product-name').val();
    var _productImage = $(this).closest('.all_products').find('.product-image').val();
    var _productPrice = $(this).closest('.all_products').find('.product-price').val();

    console.log(_productId);
    console.log(_productName);
    console.log(_productPrice);

    $.ajax({
        url:'/add_to_cart/',
        type : 'POST',
        headers: {
            'X-CSRFToken': $(this).closest('.all_products').find('.csrf_token').val()
        },
        data:{
            'id':_productId,
            'image':_productImage,
            'qty':_qty,
            'name':_productName,
            'price':_productPrice,
        },

        dataType:'json',
        beforeSend:function(){

            _addBtn.attr('disabled',true);
        },
        success:function(res){

            updateCartTotal()
            console.log(res.data);






        }
    });



})


$(document).ready(function() {
    window.onpageshow = function(event) {
      if (event.persisted) {
        // The page is loaded from the cache
        location.reload(true); // Reload the page
      } else {
        // The page is loaded from the server
        updateCartTotal(); // Update the cart total
      }
    };
  });






