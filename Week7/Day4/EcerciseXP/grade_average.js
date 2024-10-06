// Exercise 2 : Grade Average

const grades = [85, 92, 76, 88, 95, 67, 82];

function findAvg(gradesList) {
  let total = 0;
  for(let i=0; i < gradesList.length; i++) {
    total += gradesList[i];
  }
  let average = total / gradesList.length;
  console.log(average);
  return average;
}

function check_pass_course(average) {
  if(average => 65) {
    alert("You have pass the course");
  } else {
    alert("You have failed and most repeat the course");
  }
}

check_pass_course(findAvg(grades));
