import { Component, NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ArticleComponent } from './article/article.component';
import { NewArticlesComponent } from "./new-articles/new-articles.component";
const routes: Routes = [
  {path:'article', component: ArticleComponent},
  {path:'new-articles', component: NewArticlesComponent},
  {path:'',redirectTo:'/article', pathMatch:'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
