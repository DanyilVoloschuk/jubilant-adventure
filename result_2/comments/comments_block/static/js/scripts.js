function addCommentsToPage(data)
{
    var delete_button_appearance = "onmouseover=\"this.src = 'https://image.flaticon.com/icons/svg/1828/1828665.svg'\" onmouseout=\"this.src = 'https://image.flaticon.com/icons/svg/1828/1828744.svg'\"";
    var edit_button_appearance = "onmouseover=\"this.src = 'https://image.flaticon.com/icons/svg/526/526127.svg'\" onmouseout=\"this.src = 'https://image.flaticon.com/icons/svg/483/483923.svg'\"";
    var html_string = "";
    var user_name = data.user_name;
    var comment_text = data.comment_text;
    var comment_date = data.date;
    var commentId = data.id;
    html_string += "<li id='" +  commentId + "' class='comment'>";
    html_string += "<img "+ delete_button_appearance +" id='del-" +  commentId + "' src='https://image.flaticon.com/icons/svg/1828/1828744.svg' class='delCommentButton' style='display:inline; margin: right'>"
    html_string += "<p style='display:inline;'><b><i>" + user_name + " </i></b>"+comment_date+"</p>";
    html_string += "<p id='label-"+commentId+"' style='display: block; word-wrap: break-word;'>" + comment_text + "</p>";
    html_string += "<img id='btn-" +  commentId + "' "+ edit_button_appearance +" name='0' src='https://image.flaticon.com/icons/svg/483/483923.svg' class='editCommentButton'><br>";
    html_string += "<form id='commentEdit-"+commentId+"' class='commentEdit' style='display:none' action='#' method='PUT'>";
    html_string += "<input type='text' name='comment_text' style='width: 80%' value='"+comment_text+"'>";
    html_string += "<button type='submit' class='cancel'>send</button></form>"

    //console.log("FIRST")
    return html_string;
}

function getComments() {
    $.ajax({
        method: "GET",
        url: "http://127.0.0.1:8000/task/block",
        async: false,
        success: function(data){
            var container = document.getElementById("comments_list");

            for (var i = 0; i < data.length; i++){

                container.insertAdjacentHTML("afterbegin", addCommentsToPage(data[i]));
            }

        },
        error:
        function(error_data){
            console.log("error");
            location.reload();
        }
    })
}

function init() {
    getComments();
    clicker();
}

init()

function deleteComment(commentId){
    console.log("Success DEL ", commentId.split('-')[1]);
    var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        url: 'http://127.0.0.1:8000/task/index/delete/'+commentId.split('-')[1],
        method: "DELETE", //метод отправки
        headers:{"X-CSRFToken": $crf_token}, //
        success: function (response) {
//             btn.parentNode.remove();

            document.getElementById(commentId.split('-')[1]).remove();

        },
        error: function(response) { // Данные не отправлены
            console.log("Fall", response);
            location.reload();
        }
        });
}


function editCommentButton(comment)
{
    if (comment.name == 1){
        document.getElementById('commentEdit-'+comment.id.split('-')[1]).style.display = "none";
        comment.name = 0;
        return;
    }
    comment.name = 1;
    document.getElementById('commentEdit-'+comment.id.split('-')[1]).style.display = "inline-block";
    return;

}



function pad(number) {
        if (number < 10) {
            return '0' + number;
        }
        return number;
      }

function clicker(){
    $('.delCommentButton').on('click', function() {
        console.log(this.id);
        deleteComment(this.id);
    })
    $('.editCommentButton').on('click', function() {

        console.log('I am here!');
        editCommentButton(this);
    })


}

$(document).ready(function() {
    function func(){
    $( ".commentEdit" ).submit(function( event ) {
        var a = $(".commentEdit");
        var formData;
        var node;
        for (var i=0; i<a.length; i++)
        {
            if (a[i].id == this.id){
                console.log(a[i]);
                formData = 'comment_text='+a[i].comment_text.value;
                node = a[i];
                break;
            }
        }
        console.log(formData);
        var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        $.ajax({
            url: 'http://127.0.0.1:8000/task/index/edit/'+this.id.split('-')[1]+'/',
            method: "PUT",
            data: formData,
            headers:{"X-CSRFToken": $crf_token},
            success: function(response) { //Данные отправлены успешно
                console.log("Success", response);
                var line = document.getElementById('label-'+node.id.split('-')[1]).childNodes;
                var btn = document.getElementById('btn-'+node.id.split('-')[1]).childNodes;
                console.log(btn);
                line[0].data = node.comment_text.value;
                node.style.display = 'none';
            },
            error: function(response){
                console.log("ERMAC", response);
                location.reload();
            }
        })
        event.preventDefault();
    })}
    func();
    $( "#commentForm" ).submit(function( event ) {
        var date = new Date().getUTCFullYear()+'-'+ pad(new Date().getUTCMonth() + 1) + '-' + pad(new Date().getUTCDate())
        var formData = $("#commentForm").serialize()+"&date="+date;
        console.log(date);
        var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        $.ajax({
            url: "http://127.0.0.1:8000/task/index/add/", //url страницы
            method:     "POST", //метод отправки
            data: formData,  // Сеарилизуем объект
            headers:{"X-CSRFToken": $crf_token}, //
            success: function(response) { //Данные отправлены успешно
               console.log("Success", response)
               var container = document.getElementById("comments_list");
               container.insertAdjacentHTML("afterbegin", addCommentsToPage(response));

               $("#input_area").val('');
               $("#text_area").val('');

               $('#del-'+response.id).on('click', function() {
                    var commentId = response.id;
                    console.log(this.id);
                    $.ajax({
                    url: 'http://127.0.0.1:8000/task/index/delete/'+commentId,
                    method: "DELETE", //метод отправки
                    headers:{"X-CSRFToken": $crf_token}, //
                    success: function (response) {
                     document.getElementById(commentId).remove()
                        },
                    error: function(response) { // Данные не отправлены
                    console.log("Fall", response);
                    location.reload();
                        }
                    });
                });
                $('#btn-'+response.id).on('click', function() {
                    var comment = document.getElementById('commentEdit-'+response.id);
                    if (comment.name == 1){
                            comment.style.display = "none";
                            comment.name = 0;
                        }
                    else{
                            comment.name = 1;
                            comment.style.display = "inline-block";
                    }
                });
                func();

            },
            error: function(response) { // Данные не отправлены
                console.log("Fall", response);
                location.reload();
            }
        });
        event.preventDefault();

    });



})
