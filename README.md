# WebScraper


- **`scrapy.cfg`**: Archivo de configuración de Scrapy.
- **`items.py`**: Define las estructuras de datos para los elementos que se recopilarán durante el scraping.
- **`middlewares.py`**: Contiene posibles middlewares para personalizar el comportamiento del scraping (no se utiliza actualmente en el proyecto).
- **`pipelines.py`**: Define las pipelines para procesar los elementos recopilados (no se utiliza actualmente en el proyecto).
- **`settings.py`**: Archivo de configuración del proyecto.
- **`spiders/`**: Directorio que contiene los spiders para diferentes sitios web.

## Spiders Disponibles
- **`properati_venta_scraper`**: Spider para recopilar propiedades en venta del sitio Properati en Tunja, Boyacá.
- **`properati_arriendo_scraper`**: Spider para recopilar propiedades en alquiler del sitio Properati en Tunja, Boyacá.
- **`nuroa_venta_scraper`**: Spider para recopilar propiedades en venta del sitio Nuroa en Tunja, Boyacá.
- **`nuroa_arriendo_scraper`**: Spider para recopilar propiedades en alquiler del sitio Nuroa en Tunja, Boyacá.
- **`mitula_venta_scraper`**: Spider para recopilar propiedades en venta del sitio Mitula en Tunja, Boyacá.
- **`mitula_arriendo_scraper`**: Spider para recopilar propiedades en alquiler del sitio Mitula en Tunja, Boyacá.
- **`airbnb_scraper`**: Spider para recopilar propiedades en alquiler del sitio Airbnb en Tunja, Boyacá.

## Ejecución de los Spiders
Para ejecutar un spider específico, utiliza el siguiente comando:

scrapy crawl <nombre_del_spider>

Reemplaza `<nombre_del_spider>` con el nombre del spider que deseas ejecutar (por ejemplo, `properati_venta_scraper`). Los datos recopilados se mostrarán en la consola y se pueden redirigir a un archivo CSV o a una base de datos según sea necesario.
