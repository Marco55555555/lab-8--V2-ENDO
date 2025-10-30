class QualityChecker:
    def __init__(self, config):
        self.config = config

    def check_quality(self, data):
        print("Control de calidad aprobado.")
        # Simular control de calidad exitoso
        return {"passed": True, "issues": []}
