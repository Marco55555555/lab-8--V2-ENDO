import yaml
import json
import logging
from datetime import datetime
from src.data_validation import DataValidator
from src.data_processing import DataProcessor
from src.data_enrichment import DataEnricher
from src.quality_checks import QualityChecker
import os  # <- agregar para crear carpetas

class PipelineOrchestrator:
    def __init__(self, config_path='config/pipeline_config.yaml'):
        self.config = self.load_config(config_path)
        self.setup_logging()

    def load_config(self, config_path):
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)

    def setup_logging(self):
        # Crear carpeta logs si no existe
        os.makedirs("logs", exist_ok=True)

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('logs/pipeline_execution.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def execute_pipeline(self):
        """Ejecuta el pipeline completo con manejo de dependencias"""
        execution_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.logger.info(f"Iniciando ejecución del pipeline: {execution_id}")

        try:
            # Validación
            self.logger.info("Ejecutando validación de datos...")
            validator = DataValidator(self.config['validation'])
            validation_result = validator.validate()

            if not validation_result['success']:
                raise Exception(f"Validación fallida: {validation_result['errors']}")

            # Procesamiento
            self.logger.info("Ejecutando procesamiento de datos...")
            processor = DataProcessor(self.config['processing'])
            processing_result = processor.process()

            # Enriquecimiento
            self.logger.info("Ejecutando enriquecimiento de datos...")
            enricher = DataEnricher(self.config['enrichment'])
            enrichment_result = enricher.enrich(processing_result['processed_data'])

            # Control de calidad
            self.logger.info("Ejecutando validación de calidad...")
            quality_checker = QualityChecker(self.config['quality'])
            quality_result = quality_checker.check_quality(enrichment_result['enriched_data'])

            if not quality_result['passed']:
                raise Exception(f"Validación de calidad fallida: {quality_result['issues']}")

            # Reportes
            self.logger.info("Generando reportes...")
            self.generate_reports(enrichment_result['enriched_data'], execution_id)

            self.logger.info(f"Pipeline completado exitosamente: {execution_id}")
            return {
                'success': True,
                'execution_id': execution_id,
                'records_processed': processing_result['record_count']
            }

        except Exception as e:
            self.logger.error(f"Error en el pipeline: {str(e)}")
            self.send_alert(f"Pipeline falló: {str(e)}")
            return {'success': False, 'error': str(e)}

    def generate_reports(self, data, execution_id):
        """Genera reportes de ejecución"""
        report = {
            'execution_id': execution_id,
            'timestamp': datetime.now().isoformat(),
            'records_processed': len(data),
            'pipeline_version': self.config['version']
        }

        os.makedirs("data/outputs", exist_ok=True)  # <- asegurar carpeta outputs
        with open(f'data/outputs/report_{execution_id}.json', 'w') as f:
            json.dump(report, f, indent=2)

    def send_alert(self, message):
        """Envía alertas (simulado)"""
        self.logger.info(f"ALERTA: {message}")

if __name__ == "__main__":
    orchestrator = PipelineOrchestrator('config/pipeline_config.yaml')
    orchestrator.execute_pipeline()
