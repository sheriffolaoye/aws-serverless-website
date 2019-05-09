var HttpClient = function() {
    this.get = function(aUrl, aCallback) {
        var HttpRequest = new XMLHttpRequest();
        HttpRequest.onreadystatechange = function() { 
            if (HttpRequest.readyState == 4 && HttpRequest.status == 200)
                aCallback(HttpRequest.responseText);
        }

        HttpRequest.open("GET", aUrl, true);   
        HttpRequest.send(null);
    }
}

var url = "https://c3pzc9vqi9.execute-api.us-east-1.amazonaws.com/default/restAPI";
var client = new HttpClient();

var repos = client.get(url, function(response) {
    var repos = JSON.parse(response);
    var text = "";

    for(i=0; i < repos.length; i++){
        text = text +  `<div class='project-card'>
                            <div class='project-card-body'>
                                <h2 class='project-card-title'>
                                    <strong>`
                                        + repos[i]["Name"] + 
                                    `</strong>
                                </h2>
                                <p>`
                                    + repos[i]["Description"] + 
                                    `<br>Language: ` + repos[i]["Language"] +
                                    `<br>Date Created: ` + repos[i]["DateCreated"] +
                                `</p>
                                <a href='` + repos[i]["HtmlLink"] + `'  target='_blank'>View on GitHub</a>
                            </div>
                        </div>`;
    }

    document.getElementById("project-container").innerHTML = text;
});