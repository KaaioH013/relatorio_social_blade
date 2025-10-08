import random
import csv
# import requests  # <-- Esta linha ficará comentada por enquanto

# --- FUNÇÕES DE PROCESSAMENTO DE DADOS (NÃO MUDAM) ---

def filter_profiles_by_followers(profiles, max_followers):
    """Filtra perfis por número de seguidores."""
    return [p for p in profiles if p.get("followers", 0) < max_followers]

def sort_profiles_by_gain(profiles):
    """Ordena perfis por ganho de seguidores em 30 dias."""
    return sorted(profiles, key=lambda p: p.get("gain_30d", 0), reverse=True)

def export_to_csv(profiles, filename, limit):
    """Exporta os dados dos perfis para um arquivo CSV."""
    if not profiles:
        print("Aviso: Nenhum perfil para exportar.")
        return
        
    # Pega as chaves do primeiro dicionário para usar como cabeçalho
    fieldnames = profiles[0].keys()
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for profile in profiles[:limit]:
            writer.writerow(profile)

# --- FUNÇÕES DE OBTENÇÃO DE DADOS ---

def create_mock_api_data():
    """Esta função simula a resposta da API, gerando 150 perfis fictícios."""
    print("-> Usando dados simulados (mock)...")
    brazilian_usernames = [
        "carolinabarbosa", "rodrigo_silva", "ana_costa", "felipe_santos", 
        "mariana_oliveira", "lucas_pereira", "julia_fernandes", "thiago_lima",
        "isabela_martins", "gabriel_alves", "leticia_rodrigues", "bruno_carvalho"
    ]
    mock_profiles = []
    for i in range(150):
        mock_profiles.append({
            "rank": i + 1,
            "username": f"{random.choice(brazilian_usernames)}_{random.randint(1, 999)}",
            "display_name": f"{random.choice(['Ana', 'Bruno', 'Carlos'])} {random.choice(['Silva', 'Santos'])}",
            "id": f"instagram_user_{random.randint(100000, 999999)}",
            "followers": random.randint(50000, 800000),
            "gain_30d": random.randint(-5000, 50000)
        })
    return mock_profiles

def fetch_real_api_data(client_id, token):
    """
    (PREPARADO PARA O FUTURO) Busca os dados reais da API do Social Blade.
    
    ATENÇÃO: Esta função precisa da biblioteca 'requests'.
    Para usá-la no futuro:
    1. Descomente a linha 'import requests' no topo do arquivo
    2. Instale a biblioteca executando: pip install requests
    3. Mude USAR_API_REAL para True
    """
    print("-> Esta funcionalidade estará disponível quando você instalar a biblioteca 'requests'")
    print("   Para instalar: pip install requests")
    return None

# --- EXECUÇÃO PRINCIPAL DO SCRIPT ---

if __name__ == '__main__':
    print("=== Gerador de Relatório Instagram ===")
    
    # --- PONTO DE CONTROLE ---
    # Alterne para 'True' quando tiver suas credenciais da API E a biblioteca 'requests' instalada
    USAR_API_REAL = False 
    
    # Suas credenciais (preencha quando tiver)
    CLIENT_ID = "SEU_CLIENT_ID_AQUI"
    TOKEN = "SEU_TOKEN_AQUI"

    if USAR_API_REAL:
        # 1. Busca os dados reais (futuro)
        perfis_brutos = fetch_real_api_data(CLIENT_ID, TOKEN)
    else:
        # 1. Gera os dados simulados
        perfis_brutos = create_mock_api_data()

    # Se a obtenção de dados falhar, encerra o script
    if not perfis_brutos:
        print("\nFalha ao obter dados. Encerrando o script.")
    else:
        # 2. Filtra os perfis
        print("-> Filtrando perfis com menos de 500.000 seguidores...")
        perfis_filtrados = filter_profiles_by_followers(perfis_brutos, 500000)
        print(f"-> Perfis após filtro: {len(perfis_filtrados)}")
        
        # 3. Ordena os perfis
        print("-> Ordenando por maior ganho de seguidores...")
        perfis_ordenados = sort_profiles_by_gain(perfis_filtrados)
        
        # 4. Exporta para CSV
        print("-> Gerando arquivo CSV...")
        nome_do_arquivo = 'relatorio_instagram.csv'
        export_to_csv(perfis_ordenados, nome_do_arquivo, 100)
        
        print(f"\n✅ SUCESSO! Relatório salvo em '{nome_do_arquivo}'")
        
        # Mostra os top 5 como sempre
        print("\n--- Top 5 perfis com maior ganho ---")
        for i, profile in enumerate(perfis_ordenados[:5]):
            print(f"  {i+1}º lugar: {profile['username']} (Ganho: {profile['gain_30d']:,})")
