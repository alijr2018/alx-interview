#!/usr/bin/node

const axios = require('axios');
const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

axios.get(apiUrl)
  .then(response => {
    const filmData = response.data;
    const characters = filmData.characters;

    characters.forEach(characterUrl => {
      axios.get(characterUrl)
        .then(response => {
          const characterData = response.data;
          console.log(characterData.name);
        });
    });
  });
