## Diseño de Pipelines
Dividí el pipeline en componentes modulares (validación, procesamiento, enriquecimiento,
control de calidad y reportes) para mantener la trazabilidad y reutilización.
Cada módulo tiene dependencias claras y ejecuta una sola responsabilidad.

## Orquestación vs Ejecución
- **Orquestación:** coordina las etapas, gestiona dependencias y registra logs centralizados.  
- **Ejecución:** se limita a correr tareas individuales sin contexto global.  
Orquestar permite manejar errores, dependencias y automatizar flujos de extremo a extremo.

## Manejo de Fallos
- **Reintentos automáticos:** reejecutar etapas en caso de errores temporales.  
- **Continuación desde el punto de fallo:** guardar checkpoints para reanudar el proceso.  
- **Notificaciones escalonadas:** alertas por correo o Slack cuando una etapa crítica falla.

## Monitoreo
Monitorearía las siguientes métricas:
- Tiempo de ejecución por etapa  
- Cantidad de registros procesados  
- Porcentaje de errores  
- Recursos de cómputo consumidos  

Estas métricas ayudan a detectar cuellos de botella y planificar escalado.

## Costos
Estrategias para optimizar costos:
- Uso de recursos **on-demand** o **serverless**  
- Compresión y archivado de datos antiguos  
- Escalado automático según carga  
- Cierre programado de entornos inactivos

**Conclusión:**  
La orquestación no solo permite automatizar el flujo de datos,
sino también escalarlo y monitorearlo de manera controlada,
manteniendo la calidad y reduciendo costos operativos.
