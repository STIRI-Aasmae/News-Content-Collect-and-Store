import { HttpClient, HttpResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';

//import { map } from "rxjs/operators"; 
import 'rxjs/add/operator/map';
import { Observable } from "rxjs";
import { map } from 'rxjs-compat/operator/map';
import { Article } from "src/app/model/model.article";

@Injectable({
  providedIn: 'root'
})
export class ArticleService {

  constructor(public httpclient:HttpClient ){ }

  getArticlesByKeywords(Keywords:string){
    return this.httpclient.get("http://127.0.0.1:8087/api/articless?Article="+Keywords)
      //.subscribe(resp=>console.log(resp))
      //.map((res: Response) => res.json())
      .map(res => res );

  }

  storeArticles(article:Article){
    return this.httpclient.post("http://127.0.0.1:8000/add_article/", article)
      .map(resp=>resp);
  }
}
