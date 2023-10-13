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
        print(detalle_links)
        for link in detalle_links:
            # Crear una solicitud para seguir el enlace a la página de detalle
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_detalle)


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
        print(detalle_links)
        for link in detalle_links:
            # Crear una solicitud para seguir el enlace a la página de detalle
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_detalle)


        # Manejar paginación
        next_page = response.xpath('//*[@id="listings"]/div/div[1]/a[5]/@href').get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)

    def parse_detalle(self, response):
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
        print(detalle_links)
        for link in detalle_links:
            # Crear una solicitud para seguir el enlace a la página de detalle
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_detalle)

        # Manejar paginación
                # Manejar paginación
        current_page = int(response.url.split('=')[-1])
        next_page_url = f'https://www.nuroa.com.co/venta/tunja?page={current_page + 1}'
        
        yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_detalle(self, response):
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
        print(detalle_links)
        for link in detalle_links:
            # Crear una solicitud para seguir el enlace a la página de detalle
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_detalle)

        # Manejar paginación
        current_page = int(response.url.split('=')[-1])
        next_page_url = f'https://www.nuroa.com.co/arriendo/tunja?page={current_page + 1}'
        
        yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_detalle(self, response):
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
        print(detalle_links)
        for link in detalle_links:
            # Crear una solicitud para seguir el enlace a la página de detalle
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_detalle)


        # Manejar paginación
        next_page = response.xpath('//*[@id="listingListFooter"]/div[2]/ul/li[6]/a/@href').get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)

    def parse_detalle(self, response):
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
    name = 'airbnb_all_scraper'
    allowed_domains = ['airbnb.com.co']
    start_urls = ['https://www.airbnb.com.co/s/Tunja--Boyac%C3%A1--Colombia/homes']
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.airbnb.com.co/',
}
    def parse(self, response):
        # Obtener enlaces a las páginas de detalle
        detalle_links = response.xpath('//*[@id="listings-content"]/a/@href').getall()
        print(detalle_links)
        for link in detalle_links:
            # Crear una solicitud para seguir el enlace a la página de detalle
            yield scrapy.Request(url=response.urljoin(link), callback=self.parse_detalle)


        # Manejar paginación
        next_page = response.xpath('//*[@id="listingListFooter"]/div[2]/ul/li[6]/a/@href').get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)

    def parse_detalle(self, response):
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

class OptiviviendaSpiderItem7(scrapy.Spider):
    name = 'fincaraiz_spider_venta'
    allowed_domains = ['fincaraiz.com.co']
    start_urls = ['https://fincaraiz.com.co/finca-raiz/venta/tunja/boyaca?pagina=1']
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://fincaraiz.com.co/',
}
    def parse(self, response):
         
        # Obtener enlaces a las páginas de detalle
        detalle_links = response.xpath('//*[@id="listingContainer"]/div/a/@href').getall()
        print(detalle_links)
        for link in detalle_links:
            # Crear una solicitud para seguir el enlace a la página de detalle
            yield scrapy.Request(url=response.urljoin(link), headers= self.headers, callback=self.parse_detalle)


        current_page = int(response.url.split('=')[-1])
        next_page_url = f'https://fincaraiz.com.co/finca-raiz/venta/tunja/boyaca?pagina={current_page + 1}'
        
        yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_detalle(self, response):
        # Extraer datos de la página de detalle
        metrocuadrado_item = OptiviviendaScraperItem()
        metrocuadrado_item['titulo'] = response.xpath('//*[@id="__next"]/div[2]/main/section/div[2]/header/div/div[1]/p').get()
        metrocuadrado_item['precio'] = response.xpath('//*[@id="__next"]/div[2]/main/section/div[4]/div/aside/div/div[1]/div[1]/div/div/p[2]').get()
        metrocuadrado_item['ubicacion'] = response.xpath('//*[@id="__next"]/div[2]/main/section/div[2]/header/div/div[2]/div[1]/p[2]').get()
        metrocuadrado_item['descripcion'] =  response.xpath('//*[@id="general"]/div/div[1]/div/div/div/p[1]').get()
        metrocuadrado_item['tipo_inmueble'] = response.xpath('//*[@id="__next"]/div[2]/main/section/div[2]/header/div/div[1]/p').get()
        metrocuadrado_item['tipo_operacion'] = response.xpath('//*[@id="__next"]/div[2]/main/section/div[2]/header/div/div[1]/p').get()
        metrocuadrado_item['estrato'] = response.xpath('//*[@id="general"]/div/div[2]/div[1]/div[6]/div[2]/p[2]').get()
        metrocuadrado_item['numero_habitaciones'] = response.xpath('//*[@id="general"]/div/div[2]/div[1]/div[1]/div[2]/p[2]').get()
        metrocuadrado_item['numero_baños'] = response.xpath('//*[@id="general"]/div/div[2]/div[1]/div[2]/div[2]/p[2]').get()
        metrocuadrado_item['area'] = response.xpath('//*[@id="general"]/div/div[2]/div[1]/div[5]/div[2]/p[2]').get()
        metrocuadrado_item['caracteristicas'] = response.xpath('//*[@id="characteristics"]/div[2]/div/div[1]/p').getall()

        yield metrocuadrado_item



