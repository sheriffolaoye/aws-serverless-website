// function to retrieve repositiory data
function getRepositories() {
    var url = "https://c3pzc9vqi9.execute-api.us-east-1.amazonaws.com/default/restAPI";
    var HttpRequest = new XMLHttpRequest();

    HttpRequest.onreadystatechange = function() { 
        if (HttpRequest.readyState == 4 && HttpRequest.status == 200){
            var response = HttpRequest.responseText;
            sessionStorage.setItem("projects", response);
            var visited = sessionStorage.getItem("visitedIndex");

            if(visited !== "yes"){
                var repos = JSON.parse(response)
                showProjects(repos);
            }
        }
    }

    HttpRequest.open("GET", url, true);   
    HttpRequest.send();
};

// function to hide loading gif and show projects
function showProjects(repos){
    var text = ""

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

    document.getElementById("loading-img").style.display = "none";
    document.getElementById("project-container").innerHTML = text;
}

function getProjects(){
    var repos = sessionStorage.getItem("projects");
    var visitedIndex = sessionStorage.getItem("visitedIndex");

    if(repos || visitedIndex === "yes"){
        var repos = JSON.parse(repos)
        showProjects(repos);
    }else{
        getRepositories();
    }
}
