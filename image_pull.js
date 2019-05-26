const fs = require("fs");
var articles = [];

fs.readdirSync('./src/assets/articles/').forEach(image => {
  const image_object = {
    "title": 'roahcosmetics&lashes',
    "hero": image, // REQUIRED
    "category": 'Cosmetics & Lashes',
    "author": '',
    "prominent": false // (Math.floor(Math.random() * 6) + 1) > 4 ? true:false
  }
  console.log(image_object);
  articles.push(image_object)
});

fs.writeFileSync('./articles.json', JSON.stringify(articles));
