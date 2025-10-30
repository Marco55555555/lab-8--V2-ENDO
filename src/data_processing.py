class DataProcessor:
    def __init__(self, config):
        self.config = config

    def process(self):
        print("Procesamiento completado correctamente.")
        # Simular salida del procesamiento
        return {
            "processed_data": [1, 2, 3, 4, 5],
            "record_count": 5
        }
