# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OptiviviendaScraperItem(scrapy.Item):
    # define the fields for your item here like:
    titulo = scrapy.Field()
    precio = scrapy.Field()
    ubicacion = scrapy.Field()
    descripcion = scrapy.Field()
    tipo_inmueble = scrapy.Field()
    tipo_operacion = scrapy.Field()
    estrato = scrapy.Field()
    numero_habitaciones = scrapy.Field()
    numero_baños = scrapy.Field()
    area = scrapy.Field()
    caracteristicas = scrapy.Field()

    pass
