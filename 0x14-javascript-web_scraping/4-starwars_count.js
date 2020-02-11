#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const allMovies = JSON.parse(body);
    // console.log(allMovies['results'].length);
    let numOfAppereances = 0;
    for (let i = 0; i <= allMovies.results.length - 1; i++) {
      const characters = allMovies.results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].indexOf('18') !== -1) {
          numOfAppereances++;
        }
      }
    }
    // console.log(characters);
    console.log(numOfAppereances);
  }
});
