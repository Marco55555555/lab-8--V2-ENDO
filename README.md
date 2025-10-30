# Laboratorio Práctico — Pipeline de Datos Orquestado

Este repositorio implementa un pipeline de datos completo que incluye:
- Ingesta, validación, procesamiento y enriquecimiento.
- Control de calidad y generación de reportes.
- Integración continua (CI) y despliegue automatizado (CD).

---

##  Estructura del Proyecto

```text
laboratorio-pipeline/
│
├── config/
│   └── pipeline_config.yaml
│
├── data/
│   ├── raw/
│   │   └── (archivos fuente descargados o simulados)
│   ├── processed/
│   │   └── (archivos intermedios procesados)
│   ├── outputs/
│   │   └── (reportes generados por el pipeline)
│   └── reports/
│       └── (reportes de ejecución generados en CD)
│
├── docs/
│   ├── pipeline_diagram.md          ← Fase 1: diagrama del pipeline
│   ├── dependencies.md              ← Fase 1: justificación y dependencias
│   ├── scalability_diagram.md       ← Fase 5: diagrama de escalabilidad
│   ├── scalability_strategies.md    ← Fase 5: estrategias de escalamiento
│   ├── reflection_questions.md      ← Fase 5: reflexiones finales
│
├── logs/
│   └── pipeline_execution.log       ← Logs de ejecución local y CI/CD
│
├── scripts/
│   ├── download_sample_data.py      ← Simula descarga de datos (Fase 3/4)
│   └── generate_execution_report.py ← Crea reporte de ejecución (Fase 5)
│
├── src/
│   ├── __init__.py                  ← Indica que src es un paquete Python
│   ├── orchestrator.py              ← Orquestador principal (Fase 2)
│   ├── data_validation.py           ← Módulo de validación de datos
│   ├── data_processing.py           ← Módulo de procesamiento / transformación
│   ├── data_enrichment.py           ← Módulo de enriquecimiento
│   └── quality_checks.py            ← Control de calidad final
│
├── tests/
│   ├── test_orchestration.py        ← Pruebas unitarias con pytest (Fase 4)
│   └── integration_test.py          ← Prueba de integración general (Fase 4)
│
├── .github/
│   └── workflows/
│       ├── ci_orchestration.yml     ← Fase 4: CI (tests automáticos)
│       └── cd_orchestrated_pipeline.yml ← Fase 5: CD (ejecución en GitHub)
│
├── requirements.txt                 ← Dependencias del proyecto (PyYAML, pytest, pytest-mock)

