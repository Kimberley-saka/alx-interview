#!/usr/bin/node

const request = require('request')

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, async function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character in characters) {
      const res = await new Promise((resolve, reject) => {
        request(characters[character], (err, res, resBody) => {
          if (err) {
            reject(err);
          } else {
            resolve(JSON.parse(resBody).name);
          }
        });
      });
      console.log(res);
    }
  }
});
