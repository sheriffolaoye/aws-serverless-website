// function to show projects

function showProjects(){
    var repos = sessionStorage.getItem("projects");

    if(repos){
        var repos = JSON.parse(repos)
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

        document.getElementById("project-container").innerHTML = text;
    }else{
        console.log("no data")
    }
}
