import pandas as pd # type: ignore

def save_csv(df: pd.DataFrame, path: str):
    """Salva o dataset limpo."""
    df.to_csv(path, index=False)
    print(f"💾 Dados salvos em: {path}")
