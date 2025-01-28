// Function to fetch random country data
async function fetchRandomCountry() {
    try {
        // Fetch the data from the API
        const response = await fetch('https://restcountries.com/v3.1/all');
        
        // Check if the response is okay (status code 200)
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        // Parse the JSON data
        const countries = await response.json();
        
        // Select a random country
        const randomIndex = Math.floor(Math.random() * countries.length);
        const randomCountry = countries[randomIndex];

        // Log the random country data
        console.log(randomCountry);
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

// Call the function
fetchRandomCountry();


