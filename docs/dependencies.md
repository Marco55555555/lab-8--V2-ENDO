# Dependencias del Pipeline

Este documento describe las dependencias lógicas entre las distintas etapas del pipeline de datos.  
Cada fase depende de la ejecución exitosa de las anteriores para garantizar coherencia, calidad de datos y trazabilidad en todo el flujo.

## Dependencias entre Etapas

| Etapa | Depende de | Descripción de la Dependencia |
|--------|-------------|--------------------------------|
| **Validación** | — | Requiere un esquema versionado (por ejemplo, `data/schemas/`) para comparar estructura, tipos y columnas esperadas. |
| **Transformación** | Validación exitosa | Solo se ejecuta si los datos pasaron validación. Depende de los archivos limpios generados en `data/processed/`. |
| **Enriquecimiento** | Transformación exitosa | Necesita datos transformados y el catálogo de referencia actualizado (`data/reference/catalogo_productos.csv`). |
| **Carga (Data Warehouse)** | Enriquecimiento exitoso | Solo se realiza si el enriquecimiento fue exitoso. Requiere conexión activa al Data Warehouse o almacenamiento de destino. |
| **Reportes** | Carga completada | Depende de los datos ya cargados o consolidados; genera salidas en `data/outputs/`. |
| **Monitoreo y Logging** | Todas las etapas | Supervisa y registra logs de cada componente, gestionando alertas en caso de error. |

## Justificación de las Dependencias

El pipeline fue diseñado bajo un principio de dependencia secuencial controlada, donde cada módulo garantiza que el siguiente reciba información válida y estructurada:

1. **Validación → Transformación:** evita procesar datos corruptos o con columnas inconsistentes.  
2. **Transformación → Enriquecimiento:** los datos deben estar estandarizados antes de añadir información externa.  
3. **Enriquecimiento → Carga:** solo se cargan datos completos y coherentes.  
4. **Carga → Reportes:** asegura que los reportes se generen con datos finales.  
5. **Monitoreo (global):** registra métricas, tiempos y errores en cada ejecución.

## Dependencias Técnicas (de Archivos y Módulos)

| Tipo | Archivo / Módulo | Depende de | Descripción |
|------|------------------|-------------|--------------|
| Configuración | `config/pipeline_config.yaml` | — | Define rutas y módulos a ejecutar. |
| Validación | `src/data_validation.py` | `data/raw/*.csv` | Usa los archivos crudos para revisar estructura y nulos. |
| Procesamiento | `src/data_processing.py` | `data/processed/` | Depende de la salida limpia de la validación. |
| Enriquecimiento | `src/data_enrichment.py` | `data/reference/*.csv` | Requiere catálogos o fuentes externas actualizadas. |
| Calidad | `src/quality_checks.py` | `data/enriched/` | Evalúa duplicados y métricas tras el enriquecimiento. |
| Orquestación | `src/orchestrator.py` | Todos los anteriores | Coordina ejecución, logs y control de errores. |


## Visualización del Flujo de Dependencias

graph TD
    A[Validación] --> B[Transformación]
    B --> C[Enriquecimiento]
    C --> D[Carga / Data Warehouse]
    D --> E[Reportes]
    A --> F[Monitoreo]
    B --> F
    C --> F
    D --> F
    E --> F

    classDef etapa fill:#4F8EF7,stroke:#333,stroke-width:1px,color:#fff;
    classDef control fill:#F39C12,stroke:#333,stroke-width:1px,color:#fff;
    class A,B,C,D,E etapa;
    class F control;
