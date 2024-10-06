const animateDiv = document.getElementById('animate');
const container = document.getElementById('container');
let position = 0;

//animateDiv.style.transform = `translateX(${position}px)`;


const interval = setInterval(myMove(), 1);

function myMove() {
  for(let i=0; i < 30; i++) {
  if (position < container.clientWidth - animateDiv.clientWidth) {
    position++;
    animateDiv.style.transform = `translateX(${position}px)`;
  } else {
    clearInterval(interval);
  }
  }
};

