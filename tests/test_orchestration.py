import pytest
from unittest.mock import patch
from src.orchestrator import PipelineOrchestrator

class TestPipelineOrchestration:

    def test_pipeline_initialization(self):
        """Test que el orquestador se inicializa correctamente"""
        orchestrator = PipelineOrchestrator('config/pipeline_config.yaml')
        assert orchestrator.config is not None
        assert 'version' in orchestrator.config

    def test_execution_flow_success(self):
        """Test de flujo exitoso"""
        with patch('src.data_validation.DataValidator') as mock_validator, \
             patch('src.data_processing.DataProcessor') as mock_processor, \
             patch('src.data_enrichment.DataEnricher') as mock_enricher, \
             patch('src.quality_checks.QualityChecker') as mock_quality:

            mock_validator.return_value.validate.return_value = {'success': True}
            mock_processor.return_value.process.return_value = {
                'processed_data': [1, 2, 3],
                'record_count': 3
            }
            mock_enricher.return_value.enrich.return_value = {'enriched_data': [1, 2, 3]}
            mock_quality.return_value.check_quality.return_value = {'passed': True, 'issues': []}

            orchestrator = PipelineOrchestrator('config/pipeline_config.yaml')
            result = orchestrator.execute_pipeline()

            assert result['success'] == True
            assert 'execution_id' in result

    def test_execution_flow_failure(self):
        """Test de fallo en validación"""
        with patch('src.data_validation.DataValidator') as mock_validator:
            mock_validator.return_value.validate.return_value = {
                'success': False,
                'errors': ['Schema validation failed']
            }
            orchestrator = PipelineOrchestrator('config/pipeline_config.yaml')
            result = orchestrator.execute_pipeline()
            assert result['success'] == False
            assert 'error' in result
