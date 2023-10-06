import scrapy
from optivivienda_scraper.items import OptiviviendaScraperItem

class OptiviviendaSpiderItem(scrapy.Spider):
    name = 'properati_venta_scraper'
    allowed_domains = ['www.properati.com.co']
    start_urls = ['https://www.properati.com.co/s/tunja-boyaca/venta']
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.properati.com.co/',
}
    def parse(self, response):
        # Obtener enlaces a las páginas de detalle
        detalle_links = response.xpath('//*[@id="listings-content"]/a/@href').getall()
        print("////////////////////////////////////////////////////////////////")
        print(detalle_links)
        for link in detalle_links:
            # Crear una solicitud para seguir el enlace a la página de detalle
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_detalle)
            # yield scrapy.Request(url=response.urljoin(link), headers=headers, callback=self.parse)


        # Manejar paginación
        next_page = response.xpath('//*[@id="listings"]/div/div[1]/a[5]/@href').get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)

    def parse_detalle(self, response):
        self.log(f'Página: {response.url}')
        # Extraer datos de la página de detalle
        metrocuadrado_item = OptiviviendaScraperItem()
        metrocuadrado_item['titulo'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[1]/h1/text()').get()
        metrocuadrado_item['precio'] = response.xpath('//*[@id="prices-and-fees"]/div[1]/div/text()').get()
        metrocuadrado_item['ubicacion'] = response.xpath('//div[@class="location"]/text()').get()
        metrocuadrado_item['descripcion'] =  response.xpath('//*[@id="description-text"]/text()').get()
        metrocuadrado_item['tipo_inmueble'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/div/span[2]/text()').get()
        metrocuadrado_item['tipo_operacion'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[4]/div[3]/div/span[2]/text()').get()
        metrocuadrado_item['estrato'] =response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[4]/div[2]/div/span[2]/text()').get()
        metrocuadrado_item['numero_habitaciones'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/text()').get()
        metrocuadrado_item['numero_baños'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/div[2]/text()').get()
        metrocuadrado_item['area'] = response.xpath('//div[@class="place-features"]/div[@class="spec "][5]/div/span[@class="place-features__values"]/text()').get()
        metrocuadrado_item['caracteristicas'] = response.xpath('//div[@id="facilities__options"]//div[@class="facilities__item"]/li/span/text()').getall()

        yield metrocuadrado_item


class OptiviviendaSpiderItem2(scrapy.Spider):
    name = 'properati_arriendo_scraper'
    allowed_domains = ['www.properati.com.co']
    start_urls = ['https://www.properati.com.co/s/tunja-boyaca/arriendo']
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.properati.com.co/',
}
    def parse(self, response):
        # Obtener enlaces a las páginas de detalle
        detalle_links = response.xpath('//*[@id="listings-content"]/a/@href').getall()
        print("////////////////////////////////////////////////////////////////")
        print(detalle_links)
        for link in detalle_links:
            # Crear una solicitud para seguir el enlace a la página de detalle
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_detalle)
            # yield scrapy.Request(url=response.urljoin(link), headers=headers, callback=self.parse)


        # Manejar paginación
        next_page = response.xpath('//*[@id="listings"]/div/div[1]/a[5]/@href').get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)

    def parse_detalle(self, response):
        self.log(f'Página: {response.url}')
        # Extraer datos de la página de detalle
        metrocuadrado_item = OptiviviendaScraperItem()
        metrocuadrado_item['titulo'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[1]/h1/text()').get()
        metrocuadrado_item['precio'] = response.xpath('//*[@id="prices-and-fees"]/div[1]/div/text()').get()
        metrocuadrado_item['ubicacion'] = response.xpath('//div[@class="location"]/text()').get()
        metrocuadrado_item['descripcion'] =  response.xpath('//*[@id="description-text"]/text()').get()
        metrocuadrado_item['tipo_inmueble'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/div/span[2]/text()').get()
        metrocuadrado_item['tipo_operacion'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[4]/div[3]/div/span[2]/text()').get()
        metrocuadrado_item['estrato'] =response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[4]/div[2]/div/span[2]/text()').get()
        metrocuadrado_item['numero_habitaciones'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/text()').get()
        metrocuadrado_item['numero_baños'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/div[2]/text()').get()
        metrocuadrado_item['area'] = response.xpath('//div[@class="place-features"]/div[@class="spec "][5]/div/span[@class="place-features__values"]/text()').get()
        metrocuadrado_item['caracteristicas'] = response.xpath('//div[@id="facilities__options"]//div[@class="facilities__item"]/li/span/text()').getall()

        yield metrocuadrado_item        

# //////////////////////////////////////////////////
class OptiviviendaSpiderItem3(scrapy.Spider):
    name = 'nuroa_venta_scraper'
    allowed_domains = ['www.nuroa.com.co']
    start_urls = ['https://www.nuroa.com.co/venta/tunja?page=1']
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.nuroa.com.co/',
}
    def parse(self, response):
        # Obtener enlaces a las páginas de detalle
        detalle_links = response.xpath('//*[@id="nu_results_container"]/div/h3/a/@href').getall()
        print("////////////////////////////////////////////////////////////////")
        print(detalle_links)
        for link in detalle_links:
            # Crear una solicitud para seguir el enlace a la página de detalle
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_detalle)
            # yield scrapy.Request(url=response.urljoin(link), headers=headers, callback=self.parse)

        # Manejar paginación
                # Manejar paginación
        current_page = int(response.url.split('=')[-1])
        next_page_url = f'https://www.nuroa.com.co/venta/tunja?page={current_page + 1}'
        
        yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_detalle(self, response):
        self.log(f'Página: {response.url}')
        # Extraer datos de la página de detalle
        metrocuadrado_item = OptiviviendaScraperItem()
        metrocuadrado_item['titulo'] = response.xpath('//div[@class="left-details"]/div[@class="main-title"]/text()').get()
        metrocuadrado_item['precio'] = response.xpath('//*[@id="prices-and-fees"]/div/div/text()').get()
        metrocuadrado_item['ubicacion'] = response.xpath('//*[@id="location-map"]/div[2]/text()').get()
        metrocuadrado_item['descripcion'] =  response.xpath('//*[@id="description-text"]/text()').get()
        metrocuadrado_item['tipo_inmueble'] = response.xpath('//div[@class="place-features"]//div[@class="property-type"]/span[@class="place-features__values"]/text()').get()
        metrocuadrado_item['tipo_operacion'] = response.xpath('//div[@class="place-features"]//div[@class="operation-type"]/span[@class="place-features__values"]/text()').get()
        metrocuadrado_item['estrato'] = response.xpath('//div[@class="place-features"]//div[@class="stratum"]/span[@class="place-features__values"]/text()').get()
        metrocuadrado_item['numero_habitaciones'] = response.xpath('//div[@class="place-details"]//div[contains(@class, "details-item--some-elements-showing")]/div[contains(@class, "details-item-icon")]/following-sibling::div[contains(@class, "details-item-value")]/text()').get()
        metrocuadrado_item['numero_baños'] = response.xpath('//div[contains(@class, "details-item-value") and contains(text(), "baños")]/text()').get()
        metrocuadrado_item['area'] = response.xpath('//div[contains(@class, "floor-area")]/span[@class="place-features__values"]/text()').get()
        metrocuadrado_item['caracteristicas'] = response.xpath('//div[@class="facilities__options"]//span/text()').getall()

        yield metrocuadrado_item

# ///////////////////////////////////////
class OptiviviendaSpiderItem4(scrapy.Spider):
    name = 'nuroa_arriendo_scraper'
    allowed_domains = ['www.nuroa.com.co']
    start_urls = ['https://www.nuroa.com.co/arriendo/tunja?page=1']
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.nuroa.com.co/',
}
    def parse(self, response):
        # Obtener enlaces a las páginas de detalle
        detalle_links = response.xpath('//*[@id="nu_results_container"]/div/h3/a/@href').getall()
        print("////////////////////////////////////////////////////////////////")
        print(detalle_links)
        for link in detalle_links:
            # Crear una solicitud para seguir el enlace a la página de detalle
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_detalle)
            # yield scrapy.Request(url=response.urljoin(link), headers=headers, callback=self.parse)

        # Manejar paginación
                # Manejar paginación
        current_page = int(response.url.split('=')[-1])
        next_page_url = f'https://www.nuroa.com.co/arriendo/tunja?page={current_page + 1}'
        
        yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_detalle(self, response):
        self.log(f'Página: {response.url}')
        # Extraer datos de la página de detalle
        metrocuadrado_item = OptiviviendaScraperItem()
        metrocuadrado_item['titulo'] = response.xpath('//div[@class="left-details"]/div[@class="main-title"]/text()').get()
        metrocuadrado_item['precio'] = response.xpath('//*[@id="prices-and-fees"]/div/div/text()').get()
        metrocuadrado_item['ubicacion'] = response.xpath('//*[@id="location-map"]/div[2]/text()').get()
        metrocuadrado_item['descripcion'] =  response.xpath('//*[@id="description-text"]/text()').get()
        metrocuadrado_item['tipo_inmueble'] = response.xpath('//div[@class="place-features"]//div[@class="property-type"]/span[@class="place-features__values"]/text()').get()
        metrocuadrado_item['tipo_operacion'] = response.xpath('//div[@class="place-features"]//div[@class="operation-type"]/span[@class="place-features__values"]/text()').get()
        metrocuadrado_item['estrato'] = response.xpath('//div[@class="place-features"]//div[@class="stratum"]/span[@class="place-features__values"]/text()').get()
        metrocuadrado_item['numero_habitaciones'] = response.xpath('//div[@class="place-details"]//div[contains(@class, "details-item--some-elements-showing")]/div[contains(@class, "details-item-icon")]/following-sibling::div[contains(@class, "details-item-value")]/text()').get()
        metrocuadrado_item['numero_baños'] = response.xpath('//div[contains(@class, "details-item-value") and contains(text(), "baños")]/text()').get()
        metrocuadrado_item['area'] = response.xpath('//div[contains(@class, "floor-area")]/span[@class="place-features__values"]/text()').get()
        metrocuadrado_item['caracteristicas'] = response.xpath('//div[@class="facilities__options"]//span/text()').getall()

        yield metrocuadrado_item


class OptiviviendaSpiderItem5(scrapy.Spider):
    name = 'mitula_all_scraper'
    allowed_domains = ['casas.mitula.com.co']
    start_urls = ['https://casas.mitula.com.co/searchRE/nivel2-Tunja/nivel1-Boyac%C3%A1/q-Tunja']
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.casas.mitula.com.co/',
}
    def parse(self, response):
        # Obtener enlaces a las páginas de detalle
        detalle_links = response.xpath('//*[@id="listings-content"]/a/@href').getall()
        print("////////////////////////////////////////////////////////////////")
        print(detalle_links)
        for link in detalle_links:
            # Crear una solicitud para seguir el enlace a la página de detalle
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_detalle)
            # yield scrapy.Request(url=response.urljoin(link), headers=headers, callback=self.parse)


        # Manejar paginación
        next_page = response.xpath('//*[@id="listingListFooter"]/div[2]/ul/li[6]/a/@href').get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)

    def parse_detalle(self, response):
        self.log(f'Página: {response.url}')
        # Extraer datos de la página de detalle
        metrocuadrado_item = OptiviviendaScraperItem()
        metrocuadrado_item['titulo'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[1]/text()').get()
        metrocuadrado_item['precio'] = response.xpath("//*[@id='prices-and-fees']/div[1]/div/text()").get()
        metrocuadrado_item['ubicacion'] = response.xpath('//div[@class="location"]/text()').get()
        metrocuadrado_item['descripcion'] =  response.xpath('//*[@id="description-text"]/text()').get()
        metrocuadrado_item['tipo_inmueble'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/div/span[2]/text()').get()
        metrocuadrado_item['tipo_operacion'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[4]/div[3]/div/span[2]/text()').get()
        metrocuadrado_item['estrato'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[4]/div[2]/div/span[2]/text()').get()
        metrocuadrado_item['numero_habitaciones'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/text()').get()
        metrocuadrado_item['numero_baños'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/div[2]/text()').get()
        metrocuadrado_item['area'] = response.xpath('//div[@class="place-features"]/div[@class="spec "][5]/div/span[@class="place-features__values"]/text()').get()
        metrocuadrado_item['caracteristicas'] = response.xpath('//div[@id="facilities__options"]//div[@class="facilities__item"]/li/span/text()').getall()

        yield metrocuadrado_item


class OptiviviendaSpiderItem6(scrapy.Spider):
    name = 'mitula_all_scraper'
    allowed_domains = ['airbnb.com.co']
    start_urls = ['https://www.airbnb.com.co/s/Tunja--Boyac%C3%A1--Colombia/homes']
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.airbnb.com.co/',
}
    def parse(self, response):
        # Obtener enlaces a las páginas de detalle
        detalle_links = response.xpath('//*[@id="listings-content"]/a/@href').getall()
        print("////////////////////////////////////////////////////////////////")
        print(detalle_links)
        for link in detalle_links:
            # Crear una solicitud para seguir el enlace a la página de detalle
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_detalle)
            # yield scrapy.Request(url=response.urljoin(link), headers=headers, callback=self.parse)


        # Manejar paginación
        next_page = response.xpath('//*[@id="listingListFooter"]/div[2]/ul/li[6]/a/@href').get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)

    def parse_detalle(self, response):
        self.log(f'Página: {response.url}')
        # Extraer datos de la página de detalle
        metrocuadrado_item = OptiviviendaScraperItem()
        metrocuadrado_item['titulo'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[1]/text()').get()
        metrocuadrado_item['precio'] = response.xpath("//*[@id='prices-and-fees']/div[1]/div/text()").get()
        metrocuadrado_item['ubicacion'] = response.xpath('//div[@class="location"]/text()').get()
        metrocuadrado_item['descripcion'] =  response.xpath('//*[@id="description-text"]/text()').get()
        metrocuadrado_item['tipo_inmueble'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/div/span[2]/text()').get()
        metrocuadrado_item['tipo_operacion'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[4]/div[3]/div/span[2]/text()').get()
        metrocuadrado_item['estrato'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[4]/div[2]/div/span[2]/text()').get()
        metrocuadrado_item['numero_habitaciones'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/text()').get()
        metrocuadrado_item['numero_baños'] = response.xpath('/html/body/section/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/div[2]/text()').get()
        metrocuadrado_item['area'] = response.xpath('//div[@class="place-features"]/div[@class="spec "][5]/div/span[@class="place-features__values"]/text()').get()
        metrocuadrado_item['caracteristicas'] = response.xpath('//div[@id="facilities__options"]//div[@class="facilities__item"]/li/span/text()').getall()

        yield metrocuadrado_item
