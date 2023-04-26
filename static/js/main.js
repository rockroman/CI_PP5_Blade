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



