from etl.extract import extract_csv
from etl.transform import transform
from etl.load import save_csv

RAW_PATH = "data/raw/credit_risk_dataset.csv"
OUTPUT_PATH = "data/processed/credit_risk_clean.csv"

def run_etl():
    print("🚀 Iniciando pipeline ETL de risco de crédito...\n")

    df = extract_csv(RAW_PATH)
    df = transform(df)
    save_csv(df, OUTPUT_PATH)

    print("\n🎉 Pipeline ETL concluída com sucesso!")

if __name__ == "__main__":
    run_etl()
