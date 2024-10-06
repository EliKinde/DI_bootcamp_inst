/*
setTimeout(function alertHello() {
  alert("Hello World!");
  let div = document.getElementById("container");
  div.innerHTML = '<p>CreateElement example</p>';

}, 2000);
*/

let div = document.getElementById("container");

function addParagraph() {
  //let div = document.getElementById("container");
  //div.innerHTML = '<p>CreateElement example</p>';
  let p = document.createElement('p');
  p.textContent = 'Hello World';
  div.appendChild(p);

  if(div.children.length >= 5) {
    clearInterval(inter);
  }
}


let clear = document.getElementById('clear');

let inter = setInterval(addParagraph, 2000);

clear.addEventListener('click', () => {
  clearInterval(inter);
});
