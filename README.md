# News-Content-Collect-and-Store
This repository consists of three projects:
1. The first one **article** is an API develped using Djano framework and BeautifulSoup and newspaper3k libraries the first one is forweb crawlin and the second one is for news crawling and cleaning. In this API the user give the API a news website and the API extracte and clean all the articles and their related information (Authors, Title, Publish Date, The URL of the article that existe in the news website) and put them in a MongoDB database (here MongoDB Atlas).
![1](https://user-images.githubusercontent.com/61889763/100276457-dd88df00-2f61-11eb-9151-2d3fd12f4f6f.PNG)\
**Data on the database.**\
![2](https://user-images.githubusercontent.com/61889763/100277726-ee3a5480-2f63-11eb-9923-5fa68876cda1.PNG)\
2. The second one **Readarticle** is an API developed using Django and Djanogorestframework. In this API the user can retreive data from the database by searching articles by keyword.\
![3](https://user-images.githubusercontent.com/61889763/100280023-cf3dc180-2f67-11eb-9ca9-5efa5442fb34.PNG)\
3. The third one **articleFrontend** is the front-end of the two API that enable the user to interract with the APIs simply without having any information about the structre of the back-end.
