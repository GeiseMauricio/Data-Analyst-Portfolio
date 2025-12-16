import pandas as pd # type: ignore

# ------------------------------------- Carregando o dataset -------------------------------------

def extract_csv(path: str) -> pd.DataFrame:
    """Extrai dados de um arquivo CSV usando o caminho fornecido."""
    print(f"📥 Extraindo dados de: {path}")
    df = pd.read_csv(path)
    print(f"✔ Extração concluída. {df.shape[0]} linhas carregadas.")
    return df