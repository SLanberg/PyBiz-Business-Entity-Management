function searchCompanies() {
    // Get the search input value
    var searchInput = document.getElementById("search-input").value;

    // Construct the URL with the search query
    var searchQuery = encodeURIComponent(searchInput);
    var url = "company-list?q=" + searchQuery;

    // Redirect to the search results page
    window.location.href = url;
}
