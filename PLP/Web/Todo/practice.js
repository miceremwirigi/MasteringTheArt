// My to do list
let todos = [
    'Get groceries',
    'Make dinner',
    'Wash car' ];

todos.push('Do laundry');
console.log(todos);
todos.forEach(function(todo) {
    let element = document.createElement('div'); // Show my list in page
    element.innerHTML = todo;
    document.body.appendChild(element);
    });


    //console logs a string in uppercase
function toUpper(stringList) {
    stringList.forEach(function(string) { 
        console.log(string.toUpperCase());
    })}

    //makes and prints a list of double strings in console
function arrayDouble(stringList) {
    let newArray = [];
    stringList.forEach(function(string) {
        newArray.push(string);
        newArray.push(string);
    })
    console.log(newArray);
    }

    //adds numbers contained in a list and prins sum in console
function arraySum(numberList) {
    let total = 0;
    numberList.forEach(function(number) {
        total = total + number;
    })
    console.log(total);
}

///toUpper(todos);
///arrayDouble(todos);
///arraySum([1,2,3,4,5])


//changes the inertext of a button
function printDone(){
    let button = document.getElementById('todo-button'); // Fun Toggle button
    if (button.innerText != 'Done'){
        button.innerText = 'Done';
    }
    else if(button.innerText != 'Click'){
        button.innerText = 'Click';
    }   
}
 
// Simple up and down counter
let counterElement = document.createElement('div');
counterElement.id = 'counter';
counterElement.innerHTML = '0';
document.body.appendChild(counterElement);

let count = 0;

let counterButtonUp = document.createElement('button');
counterButtonUp.innerText = 'Up';
counterButtonUp.id = 'counter-button-up';
counterButtonUp.style.backgroundColor = "Purple";
document.body.appendChild(counterButtonUp);

document.getElementById('counter-button-up').onclick = function countUp(){
    count = count + 1;
    document.getElementById('counter').innerHTML = count;
}

let counterButtonDown = document.createElement('button');
counterButtonDown.innerText = 'Down';
counterButtonDown.id = 'counter-button-down';
counterButtonDown.style.backgroundColor = "Cyan";
document.body.appendChild(counterButtonDown);

document.getElementById('counter-button-down').onclick = function countDown(){
    count = count - 1;
    document.getElementById('counter').innerHTML = count;
}


// Tkaes input text, creates div and adds div to page content 
function updateText() {  
    let readInputElement = document.getElementById('text-input');     
    let addTextElement = document.createElement('div');
    addTextElement.innerHTML = readInputElement.value;
    document.body.appendChild(addTextElement);
    }

// Cart to add and delete fruit selection as a div to content page

let addCart = document.createElement('div');
addCart.id = 'cart';
document.body.appendChild(addCart);

cartList = ["Apple","Egg","Tomatoes","Oranges","Citrus"]
cartList.forEach(cartItem => {
    addButton(cartItem);
    addToCart(cartItem);
}
)
addButton("clear");
deleteCart();



function addButton(text) {
    let button = document.createElement('button');
    button.id = text.toLowerCase();
    button.innerText = text;
    document.body.appendChild(button);    
}
function addToCart(text) {
    let button = document.getElementById(text.toLowerCase());
    let cartItem = document.createElement('div');
    let cart = document.getElementById('cart');
    cartItem.innerText = button.innerText
    button.onclick = () => {cart.appendChild(cartItem)};
}
function deleteCart(){
    let button = document.getElementById("clear");
    let cart = document.getElementById('cart');
    
    button.onclick = () => {cart.innerHTML = ""};
}
