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




// function updateCartTotal() {
//     $.ajax({
//         url: '/get_cart_total/',
//         dataType: 'json',
//         success: function (res) {
//             var message = res.message;
//             console.log(res);
//             $('.cart-total').text(res.total_items);
//             $('my_custom').toast('show');


//         }
//     });
// }

// new try

function updateCartTotal() {
    $.ajax({
      url: '/get_cart_total/',
      dataType: 'json',
      success: function(res) {
        var totalItems = res.total_items;
        $('.cart-total').text(totalItems);
      }
    });
  }




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


    // Ajax
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
            var message = res.my_message;
            console.log(message);

            updateCartTotal()
            $('.success-modal').modal('show');

            console.log(res.data);
            $('.product-qty').removeClass('is-invalid')
            $('#Error').remove()
            $('.product-qty').val(1)

            _addBtn.attr('disabled',false);





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
            $('.success-modal').modal('show');
            _addBtn.attr('disabled',false);
            console.log(res.data);






        }
    });



})



//

// $(document).ready(function() {
//     // Retrieve cart information from the local storage
//     var cartData = JSON.parse(localStorage.getItem('cart'));

//     // Update the cart counter
//     if (cartData) {
//       var totalItems = cartData.total_items;
//       $('.cart-total').text(totalItems);
//     }
//   });

//   $(window).on('popstate', function() {
//     // Retrieve cart information from the local storage
//     var cartData = JSON.parse(localStorage.getItem('cart'));

//     // Update the cart counter
//     if (cartData) {
//       var totalItems = cartData.total_items;
//       $('.cart-total').text(totalItems);

//     }
//   });


// $(document).ready(function () {
//     // Initialize cart counter with value from localStorage
//     var total_items = localStorage.getItem('total_items');
//     if (total_items) {
//         $('.cart-total').text(total_items);
//     }

//     // Listen for updates to cart counter and update localStorage
//     $(document).on('cartUpdated', function (event, total_items) {
//         $('.cart-total').text(total_items);
//         localStorage.setItem('total_items', total_items);
//     });
// });


$(document).ready(function () {
    updateCartTotal();
});






