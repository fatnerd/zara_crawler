from requests_html import HTMLSession,HTML
import time

class Crawler():
    def scrape(self,link):
        session = HTMLSession()

        url = session.get(link)
        url.html.render(timeout = 5,sleep = 2)

        # get title
        title = url.html.find('h1.product-name',first = True).text

        # get price
        price = url.html.find('span.main-price',first = True).text
        print(price)

        # get stock
        all_size = None
        stock = None
        out_list = []
        out_of_stock = url.html.find('label.back-soon')
        sizes = url.html.find('div.size-list')

        for size in sizes:
            s = str(size.text).split('\n')
            for i in range(len(s)-1):
                if len(s[i]) >= 2:
                    s.pop(i)
            all_size= s

        for out in out_of_stock:
            out_list += str(out.text).split('\n')
        print(out_list)
            

        for i in range(len(all_size)-1):
            if all_size[i] in out_list:
                all_size.pop(i)   
            stock = all_size
            
        print('title:'+title,'price:'+ price,stock,all_size) 
        return [title,price,stock,all_size]
