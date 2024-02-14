#!/usr/bin/node

const axios = require('axios');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movieId>');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

axios.get(apiUrl)
  .then(response => {
    const filmData = response.data;
    const characters = filmData.characters;

    if (!characters || characters.length === 0) {
      console.error('No characters found for the specified movie ID.');
      process.exit(1);
    }

    characters.forEach(characterUrl => {
      axios.get(characterUrl)
        .then(response => {
          const characterData = response.data;
          console.log(characterData.name);
        })
        .catch(error => {
          console.error('Error fetching character data:', error.message);
          process.exit(1);
        });
    });
  })
  .catch(error => {
    console.error('Error fetching data from the Star Wars API:', error.message);
    process.exit(1);
  });
