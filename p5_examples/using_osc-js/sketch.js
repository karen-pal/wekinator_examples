// Using osc-js 
// https://github.com/adzialocha/osc-js
let port = 8081;
let osc;

function setup() {
  createCanvas(400, 400);
  
  osc = new OSC();
  osc.open({host:"localhost", port: port}) //connect to server that was created by the bridge

  
}

function draw() {
  background(220);
  text(mouseX+"   ⬄   "+map(mouseX, 0, width, 0, 1), height/2, width/2);
}

function mouseMoved() {
  let normX = map(mouseX, 0, width, 0, 1);
  print(normX.toString());
  var message = new OSC.Message('/test/', normX.toString());
  osc.send(message);  //send message on click
}
