
# Análisis de la evolución de los ciberdelitos y situación de la cibercriminalidad 

Datos y estadísticas disponibles de criminalidad
https://estadisticasdecriminalidad.ses.mir.es/publico/portalestadistico/

Series anuales sobre Criminalidad 
https://estadisticasdecriminalidad.ses.mir.es/publico/portalestadistico/datos.html?type=jaxi&title=Cibercriminalidad&path=/Datos5/

## Origen de los datos 
### PORTAL ESTADÍSTICO DE CRIMINALIDAD 

    * Series anuales. Cibercriminalidad. Comunidades y Ciudades Autónomas
        * Hechos conocidos de infracciones penales relacionadas con cibercriminalidad por grupo penal
        * Hechos conocidos de infracciones penales relacionadas con cibercriminalidad por tipo hecho
        * Hechos esclarecidos de infracciones penales relacionadas con cibercriminalidad por grupo penal
        * Hechos esclarecidos de infracciones penales relacionadas con cibercriminalidad por tipo hecho
        * Detenciones e investigados de infracciones penales relacionadas con cibercriminalidad desglosado por grupo penal
        * Detenciones e investigados de infracciones penales relacionadas con cibercriminalidad desglosado por tipo hecho
        * Detenciones e investigados de infracciones penales relacionadas con cibercriminalidad desglosado por nacionalidad
        * Victimizaciones de infracciones penales relacionadas con cibercriminalidad desglosado por grupo penal
        * Victimizaciones de infracciones penales relacionadas con cibercriminalidad desglosado por tipo hecho
        * Victimizaciones de infracciones penales relacionadas con cibercriminalidad desglosado por nacionalidad 
    
    * Series anuales. Cibercriminalidad. Provincias
        * Hechos conocidos de infracciones penales relacionadas con cibercriminalidad por grupo penal
        * Hechos conocidos de infracciones penales relacionadas con cibercriminalidad por tipo hecho
        * Hechos esclarecidos de infracciones penales relacionadas con cibercriminalidad por grupo penal
        * Hechos esclarecidos de infracciones penales relacionadas con cibercriminalidad por tipo hecho
        * Detenciones e investigados de infracciones penales relacionadas con cibercriminalidad desglosado por grupo penal
        * Detenciones e investigados de infracciones penales relacionadas con cibercriminalidad desglosado por tipo hecho
        * Detenciones e investigados de infracciones penales relacionadas con cibercriminalidad desglosado por nacionalidad
        * Victimizaciones de infracciones penales relacionadas con cibercriminalidad desglosado por grupo penal
        * Victimizaciones de infracciones penales relacionadas con cibercriminalidad desglosado por tipo hecho
        * Victimizaciones de infracciones penales relacionadas con cibercriminalidad desglosado por nacionalidad 2011-2020
        * Victimizaciones de infracciones penales relacionadas con cibercriminalidad desglosado por nacionalidad 2021-2025 


### Datos locales (archivos CSV descargados del PORTAL ESTADÍSTICO DE CRIMINALIDAD)
* 05001 (Comunidades) Hechos conocidos de infracciones penales relacionadas con cibercriminalidad por grupo penal.csv
* 05002 (Provincias) Hechos conocidos de infracciones penales relacionadas con cibercriminalidad por grupo penal.csv
* 05003 (Comunidades) Hechos conocidos de infracciones penales relacionadas con cibercriminalidad por tipo hecho.csv
* 05004 (Provincias) Hechos conocidos de infracciones penales relacionadas con cibercriminalidad por tipo hecho.csv
* 05005 (Comunidades) Hechos esclarecidos de infracciones penales relacionadas con cibercriminalidad por grupo penal.csv
* 05006 (Provincias) Hechos esclarecidos de infracciones penales relacionadas con cibercriminalidad por grupo penal.csv
* 05007 (Comunidades) Hechos esclarecidos de infracciones penales relacionadas con cibercriminalidad por tipo hecho.csv
* 05008 (Provincias) Hechos esclarecidos de infracciones penales relacionadas con cibercriminalidad por tipo hecho.csv
* 05009 (Comunidades) Detenciones e investigados de infracciones penales relacionadas con cibercriminalidad desglosado por grupo penal.csv
* 05010 (Provincias) Detenciones e investigados de infracciones penales relacionadas con cibercriminalidad desglosado por grupo penal.csv
* 05011 (Comunidades) Detenciones e investigados de infracciones penales relacionadas con cibercriminalidad desglosado por tipo hecho.csv
* 05012 (Provincias) Detenciones e investigados de infracciones penales relacionadas con cibercriminalidad desglosado por tipo hecho.csv
* 05013 (Comunidades) Detenciones e investigados de infracciones penales relacionadas con cibercriminalidad desglosado por nacionalidad.csv
* 05014 (Provincias) Detenciones e investigados de infracciones penales relacionadas con cibercriminalidad desglosado por nacionalidad.csv
* 05015 (Comunidades) Victimizaciones de infracciones penales relacionadas con cibercriminalidad desglosado por grupo penal.csv
* 05016 (Provincias) Victimizaciones de infracciones penales relacionadas con cibercriminalidad desglosado por grupo penal.csv
* 05017 (Comunidades) Victimizaciones de infracciones penales relacionadas con cibercriminalidad desglosado por tipo hecho.csv
* 05018 (Provincias) Victimizaciones de infracciones penales relacionadas con cibercriminalidad desglosado por tipo hecho.csv
* 05019 (Comunidades) Victimizaciones de infracciones penales relacionadas con cibercriminalidad desglosado por nacionalidad.csv
* 05020 (Provincias) Victimizaciones de infracciones penales relacionadas con cibercriminalidad desglosado por nacionalidad 2011-2020.csv
* 05022 (Provincias) Victimizaciones de infracciones penales relacionadas con cibercriminalidad desglosado por nacionalidad 2021-2025.csv




