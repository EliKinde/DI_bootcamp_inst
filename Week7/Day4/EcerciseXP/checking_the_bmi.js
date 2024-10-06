// Exercise 1 : Checking The BMI

let personOne = {
  FullName: "Jonh Wick",
  Mass: 80,
  Height: 1.80,
  calc_bmi: function() {
    let bmi = this.Mass / (this.Height * this.Height);
    return bmi;
  }
};

let personTwo = {
  FullName: "Make joiner",
  Mass: 180,
  Height: 1.50,
  calc_bmi: function() {
    let bmi = this.Mass / (this.Height * this.Height);
    return bmi;
  }
};

function compares_bmi(bmi_one, bmi_two) {
  if(bmi_one > bmi_two) {
    console.log(`The largest BMI is ${personOne["FullName"]}`);
  }
  else {
    console.log(`The largest BMI is ${personTwo["FullName"]}`);
}
};

compares_bmi(personOne.calc_bmi(), personTwo.calc_bmi());

