function removecolor() {
    const selectElement = document.getElementById('colorSelect');
    const selectedValue = selectElement.value;

    // Loop through options and remove the selected one
    for (let i = 0; i < selectElement.options.length; i++) {
        if (selectElement.options[i].value === selectedValue) {
            selectElement.remove(i);
            break; // Exit the loop after removing
        }
    }
}

document.getElementById('removeButton').addEventListener('click', removecolor);

