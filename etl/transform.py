import pandas as pd # type: ignore

def remove_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Remove valores ausentes."""
    print("🧹 Removendo valores ausentes...")
    before = df.shape[0]
    df = df.dropna()
    after = df.shape[0]
    print(f"✔ Removidos {before - after} registros.")
    return df

def filter_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """Remove outliers de idade e renda."""
    print("📊 Filtrando outliers de idade e renda...")

    before = df.shape[0]

    df = df[(df["person_age"] >= 18) & (df["person_age"] <= 80)]
    df = df[df["person_income"] <= 500000]

    after = df.shape[0]

    print(f"✔ Removidos {before - after} registros com outliers.")
    return df

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Executa todas as transformações."""
    print("🔧 Iniciando transformações...")
    df = remove_missing(df)
    df = filter_outliers(df)
    print("✔ Transformação concluída!")
    return df
