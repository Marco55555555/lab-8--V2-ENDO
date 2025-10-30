
# Estrategias de Escalabilidad
La escalabilidad garantiza que el pipeline mantenga su desempeño
a medida que crecen los volúmenes de datos o las demandas de procesamiento.

## Nivel 1: Procesamiento Local
- **Volumen:** < 1 GB  
- **Herramientas:** Python, Pandas, archivos CSV.  
- **Ejecución:** Local o en GitHub Actions.  
- **Ventajas:** Bajo costo, simplicidad, rápida iteración.  
- **Limitaciones:** No soporta grandes volúmenes ni concurrencia.

## Nivel 2: Procesamiento en la Nube
- **Volumen:** 1 GB – 10 GB  
- **Herramientas:** Azure Functions, Azure Batch, AWS Lambda, GCP Cloud Run.  
- **Ventajas:** Escalado automático, integración con CI/CD, disponibilidad 24/7.  
- **Limitaciones:** Costos variables y latencia de red.

## Nivel 3: Procesamiento Distribuido
- **Volumen:** > 10 GB  
- **Herramientas:** Apache Spark, Azure Databricks, Azure Synapse, Google Dataproc.  
- **Ventajas:** Procesamiento paralelo, alta tolerancia a fallos, escalabilidad horizontal.  
- **Limitaciones:** Requiere configuración avanzada, costos de infraestructura mayores.

##  Nivel 4: Monitoreo y Optimización
- **Herramientas:** Azure Monitor, Prometheus, Grafana, CloudWatch.  
- **Métricas clave:**  
  - Tiempos de ejecución por etapa  
  - Volumen procesado  
  - Tasa de errores  
  - Consumo de CPU y memoria  
- **Estrategias:**  
  - Alertas automáticas y dashboards interactivos  
  - Reintentos controlados  
  - Escalado adaptativo según carga
