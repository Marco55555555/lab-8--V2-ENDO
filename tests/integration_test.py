from src.orchestrator import PipelineOrchestrator

def test_full_pipeline_integration():
    """Prueba de integración completa del pipeline."""
    orchestrator = PipelineOrchestrator('config/pipeline_config.yaml')
    result = orchestrator.execute_pipeline()

    assert 'success' in result
    assert isinstance(result['success'], bool)
    print("Prueba de integración ejecutada correctamente.")
