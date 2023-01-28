//JQuery API
$.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    type: "GET",
    dataType: 'json'
})
  .done(function (json) {
    let titles = json.results;
    for (let i = 0; i < titles.length; i++) {
      $('UL#list_movies').append('<li>' + titles[i].title + '</li>');    
    };
  });