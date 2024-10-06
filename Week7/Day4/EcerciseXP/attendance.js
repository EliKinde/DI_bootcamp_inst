// Exercise 2 : Attendance

let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}

let student = prompt("Enter your name: ");

if (student in guestList) {
  console.log(`Hi! I'm ${student}, and I'm from ${guestList[student]}.`);
} else {
  console.log("Sorry, you're not on the guest list.");
}
