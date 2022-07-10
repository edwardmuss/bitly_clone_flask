$(document).ready(function() {
    $('#form').on('submit',function(e){
    $.ajax({
        data : {
        url : $('#url').val(),
        },
        type : 'POST',
        url : '/'
    })
    .done(function(data){
        $('#output').text(data.output).show();
    });
    e.preventDefault();
    });
});