## Estructura del repositorio:

```
https://github.com/aupatxus/cibercriminalidad/
│
│
├── src/
│   ├── data/          datasets.csv
│   │
│   ├── notebooks/     estudios y pruebas.ipynb
│   │
│   ├── utils/         generando datasets propios y gráficos.ipynb
│   │
│   └── memoria.ipynb
│
└── README.md
```

## Limpieza y transformación de los datos de (origen) entrada

* `pandas`: importar, limpiar y transformar los datos.
* `numpy`: cálculos estadísticos.
* `matplotlib` y `seaborn`: visualizaciones.
* `plotly`: gráficos interactivos y mapas.



> La columna "Total" contiene datos numéricos con el formato de . para separar por miles, lo que genera un problema a la hora de importar los datos del csv ya que los interpreta como valores float en lugar de numéricos de tipo integer (int) o entero sin decimales. Para prevenir estos futuros errores procesando los datos totales se emplea el parámetro `thousands="."` para importar correctamente la columna de totales con el comando `pd.read_csv(../data/archivo.csv", sep=";", thousands=".")`


````
df = pd.read_csv("../data/archivo.csv", sep=";", thousands=".")
````


## Hipótesis en desarrollo y conclusiones previas

1. Evolución temporal de la ciberdelincuencia por tipo de delito (por grupo penal)
   * Los ciberdelitos conocidos pasaron de 37.412 en 2011 a 488.426 en 2025 (multiplicándose por más de 13).
   * El Fraude Informático acumula 2.794.739 casos en todo el periodo, representando la inmensa mayoría de la ciberdelincuencia en España.
     
2. Distribución por CCAA: Los lugares con mayor número de ciberdelitos (hechos conocidos)
   * Tres comunidades concentran casi la mitad de todos los hechos conocidos: Cataluña (535.646), Andalucía (513.138) y Comunidad de Madrid (507.804).

3. El top 10 de la tipología penal (por tipo de hecho)
   * Dentro de los fraudes, destacan las estafas con tarjetas de crédito/débito (1.177.949), otras estafas (1.060.872) y estafa bancaria (400.067).
     
4. Datos conocidos vs. Datos esclarecidos: Tasa de esclarecimiento por año, por grupo penal y por CCAA de infracciones penales relacionadas con cibercriminalidad. 
   * Mientras los casos conocidos se disparaban, la tasa nacional de esclarecimiento cayó del 36% en 2011 al 15% en 2025 (tocando suelo en el 13% en 2020 y 2023). Visualmente vemos cómo sube la barra de delitos mientras cae la línea naranja de casos resueltos.
   * Por tipo de delito, los Delitos Sexuales y contra la Propiedad Industrial/Intelectual tienen un 63% de esclarecimiento, seguidos de cerca por las Amenazas y Coacciones y los delitos Contra el Honor, ambos con un 57%, mientras que el Fraude Informático apenas  logra esclarecerse el 12%, y peor aún es el escenario en Interferencia en los datos y en el sistema (ataques informáticos, sabotajes), donde la resolución cae al 6%.
      * Podemos interpretar que los delitos contra las personas suelen dejar rastros directos en redes sociales o mensajería vinculados a entornos cercanos a la víctima, facilitando su investigación. En cambio, las estafas masivas y ciberataques operan mediante redes automatizadas, suplantación de identidad y servidores internacionales, lo que dificulta enormemente identificar al autor.
   * Hay un contraste territorial llamativo: Las regiones que concentran el mayor volumen absoluto de denuncias en España son las que presentan menores porcentajes de resolución. Mientras territorios con menor volumen como Melilla (32%), Extremadura (25%) o Castilla-La Mancha (24%) superan holgadamente la media nacional, grandes núcleos urbanos como Madrid (13%), Cataluña (8%) y País Vasco (2%) se sitúan a la cola.
      * (nota: en el caso de País Vasco y Cataluña debemos tener en cuenta que el reporte de (Ertzaintza y Mossos d'Esquadra) policías autonómicas se dió a partir de 2015, frente a los datos de FCSE (Policía Nacional y Guardia Civil) que disponemos desde 2011).
      * Podemos interpretar que en comunidades con una altísima densidad de denuncias digitales (como Madrid, con más de 500.000 hechos conocidos), el volumen masivo de estafas cotidianas satura la capacidad de investigación frente a regiones con menor carga de casos.
   
5. Victimizaciones: ¿Qué colectivos son los más (vulnerables) atacados por la ciberdelincuencia?) Víctimas por sexo, por grupo de edad y por tipología delictiva.





