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
        $('#output').val(data.output);
        $('#url-wrapper').css({"display": "block"});
        $('#url').val('');
    });
    e.preventDefault();
    });
});

function CopyText() {
    var copyText = document.getElementById("output");
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(copyText.value);
    
    var tooltip = document.getElementById("txttooltip");
    tooltip.innerHTML = "Copied";
  }
  
  function outFunc() {
    var tooltip = document.getElementById("txttooltip");
    tooltip.innerHTML = "Copy to clipboard";
  }