class OptiviviendaSpiderItem8(scrapy.Spider):
    name = 'metrocuadrado_spider_venta'
    allowed_domains = ['metrocuadrado.com']
    start_urls = ['https://www.metrocuadrado.com/apartamento-casa-oficina-local-bodega-lote-finca-consultorio/venta/tunja/?search=form']
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://metrocuadrado.com/',
}
    def parse(self, response):
         
        # Obtener enlaces a las páginas de detalle
        detalle_links = response.xpath('//*[@id="__next"]/div/div/div[3]/div[2]/div[2]/div[2]/ul[1]/li[1]/div/ul/li[2]/div/a/@href').getall()
        print(detalle_links)
        for link in detalle_links:
            # Crear una solicitud para seguir el enlace a la página de detalle
            yield scrapy.Request(url=response.urljoin(link), headers= self.headers, callback=self.parse_detalle)


         # Manejar paginación
        next_page = response.xpath('//*[@id="__next"]/div/div/div[3]/div[2]/div[2]/div[2]/ul[2]/li[8]/a/@href').get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)
        

    def parse_detalle(self, response):
        # Extraer datos de la página de detalle
        metrocuadrado_item = OptiviviendaScraperItem()
        metrocuadrado_item['titulo'] = response.xpath('//*[@id="__next"]/div/div/div/div[2]/div[3]/div[1]/div/h1').get()
        metrocuadrado_item['precio'] = response.xpath('//*[@id="__next"]/div/div/div/div[2]/div[3]/div[2]/div/div[2]/div/div[1]/h3').get()
        metrocuadrado_item['ubicacion'] = response.xpath('//*[@id="__next"]/div/div/div/div[2]/div[4]/div[1]/div[8]/div/div[2]/p').get()
        metrocuadrado_item['descripcion'] =  response.xpath('//*[@id="__next"]/div/div/div/div[2]/div[4]/div[1]/div[6]/p').get()
        metrocuadrado_item['tipo_inmueble'] = response.xpath('//*[@id="__next"]/div/div/div/div[2]/div[3]/div[1]/div/h1').get()
        metrocuadrado_item['tipo_operacion'] = response.xpath('//*[@id="__next"]/div/div/div/div[2]/div[3]/div[1]/div/h1').get()
        metrocuadrado_item['estrato'] = response.xpath('//*[@id="general"]/div/div[2]/div[1]/div[6]/div[2]/p[2]').get()
        metrocuadrado_item['numero_habitaciones'] = response.xpath('//*[@id="__next"]/div/div/div/div[2]/div[4]/div[1]/div[4]/div[2]/div/div/ul/li[2]/div/h2').get()
        metrocuadrado_item['numero_baños'] = response.xpath('//*[@id="__next"]/div/div/div/div[2]/div[4]/div[1]/div[4]/div[2]/div/div/ul/li[3]/div/h2').get()
        metrocuadrado_item['area'] = response.xpath('//*[@id="__next"]/div/div/div/div[2]/div[4]/div[1]/div[8]/div/div[6]/p').get()
        metrocuadrado_item['caracteristicas'] = response.xpath('//*[@id="__next"]/div/div/div/div[2]/div[4]/div[1]/div[11]/div/div/div[2]/div/div/div[1]/ul/li[2]').getall()

        yield metrocuadrado_item




