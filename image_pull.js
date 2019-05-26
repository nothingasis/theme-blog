const fs = require("fs");
var articles = [];

fs.readdirSync('./src/assets/images/').forEach(image => {
  const image_object = {
    "title": '',
    "hero": image, // REQUIRED
    "category": 'Makeup',
    "author": '',
    "prominent": (Math.floor(Math.random() * 6) + 1) > 4 ? true:false
  }
  console.log(image_object);
  articles.push(image_object)
});

fs.writeFileSync('./articles.json', JSON.stringify(articles));
