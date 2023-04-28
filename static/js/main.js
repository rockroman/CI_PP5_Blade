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

// back to top button

// When the user scrolls down 300px from the top of the document, show the button
// window.onscroll = function () {
//     scrollFunction();
//   };

//   function scrollFunction() {
//     if (
//       document.body.scrollTop > 150 ||
//       document.documentElement.scrollTop > 150
//     ) {
//       $(".btt").fadeIn(700);
//     } else {
//       $(".btt").fadeOut(700);
//     }
// }

$('.back-to-top').click(function(e) {
    window.scrollTo(0,0)
})

// update cart

// $('#addToCartBtn').on('click', function(){
//     var _addBtn = $(this);
//     var _qty = $('.product-qty').val();
//     var _productId = $('.product-id').val();
//     var _productName = $('.product-name').text();
//     var _productImage = $('.product-image').val();
//     var _productPrice = $('.product-price').text();
//     console.log(_qty);

//     // Ajax
//     $.ajax({
//         url:'/add_to_cart',
//         data:{
//             'id':_productId,
//             'image':_productImage,
//             'qty':_qty,
//             'name':_productName,
//             'price':_productPrice,
//         },
//         dataType:'json',
//         beforeSend:function(){
//             _addBtn.attr('disabled',true);
//         },
//         success:function(res){
//             $('.cart-total').text(res.totalitems);
//             _addBtn.attr('disabled',false);
//         }
//     });
//     // End

// })
$('#addToCartBtn').on('click', function(){
    var _addBtn = $(this);
    var _qty = $('.product-qty').val();
    var _productId = $('.product-id').val();
    var _productName = $('.product-name').text();
    var _productImage = $('.product-image').val();
    var _productPrice = $('.product-price').val();
    console.log(_productPrice);

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
            $('.cart-total').text(res.totalitems);
            _addBtn.attr('disabled',false);
        }
    });
    // End

})



