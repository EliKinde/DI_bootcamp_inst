// 🌟 Exercise 1 : Colors

const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
/*
for(let i=0; i<colors.length; i++) {
  console.log(`${i+1}# choice is ${colors[i]}`);
}
*/

colors.forEach(myFun);
function myFun(val, index, array) {
  console.log(`${index+1}# choice is ${array[index]}`);
};
if(colors[-1] === 'Violet') {
  console.log('Yeah');
} else {
  console.log('No...');
}
