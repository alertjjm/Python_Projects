var url = "https://api.bithumb.com/public/ticker/BTC";

request(url, function(error, response, body) {
  if (error) throw error;

  var $ = cheerio.load(body);

  var postElements = $("section.posts article.post");
  postElements.each(function() {
    var postTitle = $(this).find("h1").text();
    var postUrl = $(this).find("h1 a").attr("href");
  });
});
