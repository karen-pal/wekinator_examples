let port = 8081;
let socket;

function setup() {
  createCanvas(400, 400);
  let thing;
  let normX;

  socket = new osc.WebSocketPort({
    url: 'ws://localhost:' + port
  });
  socket.on('message', handleOsc);
  socket.open();
}

function draw() {
}

function mouseMoved() {
  let valueMapped = parseInt(map(mouseX,0,300,0,256));
  background(valueMapped);
  thing = mouseX.toString();
  socket.send({
    address: '/asd',
    args: [thing]
  });
  console.log(valueMapped);
  console.log("> sendt: ", thing)
  return false;

}

function handleOsc(msg) {
  if (msg.address === '/1/fader1') {
  } else if (msg.address === '/1/fader2') {
  } else if (msg.address === '/1/fader3') {
  } else if (msg.address === '/1/fader4') {
  }
}
