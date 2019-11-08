**Web scraping**

It's the automated collecting of data from the web by any means other than a program interacting with an API.
This is typically done through writing a program that requests data from a web server 
and obtain necessary information.

Many companies uses web scrapping to gain competitive advantage. 


Starting scrapy up via your terminal
- scrapy startproject AraneaSpider


Let's talk a little bit about what a couple of these files are used for in Aranea Spider.

- items.py is used to define a model of data for scraped items. Scrapy spiders can return scraped data as Python dicts.
As you know, dicts lack structure.

- We can use items.py to create containers, where we can put the data we get from a site.

- Middlewares allow for custom functionality to be built to customize the responses
what are sent to spiders.

- The pipeline.py is used to customize the processing of data. For example, you could write a pipeline that would cleanse the HTML,
then move down the processing pipeline to be validated, then store the information into a database.
Steps along the data processing path can be put into the pipeline.

- settings.py allows for the behavior of Scrapy components to be customized