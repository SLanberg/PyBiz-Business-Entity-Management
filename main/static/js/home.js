$(document).ready(function () {
  document
    .getElementById("search-input")
    .addEventListener("keydown", function (event) {
      if (event.key === "Enter" || event.keyCode === 13) {
        // Check if the input field is not empty to avoid redirection on an empty search
        var searchInput = document.getElementById("search-input").value;

        // Construct the URL with the search query
        var searchQuery = encodeURIComponent(searchInput);

        // Replace 'your-destination-url' with the URL you want to redirect to
        var url = "company_list?q=" + searchQuery;

        // Redirect to the search results page
        window.location.href = url;
      }
    });
});
