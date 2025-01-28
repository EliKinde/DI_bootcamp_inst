const tasks = [];

function addTask(task) {
};

document.getElementById('taskForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const taskInput = document.getElementById('taskInput');
    addTask(taskInput.value);
    taskInput.value = '';
});
