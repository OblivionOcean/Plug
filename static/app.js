function search() {
    var search = document.getElementById("search").value;
    var searchEngine = document.getElementsByName("SearchE")[0].checked ? "bing" : "google" ;
    fetch("/s", {
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ search: search, searchEngine: searchEngine })
    }).then(response => response.json()).then(data => {
        console.log(data);
    });
}