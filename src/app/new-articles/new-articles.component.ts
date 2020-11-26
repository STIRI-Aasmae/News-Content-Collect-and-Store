import { Component, OnInit } from '@angular/core';
import { Article } from "src/app/model/model.article";
import { ArticleService } from "src/app/service/article.service";

@Component({
  selector: 'app-new-articles',
  templateUrl: './new-articles.component.html',
  styleUrls: ['./new-articles.component.css']
})
export class NewArticlesComponent implements OnInit {
  
  article: Article = new Article();
  
  constructor(public articleservice:ArticleService) { }

  ngOnInit() {
  }

  storeArticles(){
    console.log(this.article)
    this.articleservice.storeArticles(this.article)
      .subscribe(data=>{
        console.log(data)
      },err=>{
        console.log(err);
      })

  }

}
