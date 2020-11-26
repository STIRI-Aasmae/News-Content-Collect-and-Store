import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http'
import { ArticleService } from '../service/article.service';

@Component({
  selector: 'app-article',
  templateUrl: './article.component.html',
  styleUrls: ['./article.component.css']
})
export class ArticleComponent implements OnInit {
  pageArticles: any;
  Keyword:string="";
  //website:string="";
  constructor(public httpclient:HttpClient, public artileservice:ArticleService) { }

  ngOnInit() {
  }

  searchBKW(){
    this.artileservice.getArticlesByKeywords(this.Keyword)
      .subscribe(data=>{
        this.pageArticles=data;
      }, err=>{
        console.log(err);
      })
  }

  search(){
    this.searchBKW();
  }

}
