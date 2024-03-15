console.log("Hello world!");



// Variables undeclared
k = 5;
l = 6;
z
r = k + l;
console.log(z)
// integers have 4bits
//variables using var(initialisation)
var a = 67;     //  use 'var' if you MUST support old browsers.
var y = 6;
var z = a + y;
console.log(z)
// varables declared using let
let m = 6;
let n = 9;         // use 'let' if you can't use const
let p = m + n;
console.log(p)
// variables declared using const
const u = 5;
const v = 6;     // use const if the value should not be changed
const f = u + v
console.log(f)
// mixed variabes
const price1 = 55;
const price2 = 60;
let total = price1 + price2;
console.log(total)
}

//TEMPLATE STRING
let text = `Hello World!`;
console.log(text)
//quotes inside text
let Text = `He's often calls me "Johnny"`;
console.log(Text)
// multiline string
let t =
`The quick
brown fox
jumps over
the lazy dog`;
console.log(t)
//Interpolation syntax ${...}
let firstName = "JonnY";
let lastName = "Doxy";

let te = `Welcome ${firstName}, ${lastName}!`;
console.log(te)

//html templates

//arrow function
let myFunction = (a, b) => a * b;
console.log(myFunction(4,5))


// validation
function validateForm() {
    let x = document.forms["myForm"]["fname"].value;
    if (x == "") {
      alert("Name must be filled out");
      return false;
    }
  } 