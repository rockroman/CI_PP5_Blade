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

// $('#addToCartBtn').on('click', function(){
//     var _addBtn = $(this);
//     var _qty = $('.product-qty').val();
//     var _productId = $('.product-id').val();
//     var _productName = $('.product-name').text();
//     var _productImage = $('.product-image').val();
//     var _productPrice = $('.product-price').val();
//     console.log(_productPrice);


//     // Ajax
//     $.ajax({
//         url:'/add_to_cart/',
//         type : 'POST',
//         headers: {
//             'X-CSRFToken': $('#csrf_token').val()
//         },
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

//             $('.cart-total').text(res.total_items);
//             _addBtn.attr('disabled',false);

//         }
//     });


// })
let count = 0
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

           console.log(res.data);
            $('.product-qty').removeClass('is-invalid')
            $('#Error').remove()
            $('.product-qty').val(1)
            // location.reload()
            // $('.msg-success').removeClass('d-none')
            // $('#reboot').on('click', function(){
            //     $('.msg-success').addClass('d-none')

            // })



// working
            // initialize the count variable
            // let count = 0;

            // iterate through the nested dictionary
            // for (const key in res.data) {
            // if (res.data.hasOwnProperty(key)) {
            //     count += res.data[key]['qty'];
            //     }
            // }

         // inject the count to the template
            // $('.items-num').text(count);

// working
        // let count = 0;

        // Get array of keys from res.data object
        // const keys = Object.keys(res.data);

        // Iterate through the keys array
        // for (const key of keys) {
        // count += res.data[key]['qty'];
        // }

        // Inject the count to the template
        // $('.items-num').text(count);

            _addBtn.attr('disabled',false);
            // console.log(res.message);

        }
    });



})



// $('.items-num').text(count);



