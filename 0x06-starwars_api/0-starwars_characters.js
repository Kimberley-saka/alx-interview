import request from 'request';
import process from 'process';

const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}
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

      characterUrls.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error('Error fetching character:', charError);
          } else if (charResponse.statusCode !== 200) {
            console.error('Request failed with status code:', charResponse.statusCode);
          } else {
            const character = JSON.parse(charBody);
            console.log(character.name);
          }
        });
      });
    } catch (parseError) {
      console.error('Error parsing JSON response:', parseError);
    }
  }
});
