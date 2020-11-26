import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ArticleComponent } from './article/article.component';
import { HttpClientModule } from '@angular/common/http';
import { ArticleService } from './service/article.service';
import { FormsModule } from '@angular/forms';
import { NewArticlesComponent } from './new-articles/new-articles.component';

@NgModule({
  declarations: [
    AppComponent,
    ArticleComponent,
    NewArticlesComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [ArticleService],
  bootstrap: [AppComponent]
})
export class AppModule { }
