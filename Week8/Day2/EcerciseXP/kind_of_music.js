let option = document.getElementsByTagName("option");
const selectElement = document.getElementById('genres');

function updateSelectedValue() {
  for(let i=0; i < option.length; i++) {
    if(option[i].selected == true) {
        console.log(option[i].value);
    }
  }

}

selectElement.addEventListener('change', updateSelectedValue);

updateSelectedValue();

