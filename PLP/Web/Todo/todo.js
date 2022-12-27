
let todos = [
    'Get groceries',
    'Make dinner',
    'Wash car',
    '' ];

todos.push('Do laundry');
console.log(todos);
render();

function addTodo() {
    let textbox = document.getElementById('todo-task');
    let task = textbox.value;
    todos.push(task);

    render();
    }

function render() {
    document.getElementById('todo-list').innerHTML = '';
    todos.forEach(function(todo) {
    let element = document.createElement('div');
    element.innerHTML = todo;
    let todoList = document.getElementById('todo-list');
    todoList.appendChild(element);
    });

}

