var url = "https://c3pzc9vqi9.execute-api.us-east-1.amazonaws.com/default/restAPI";

fetch(url)
.then(response => response.json())
.then(data => showProjects(data));

// function to hide loading gif and show projects
function showProjects(repos){
    var text = ""

    for(i=0; i < repos.length; i++){
        text = text +  `<div class='project-card'>
                            <div class='project-card-body'>
                                <h4 class='project-card-title'>
                                    <strong>`
                                        + repos[i]["Name"] + 
                                    `</strong>
                                </h4>
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
