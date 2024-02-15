#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

request(url, async function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    const characters = JSON.parse(body).characters;

    const fetchCharacter = async (characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (err, res, html) => {
          if (err) {
            reject(err);
          } else {
            resolve(JSON.parse(html).name);
          }
        });
      });
    };

    for (const characterUrl of characters) {
      try {
        const characterName = await fetchCharacter(characterUrl);
        console.log(characterName);
      } catch (err) {
        console.error('Error fetching character:', err);
      }
    }
  }
});
