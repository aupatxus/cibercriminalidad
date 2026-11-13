
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




## Hipótesis desarrolladas 

1. Evolución de la ciberdelincuencia por tipo de delito (por grupo penal)
2. CCAA con mayor número de ciberdelitos (hechos conocidos)
3. El top 10 de la tipología penal (por tipo de hecho)
4. Datos conocidos vs. Datos esclarecidos: Tasa de esclarecimiento por año, por grupo penal y por CCAA de infracciones penales relacionadas con cibercriminalidad. 
5. Victimizaciones: ¿Qué colectivos son los más (vulnerables) atacados por la ciberdelincuencia?) Víctimas por sexo, por grupo de edad y por tipología delictiva.


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