class OptiviviendaSpiderItem10(scrapy.Spider):
    name = 'ciencuadras_spider_arriendo'
    allowed_domains = ['www.ciencuadras.com']
    start_urls = ['https://www.ciencuadras.com/arriendo/tunja']
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.ciencuadras.com/',
}
    def parse(self, response):
         
        # Obtener enlaces a las páginas de detalle
        detalle_links = response.xpath('/html/body/ciencuadras-root/main/div[1]/ciencuadras-result-entry/main/ciencuadras-container-load/div/ciencuadras-container-middle/section/div[1]/section/ciencuadras-list-cards/div/a/@href').getall()
        print(detalle_links)
        for link in detalle_links:
            # Crear una solicitud para seguir el enlace a la página de detalle
            yield scrapy.Request(url=response.urljoin(link), headers= self.headers, callback=self.parse_detalle)


         # Manejar paginación
        next_page = response.xpath('/html/body/ciencuadras-root/main/div[1]/ciencuadras-result-entry/main/ciencuadras-container-load/div/ciencuadras-container-middle/section/div[1]/section/div[3]/ciencuadras-paginator/div/ul/li[2]/@href').get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)
        

    def parse_detalle(self, response):
        # Extraer datos de la página de detalle
        metrocuadrado_item = OptiviviendaScraperItem()
        metrocuadrado_item['titulo'] = response.xpath('/html/body/ciencuadras-root/main/div[1]/ciencuadras-detail-entry/div/ciencuadras-container-top/div[1]/div[1]/ciencuadras-breadcrum/div/div[7]/p').get()
        metrocuadrado_item['precio'] = response.xpath('/html/body/ciencuadras-root/main/div[1]/ciencuadras-detail-entry/div/ciencuadras-container-top/div[1]/div[3]/div/ciencuadras-contact-sales-tabs/div/div[1]/ciencuadras-contact/div/div[1]/div[1]/div[1]/div/p').get()
        metrocuadrado_item['descripcion'] =  response.xpath('/html/body/ciencuadras-root/main/div[1]/ciencuadras-detail-entry/div/div[1]/ciencuadras-container-middle/div/div/div[2]/ciencuadras-detail-information/div/ciencuadras-expansion-panel[1]/mat-expansion-panel/div/div/div/p').get()
        metrocuadrado_item['tipo_inmueble'] = response.xpath('//*[@id="datos"]/div/div[1]/div[2]/div[1]/h1').get()
        metrocuadrado_item['tipo_operacion'] = "arriendo"
        metrocuadrado_item['estrato'] = response.xpath('//*[@id="datos"]/div/div[1]/div[6]/div/div[1]/span[2]/strong').get()
        metrocuadrado_item['numero_habitaciones'] = response.xpath('//*[@id="datos"]/div/div[1]/div[5]/div[2]/div[2]/div[1]/p[2]').get()
        metrocuadrado_item['numero_baños'] = response.xpath('//*[@id="datos"]/div/div[1]/div[5]/div[2]/div[2]/div[2]/p[2]').get()
        metrocuadrado_item['area'] = response.xpath('//*[@id="datos"]/div/div[1]/div[5]/div[1]/div[2]/span[2]').get()
        metrocuadrado_item['caracteristicas'] = response.xpath('//*[@id="datos"]/div/h2').getall()

        yield metrocuadrado_item
