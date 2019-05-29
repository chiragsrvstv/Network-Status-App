var p = new Ping();


p.ping("http://google.com", function(err, data) {
  // Also display error if err is returned.
  if (err) {
    console.log("error loading resource")
    data = data + " " + err;
  }
  document.getElementById("ping-google").innerHTML = data;
});

p.ping("http://guildbit.com", function(err, data) {
  if (err) {
    console.log("error loading resource")
    data = data + " " + err;
  }
  document.getElementById("ping-guildbit").innerHTML = data;
});

p.ping("http://sf.guildbit.com", function(err, data) {
  if (err) {
    console.log("error loading resource")
    data = data + " " + err;
  }
  document.getElementById("ping-guildbit-sf").innerHTML = data;
});

p.ping("http://ny.guildbit.com", function(err, data) {
  if (err) {
    console.log("error loading resource")
    data = data + " " + err;
  }
  document.getElementById("ping-guildbit-ny").innerHTML = data;
});

p.ping("http://am.guildbit.com", function(err, data) {
  if (err) {
    console.log("error loading resource")
    data = data + " " + err;
  }
  document.getElementById("ping-guildbit-am").innerHTML = data;
});
