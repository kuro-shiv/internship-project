document.getElementById("search-button").addEventListener("click", function() {
    const searchTerm = document.getElementById("search-input").value;
    
    // Make an API call to the backend search endpoint
    fetch(`/search?query=${encodeURIComponent(searchTerm)}`)
        .then(response => response.json())
        .then(data => {
            const resultsContainer = document.getElementById("results");
            resultsContainer.innerHTML = ''; // Clear previous results
            
            if (data.results.length === 0) {
                resultsContainer.innerHTML = '<p>No results found.</p>';
                return;
            }

            data.results.forEach(result => {
                const resultCard = document.createElement("div");
                resultCard.className = "result-card";
                resultCard.innerHTML = `
                    <h3>${result.title}</h3>
                    <a href="${result.link}" target="_blank">View</a>
                `;
                resultsContainer.appendChild(resultCard);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});
