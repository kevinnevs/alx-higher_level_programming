//JQuery API
$.ajax({
    url: "https://fourtonfish.com/hellosalut/?lang=fr",
    type: 'GET',
    dataType: 'json'
})
  .done(function (json) {
    $('DIV#hello').text(json.hello);
});