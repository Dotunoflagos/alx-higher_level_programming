'use strict';
$(() => {
  const URL = 'https://swapi-api.hbtn.io/api';

  $.get(`${URL}/people/5/?format=json`, (data, status) => {
    $('DIV#character').html(data.name);
  });
});
