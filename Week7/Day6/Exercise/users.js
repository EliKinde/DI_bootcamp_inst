// 🌟 Exercise 5 : Users

let container = document.getElementById("container");
console.log(container);

let changeName = document.getElementsByClassName('list');

changeName[0].children[1].innerText = "Richard";
changeName[1].children[1].remove();

for(let i=0;i < changeName.length; i++) {
  if(changeName[i].children[0]) {
    changeName[i].children[0].innerText = "Elihyu";
  }
}

for(let i=0; i < changeName.length; i++) {
 changeName[i].classList.add('student_list');
};

changeName[0].classList.add('university','attendance');

container.style.color = "lightblue";
container.style.padding = "10px";


changeName[0].children[1].style.border= "10px solid red";


changeName[1].children[1].style.display = "none";

document.body.style.fontSize = "2em";

if(container.style.color === "lightblue") {
  alert("Hello x and y");
}
