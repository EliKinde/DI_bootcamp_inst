const tasks = [];

function addTask(task) {
    // Check if the task is not empty
    if (task.trim() === "") return;

    // Add the task to the array
    tasks.push(task);

    // Create a new task item in the DOM
    const taskItem = document.createElement('div');
    taskItem.className = 'task-item';

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';

    const label = document.createElement('label');
    label.textContent = task;

    const deleteBtn = document.createElement('i');
    deleteBtn.className = 'fas fa-times delete-btn';
    deleteBtn.onclick = () => {
        tasks.splice(tasks.indexOf(task), 1); // Remove the task from the array
        taskItem.remove(); // Remove the task from the DOM
    };

    // Append elements to the task item
    taskItem.appendChild(checkbox);
    taskItem.appendChild(label);
    taskItem.appendChild(deleteBtn);

    // Append task item to the list
    document.querySelector('.listTasks').appendChild(taskItem);
}

document.getElementById('taskForm').addEventListener('submit', function(event) {
    //event.preventDefault(); // Prevent form submission
    const taskInput = document.getElementById('taskInput');
    addTask(taskInput.value); // Add the task
    taskInput.value = ''; // Clear the input
});

