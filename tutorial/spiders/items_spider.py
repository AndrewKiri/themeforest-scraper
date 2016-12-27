import scrapy
import json

class ItemSpider(scrapy.Spider):
    name = "items"

    def start_requests(self):
        urls = [
            'https://themeforest.net/user/cmsmasters/portfolio?page=1',
            'https://themeforest.net/user/cmsmasters/portfolio?page=2',
            'https://themeforest.net/user/cmsmasters/portfolio?page=3'
        ]
        for url in urls:
            page_number = url[len(url)-1]
            request = scrapy.Request(url=url, callback=self.parse)
            request.meta['page_number'] = page_number
            yield request

    def parse(self, response):
        response_obj = {}
        page_number = response.meta['page_number']
        counter = 1
        for item in response.css(".js-google-analytics__list-event-container"):
            sales = item.css(".product-list__sales-desktop::text").extract()
            if len(sales) > 1 :
                sales_number = sales[2]
            else :
                sales_number = "0"
            response_obj[counter] = {
                'title': item.css(".js-google-analytics__list-event-trigger::text")[2].extract(),
                'price': item.css(".product-list__price-desktop::text").extract_first(),
                'sales': sales_number
            }
            counter += 1
        filename = "cmsmasters_portfolio_page_" + page_number + ".json"
        with open(filename, 'w') as fp:
            json.dump(response_obj, fp)

#        print((response.css(".main-item::attr(data_id)")[0]).extract())
#        page = response.url.split("/")[-2]
#        filename = 'quotes-%s.html' % page
#        with open(filename, 'wb') as f:
#            f.write(response.body)
#        self.log('Saved file %s' % filename)