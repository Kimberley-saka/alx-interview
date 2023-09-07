#!/usr/bin/node
import request from 'request';

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
  } else {
    try {
      const movie = JSON.parse(body);
      const characterUrls = movie.characters;

      const fetchCharacterNames = (urls) => {
        if (urls.length === 0) {
          process.exit(0);
        }

        const characterUrl = urls.shift();
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error('Error fetching character:', charError);
          } else if (charResponse.statusCode !== 200) {
            console.error('Request failed with status code:', charResponse.statusCode);
          } else {
            const character = JSON.parse(charBody);
            console.log(character.name);

            fetchCharacterNames(urls);
          }
        });
      };

      fetchCharacterNames([...characterUrls]);
    } catch (parseError) {
      console.error('Error parsing JSON response:', parseError);
    }
  }
});
