// 🌟 Exercise 2 : Your Favorite Colors

let colors = ["Red", "Blue", "Pink", "Green", "Yellow"];

for(let i=0; i < colors.length; ++i) {
  //let num = 1
  console.log(`My #${(i+1)} choice is ${colors[i]}`);
}


for(let i=0; i < colors.length; i++) {
  let num = i + 1;
  let suffix;
  if(num == 1) {
    suffix = 'st';
  } else if (num == 2) {
    suffix = 'nd';
  } else if (num == 3) {
    suffix = 'rd';
  } else {
    suffix = 'th';
  }
  console.log(`My ${num}${suffix} choice is ${colors[i]}`);
}
