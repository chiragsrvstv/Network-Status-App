var express = require("express");
var app = express();
var port = 3000


var bodyParser = require("body-parser");

// importing queries file
var db = require('./queries')

//
var request = require("request");

app.use(bodyParser.json())
app.use(
  bodyParser.urlencoded({
    extended: true,
  })
)

// just testing some json at home '/'
//app.get("/", function(req, res){
//  res.json({info: 'Node.js, Express, and Postgres API'})
//})

// tell express to listen for requests(statrt server)
app.listen(3000, function(){
  console.log("serving demo port 3000");
});

// routing '/details' with db.getDetails function
app.get('/details', db.getDetails);

// creating delete method
app.post('/delete', db.deleteData);

// creating details method
app.post('/createDetails', db.createDetails);



// working with the above API

  // homepage
app.get('/', function(req, res){
  request('http://localhost:3000/details', function(error, response, body){
    if(!error && response.statusCode == 200){
      var data = JSON.parse(body);
      res.render('home.ejs', {data: data});
    }
  })
});
