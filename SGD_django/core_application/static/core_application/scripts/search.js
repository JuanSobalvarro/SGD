// Filter buttons configuration
function filterSelection() {
    var btnContainer = document.getElementById("filters");
    var btns = btnContainer.getElementsByClassName("btn");
    
    for (var i = 0; i < btns.length; i++) 
    {
        btns[i].addEventListener("click", function() {
            var current = document.getElementsByClassName(" active");
            current[0].className = current[0].className.replace(" active", "");
            this.className += " active";
            search();
        });
    }
}

// Card creation function
function createCard(title, alias, imgUrl) {
    const cardHtml = `
        <div class="col-md-3">
            <div class="card">
                <img src="${imgUrl}" class="card-img-top" alt="${title}">
                <div class="card-body">
                    <h5 class="card-title">${title}</h5>
                    <p class="card-text">${alias}</p>
                    <a href="#" class="btn btn-primary card-button">Ver más</a>
                </div>
            </div>
        </div>
    `;

    const cardContainer = document.getElementById('results-container');
    cardContainer.innerHTML += cardHtml;
}

// Clear cards function
function clearCards() {
    const cardContainer = document.getElementById('results-container');
    cardContainer.innerHTML = '';
}

// Initial search
document.querySelector('.busqueda').addEventListener('submit', function(event) {
    event.preventDefault();
    search();
});

// Search algorithm
function search() {
    const query = document.getElementById('search-input').value;
    const filter = document.querySelector('.filter.active').id;

    console.log('Searching for:', query, 'with filter:', filter);

    fetch(`/search-api/?search=${encodeURIComponent(query)}&filter=${encodeURIComponent(filter)}`)
        .then(response => response.json())
        .then(data => {
            clearCards();

            if (data.results.length === 0) {
                document.getElementById('results-container').innerHTML = '<p id="not_found_message">No se encontraron resultados.</p>';
            } else {
                data.results.forEach(result => {
                    createCard(result.title, result.alias, result.image);
                });
            }
        })
        .catch(error => {
            console.error('Error fetching search results:', error);
            document.getElementById('results-container').innerHTML = '<p>Error al buscar resultados.</p>';
        });
}

filterSelection();


