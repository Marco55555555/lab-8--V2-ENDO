# Fase 1: Diagramación del Pipeline

Este documento presenta el diseño general del pipeline, desde la ingesta de datos hasta el monitoreo.

    A1[API Externa] --> B[Ingesta de Datos]
    A2[CSV Locales] --> B
    A3[Base de Datos] --> B
    B --> C[Validación]
    C --> D[Transformación]
    D --> E[Enriquecimiento]
    E --> F[Carga a Data Warehouse]
    F --> G[Generación de Reportes]
    G --> H[Monitoreo y Logging]

    class A1,A2,A3 fuente;
    class B,C,D,E proceso;
    class F,G destino;
    class H control;
