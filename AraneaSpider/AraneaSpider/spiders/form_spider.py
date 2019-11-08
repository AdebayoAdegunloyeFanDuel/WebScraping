from scrapy.http import FormRequest
from scrapy.spiders import Spider


class FormSpider(Spider):

    name = 'horseForms'

    start_urls = ['https://treehouse-projects.github.io/horse-land/form.html']

    def parse(self, response):
        formdata = {'firstname': 'Bee',
                    'lastname': 'Hot',
                    'jobtitle': 'Test'}

        # This passes the methos in the form and defines what to do after the post
        return FormRequest.from_response(response, formnumber=0,
                                         formdata=formdata,
                                         callback=self.after_post)

    def after_post(self, reponse):
        print('\n\n*************\nForm processed.\n')
        print(reponse)
        print('\n*************\n')

