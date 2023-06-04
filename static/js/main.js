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
});

// updating price and item counter in navbar
function updateCartTotal() {
    $.ajax({
      url: '/get_cart_total/',
      dataType: 'json',
      success: function(res) {
        var totalItems = res.total_items;
        var total_price = res.total_price
        $('.cart-total').text(totalItems);
        $('.cart-total-bottom').text(totalItems);
        if(total_price == 0){
            $('.price').text('€0.00');

        }else{
            $('.price').html('€'+total_price);

        }

      }
    });
  }

// ajax call from product details page
$('#addToCartBtn').on('click', function(){
    var _addBtn = $(this);
    var _qty = $('.product-qty').val();
    var _productId = $('.product-id').val();
    var _productName = $('.product-name').text();
    var _productImage = $('.product-image').val();
    var _productPrice = $('.product-price').val();

    if (_qty > 10 || _qty <= 0) {
        // code taken from https://djangocentral.com/django-ajax-with-jquery/
        _addBtn.removeClass('active').blur();
        $('.product-qty').removeClass('is-valid').addClass('is-invalid');
        $('.product-qty').blur();
        $('#Error').remove()
        $('.error-qty').before('<div class="invalid-feedback d-block" id="Error">quantity must be range 1 -10!</div>');
        return
    }

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
            var message = _productName + ' quantity: ' + _qty + ' added to cart';
            updateCartTotal()
            $('.success-modal').modal('show');
            $('.custom-content').text(message)
            $('.product-qty').removeClass('is-invalid')
            $('#Error').remove()
            $('.product-qty').val(1)
            _addBtn.attr('disabled',false);
        }
    });
})

// ajax call for adding product to shopping cart from all products page
$('.addToCartBtn').on('click', function(){
    var _addBtn = $(this);
    var _qty = 1;
    var _productId = $(this).closest('.all_products').find('.product-id').val();
    var _productName = $(this).closest('.all_products').find('.product-name').val();
    var _productImage = $(this).closest('.all_products').find('.product-image').val();
    var _productPrice = $(this).closest('.all_products').find('.product-price').val();

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
            var message = _productName + ' quantity: ' + _qty + ' added to cart';
            updateCartTotal()
            $('.success-modal').modal('show');
            $('.custom-content').text(message)
            _addBtn.attr('disabled',false);
            console.log(res.data);
        }
    });
})

// ajax call for adding product to shopping cart from wishlist page
$('.addToCartBtnWish').on('click', function(){
    var _addBtn = $(this);
    var _qty = 1;
    var _productId = $(this).closest('.wishlist_products').find('.product-id').val();
    var _productName = $(this).closest('.wishlist_products').find('.product-name').val();
    var _productImage = $(this).closest('.wishlist_products').find('.product-image').val();
    var _productPrice = $(this).closest('.wishlist_products').find('.product-price').val();

    $.ajax({
        url:'/add_to_cart/',
        type : 'POST',
        headers: {
            'X-CSRFToken': $(this).closest('.wishlist_products').find('.csrf_token').val()
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
            var message = _productName + ' quantity: ' + _qty + ' added to cart';
            $('.custom-content').text(message)
            updateCartTotal()
            $('.success-modal').modal('show');
            _addBtn.attr('disabled',false);
        }
    });
});

// updating wishlist counters in top and bottom nav bar
function updateWishlistTotal(){

    $.ajax({
      url: '/wishlist/wishlist_total/',
      dataType: 'json',
      headers: {
        'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val()
      },

      success: function(res) {
        var wishlist_count = res.wishlist_count;
        console.log(wishlist_count);
        $('.heart-total').text(wishlist_count);
        $('.heart-total-bottom').text(wishlist_count);
      },
      error:function(xhr, textStatus, errorThrown){
        var errorMessage = "An error occured" + errorThrown
        $('#errorModal .error-content').text(errorMessage);
        $('#errorModal').modal('show');

      }

    });
}

//updating counters and price(even if page is served from the cache)
$(document).ready(function () {
    updateCartTotal();
    updateWishlistTotal()
});

// modal fade after 2 sec
function modalFading(){
    $('.success-modal').modal('show');
    setTimeout(function(){
        $('.success-modal').modal('hide');

    }, 2000)
}


