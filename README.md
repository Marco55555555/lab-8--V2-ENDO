#  Laboratorio Práctico — Pipeline de Datos Orquestado

Este laboratorio implementa un **pipeline de datos orquestado de extremo a extremo**, con integración continua (CI), despliegue automatizado (CD), control de calidad y documentación completa.

---

## Contenido del Proyecto

El repositorio contiene todos los componentes necesarios para la ejecución automatizada del pipeline:

-  **Código fuente completo** en `src/`
-  **Diagramas y documentación** en `docs/`
-  **Pruebas unitarias e integrales** en `tests/`
-  **Workflows CI/CD** configurados en `.github/workflows/`
-  **Reportes y logs de ejecución** en `data/` y `logs/`

---

##  Descripción General del Pipeline

El pipeline implementa las siguientes fases:

| Fase | Descripción | Archivo Principal |
|------|--------------|-------------------|
| 1 | Diseño y documentación del pipeline | `docs/pipeline_diagram.md` |
| 2 | Orquestación del flujo de datos | `src/orchestrator.py` |
| 3 | Procesamiento y validación de datos | `src/data_validation.py`, `src/data_processing.py` |
| 4 | Integración continua y pruebas | `.github/workflows/ci_orchestration.yml` |
| 5 | Despliegue automatizado (CD) y escalabilidad | `.github/workflows/cd_orchestrated_pipeline.yml`, `docs/scalability_strategies.md` |

---

##  Estructura del Repositorio

```text
laboratorio-pipeline/
│
├── config/
│   └── pipeline_config.yaml
│
├── data/
│   ├── raw/               ← Datos fuente simulados
│   ├── processed/         ← Datos intermedios
│   ├── outputs/           ← Resultados del pipeline
│   └── reports/           ← Reportes generados por CD
│
├── docs/
│   ├── pipeline_diagram.md          ← Fase 1: diagrama del pipeline
│   ├── dependencies.md              ← Fase 1: dependencias justificadas
│   ├── scalability_diagram.md       ← Fase 5: diagrama de escalabilidad
│   ├── scalability_strategies.md    ← Fase 5: estrategias de escalamiento
│   ├── reflection_questions.md      ← Fase 5: reflexiones finales
│   └── img/
│       └── pipeline_diagram.png
│
├── logs/
│   └── pipeline_execution.log       ← Registro de ejecuciones
│
├── scripts/
│   ├── download_sample_data.py      ← Simula descarga de datos
│   └── generate_execution_report.py ← Genera reporte final
│
├── src/
│   ├── __init__.py
│   ├── orchestrator.py
│   ├── data_validation.py
│   ├── data_processing.py
│   ├── data_enrichment.py
│   └── quality_checks.py
│
├── tests/
│   ├── test_orchestration.py        ← Pruebas unitarias (pytest)
│   └── integration_test.py          ← Pruebas de integración
│
├── .github/
│   └── workflows/
│       ├── ci_orchestration.yml     ← CI: pruebas automáticas
│       └── cd_orchestrated_pipeline.yml ← CD: ejecución programada
│
├── requirements.txt                 ← Dependencias del proyecto
└── README.md                        ← Este archivo

---
##  Pruebas

<p align="center">
  <img src="https://github.com/user-attachments/assets/e4b05953-71c2-4104-a71b-b9502b8593c8" alt="Diagrama del Pipeline" width="800"/>
</p>

