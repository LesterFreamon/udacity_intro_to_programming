let price = 15.00;
let money = 20.00;
if (money >= price) {
    console.log('buy the hammer')
} else {
    console.log('Do not buy the hammer')
}

// declares the sayHello function
function sayHello() {
  const message = "Hello!"
  return message; // returns value instead of printing it
}

// function returns "Hello!" and console.log prints the return value
console.log(sayHello());

function makeLine(length) {
    let line = "";
    for (let j = 1; j <= length; j++) {
        line += "* ";
    }
    return line + "\n";
}

function buildTriangle(size) {
    let totalLines = "";
    for (let i = 1; i <= size; i++) {
        totalLines += makeLine(i);
    }
    return totalLines
}


console.log(buildTriangle(10));