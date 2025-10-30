class DataEnricher:
    def __init__(self, config):
        self.config = config

    def enrich(self, data):
        print("Enriquecimiento completado correctamente.")
        # Simular enriquecimiento de datos
        enriched = [{"valor": d, "enriched": True} for d in data]
        return {"enriched_data": enriched}
