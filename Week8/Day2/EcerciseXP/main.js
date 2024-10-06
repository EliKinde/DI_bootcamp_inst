//function calculateTip() {
/*  let billAmount = document.getElementById("billamt").value;
  let serviceQuality = document.getElementById("serviceQual").value;
  let numberOfPeople = document.getElementById("peopleamt").value;


  console.log(billAmount);

*/
 //calculateTip();


document.getElementById('calculate').addEventListener('click', function() {
    const billAmount = document.getElementById('billamt').value;
    const serviceQuality = parseFloat(document.getElementById('serviceQual').value);
    const peopleAmount = document.getElementById('peopleamt').value;

    // Validate inputs
    if (serviceQuality === 0 || billAmount.trim() === '') {
        alert('Please enter both service quality and bill amount.');
        return;
    }

    // Convert values
    const bill = parseFloat(billAmount);
    const people = parseInt(peopleAmount) || 1; // default to 1 if empty or NaN

    // Calculate tip and total
    const tipAmount = bill * serviceQuality;
    const totalTip = tipAmount / people;

    // Display results
    document.getElementById('tip').textContent = totalTip.toFixed(2);
});

