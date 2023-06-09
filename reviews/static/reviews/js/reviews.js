
function appendReview(res){
    var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
    var now = new Date();
    const currentTime = now.getHours() + ':' + now.getMinutes().toString().padStart(2, '0');
    $('.commented-section').append(`

    <div class="modal fade review" tabindex="-1" id="modal_${res.id}">
        <div class="modal-dialog custom-modal-dialog ">
            <div class="modal-content">
                <div class="modal-header p-2">
                    <p class="h4 modal-title fw-bold">You are Deleting</p>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <p class="del-review">Your review!!Are you sure?</p>
                </div>
                <div class="modal-footer">
                    <form action="" method="POST" class="mx-2 delete-form">
                        <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                        <input type="hidden" name="review_id" value="${res.id}">
                        <input type="hidden" name="delete-ur" value="{% url 'reviews:delete_review' %}">
                        <button class="btn btn-danger" type="submit">delete</button>
                    </form>
                    <button class="btn btn-primary" data-bs-dismiss="modal">Go back</button>
                </div>
            </div>
        </div>
    </div>
    <div class="user-comments mt-2 pb-0 border">
        <div class="d-flex flex-column align-items-start commented-user mt-2 mb-2" >
            <div class="d-flex gap-2 ">
                <h5 class="mr-2 mb-0 ml-1 fw-bold text-capitalize">${ res.author } </h5>
                <small class="text-muted text-decoration-underline bg-white">${currentTime}</small>
            </div>
            ⭐️⭐️⭐️⭐️⭐️

        </div>
        <div class="comment-text-sm review_content" data-id="${ res.id }" >
            <p class="my-2">${ res.content }</p>
            <div class="d-flex justify-content-end">
                <button class="edit_review btn mt-3 text-primary shadow-none" aria-label="update-review-button"  >
                <i class="bi bi-pencil-square" style="font-size:1.2rem; -webkit-text-stroke-width: 1px;"></i>
                </button>
                <button class="btn  mt-3 text-danger shadow-none" aria-label="delete-product-button" data-bs-toggle="modal" data-bs-target="#modal_${ res.id }">
                <i class="bi bi-trash" style="font-size:1.2rem; -webkit-text-stroke-width: 1px;"></i>
                </button>
            </div>
        </div>
    </div>

    `);
}

function addDeleteUrl(){
    if($('.delete-form')){
        var deleteUrl = $('#delete-url').val();
        $('.delete-form').attr('action',deleteUrl);
    }
}

//
$(document).ready(function(){
    addDeleteUrl();
    var editing_content = null;
    var review_id = null;
    var edit_container = null;

    $('.review-form').submit(function(event){
        event.preventDefault();
        var _submitBtn = $('.add_review');
        // setting default value since im using product id to pass review id in a view
        var _default_product_id = $('.default-product-id').val();

        var _productId = $('.product-id').val();
        var _user = $('.user').val();

        var _content = $('textarea[name="content"]').val();
        var createReviewUrl = $(this).data('create-review-url');
        var editReviewUrl=$('#edit-url').val();

        var currentTime = new Date().toLocaleString('en-US', {
            hour: 'numeric', minute: 'numeric', hour12: true
        });

        var url;

        if (editing_content === null){
                url=createReviewUrl;

        }else{
            url = editReviewUrl;
            data = {

            'user': _user,
            'product_id': _productId,
            'content': _content,
            'current_time': currentTime,
            'review-id': review_id,
            };
        }

        $.ajax({
                url: url,
                type: 'POST',
                cache: false,
                headers: {
                    'X-CSRFToken': $('#csrf').val()
                },
                data: {

                    'user':_user,
                    'product_id': _productId,
                    'content': _content,
                    'current_time': currentTime
                },
                dataType:'json',
                beforeSend:function(){
                    _submitBtn.attr('disabled',true);

                },
                success:function(res){
                    if(res.status==='created'){
                        appendReview(res);
                        addDeleteUrl();
                        $('.success-modal').modal('show');
                        $('.custom-content').text(res.message);

                    }
                    else if(res.status==='edited'){
                        console.log(res.content);
                        edit_container.text(res.content);
                        $('.add_review').text('Comment');

                        editing_content=null;
                        modalFading();
                        $('.custom-content').text(res.message);
                        $('.modal-header').css('border-top','3px solid green');
                        $('.review-form')[0].reset();
                        $('.product-id').val(_default_product_id);
                    }
                    _submitBtn.attr('disabled',false);
                    $('.review-form')[0].reset();
                }
        });

    });


    $('.commented-section').on('click', '.review_content', function(){

        var dataId = $(this).data('id');
        console.log(dataId);
    }).on('click', '.edit_review', function(event){
        event.stopPropagation();
        editing_content=$(this).parent().parent().children().first().text();
        edit_container=$(this).parent().parent().children().first();
        console.log(edit_container);
        review_id=$(this).parent().parent().attr('data-id');
        console.log(editing_content);
        console.log(review_id);
        $('#id_content').val(editing_content);
        $('.product-id').val(review_id);
        $('#id_content').focus();
        $('.add_review').text('Update review');
    });
});




