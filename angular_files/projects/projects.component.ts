import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Repository } from '../repo.model';

@Component({
  selector: 'app-projects',
  templateUrl: './projects.component.html',
  styleUrls: ['./projects.component.css']
})
export class ProjectsComponent implements OnInit {
  apiURL = "https://c3pzc9vqi9.execute-api.us-east-1.amazonaws.com/default/restAPI";
  repos: Repository;

  constructor(private http: HttpClient) {}

  getRepos(){
    console.log("Hello world")
    return this.http.get<Repository>(this.apiURL);
  }

  showRepos(){
    this.getRepos()
      .subscribe((data: Repository) => {
        this.repos = data;
    });
  }

  ngOnInit() {
    this.showRepos();
  }

}
