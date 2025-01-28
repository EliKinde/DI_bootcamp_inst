// #1
function funcOne() {
    let a = 5;
    if(a > 1) {
        a = 3;
    }
    alert(`inside the funcOne function ${a}`);
}

// #1.1 - run in the console:
funcOne()
// ** My Answer is the value of a is 3
// ** becuase the condintion is true and is change the value
// ** to 3


// #1.2 What will happen if the variable is declared
// with const instead of let ?
// ** it will throw error


//#2
let a = 0;
function funcTwo() {
    a = 5;
}

function funcThree() {
    alert(`inside the funcThree function ${a}`);
}

// #2.1 - run in the console:
funcThree()
funcTwo()
funcThree()
// ** the output is in the 0 and 5
// ** becuase when we call the funcTwo() we change the value to 5

// #2.2 What will happen if the variable is declared
// with const instead of let ?
// ** it will not change to value and it will TypeError


//#3
function funcFour() {
    window.a = "hello";
}


function funcFive() {
    alert(`inside the funcFive function ${a}`);
}

// #3.1 - run in the console:
funcFour()
funcFive()

//#4
let a = 1;
function funcSix() {
    let a = "test";
    alert(`inside the funcSix function ${a}`);
}

// ** the alert is 'test' becuase the scop of inside

// #4.1 - run in the console:
funcSix()
// #4.2 What will happen if the variable is declared
// with const instead of let ?
// ** it will not change to value and it will TypeError

//#5
let a = 2;
if (true) {
    let a = 5;
    alert(`in the if block ${a}`);
}
alert(`outside of the if block ${a}`);
// ** in both case the value is 5
//
// #5.1 - run the code in the console
// #5.2 What will happen if the variable is declared
// with const instead of let ?
// ** it will not change to value and it will TypeError
