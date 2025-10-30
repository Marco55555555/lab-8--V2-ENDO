import yaml
import sys
from pathlib import Path

CONFIG_PATH = Path("config/pipeline_config.yaml")

def main():
    if not CONFIG_PATH.exists():
        print(f"Archivo de configuración no encontrado: {CONFIG_PATH}")
        sys.exit(1)

    with open(CONFIG_PATH, "r") as f:
        config = yaml.safe_load(f)

    required_keys = ["version", "validation", "processing", "enrichment", "quality"]

    missing = [k for k in required_keys if k not in config]
    if missing:
        print(f"Faltan claves requeridas en la configuración: {missing}")
        sys.exit(1)

    print("Archivo de configuración válido.")

if __name__ == "__main__":
    main()
