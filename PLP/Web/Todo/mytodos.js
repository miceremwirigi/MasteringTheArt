// Model

if (window.localStorage.getItem("todos")){
    todos = window.localStorage.getItem("todos");
    todos = JSON.parse(todos)    
}
else {
    todos = [{
    title: "Clean Pen",
    date: "2023-04-18",
    id: "id1"
}];
}
// Save todos



//Views

// Display saved todos
function renderTodos(todos) {
    todos.forEach(todo => {
        let element = document.createElement("div");
        element.setAttribute("className", "displaytodo-"+todo.id);
        element.setAttribute("id", "displaytodo");
        element.innerHTML = todo.title + " " + todo.date;
        document.body.appendChild(element);    
    });
}

// Inputs to add todos
function renderInputSection(){

    let inputbox = document.createElement("input");
    inputbox.type = "text";
    inputbox.id = "text-input-box";
    inputbox.className = "inputBox"
    inputbox.placeholder = "new todo";
    document.body.appendChild(inputbox);

    inputbox = document.createElement("input");;
    inputbox.type = "date";
    inputbox.id = "date-input-box";
    inputbox.className = "inputBox"
    document.body.appendChild(inputbox);

    element = document.createElement("button");
    element.id="add-todo-button";
    element.innerHTML = "Add Todo";
    document.body.appendChild(element);
}

function renderTableSection(todos){
    let table = document.createElement("table");
    document.body.appendChild(table);

    function generateTableHead(table, data){
        let thead = table.createTHead();
        let row = thead.createRow();
        for (let key of data){
            let th = document.createElement("th");
            let text = document.createTextNode(key);
            th.appendChild(text);
            thead.appendChild(th);
        }
    };

    table = document.querySelector("table");
    let data = Object.keys(todos[0]);
    generateTableHead(table, data);
}


// Controller

renderInputSection();
renderTodos(todos);
renderTableSection(todos);



element = document.getElementById("add-todo-button");
element.addEventListener("click", addTodo);

function addTodo(){
    let title = document.getElementById("text-input-box").value;
    let date = document.getElementById("date-input-box").value;
    let id = new Date().getTime();
    todos.push({ title, date, id });
    window.localStorage.setItem("todos", JSON.stringify(todos));
    renderTodos(todos);
}

console.log(todos);
