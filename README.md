# 📊 Relatório Instagram - Social Blade API

Um script Python para gerar relatórios CSV dos perfis brasileiros do Instagram que mais ganharam seguidores nos últimos 30 dias, projetado para usar dados da API do Social Blade Business.

## 🎯 Objetivo

Extrair e analisar os **100 perfis brasileiros** que mais cresceram em seguidores no Instagram (últimos 30 dias), aplicando filtros específicos:
- ✅ Perfis localizados no Brasil
- ✅ Menos de 500.000 seguidores
- ✅ Ordenados por maior ganho de seguidores em 30 dias

## 🚀 Funcionalidades

- **Mock de Dados**: Funciona totalmente offline com dados simulados para desenvolvimento e testes.
- **Filtragem Inteligente**: Isola apenas os perfis com menos de 500.000 seguidores.
- **Ordenação Automática**: Classifica os perfis pelo maior ganho, colocando os mais relevantes no topo.
- **Exportação para CSV**: Gera um relatório limpo e organizado, pronto para análise em qualquer editor de planilhas.
- **Preparado para API Real**: A estrutura modular permite uma transição fácil para o uso de uma API real, bastando alterar uma única variável de controle.

## 🛠️ Como Usar

### 1. Clone o Repositório

git clone https://github.com/KaaioH013/relatorio_social_blade.git

cd relatorio_social_blade

### 2. Execute o Script

python gerador_relatorio.py

O script funciona sem dependências externas no modo de simulação.


### 3. Resultado
Após a execução, o arquivo `relatorio_instagram.csv` será criado na pasta do projeto com os 100 perfis que mais cresceram.

## 🔧 Configuração para API Real (Futuro)

Quando você tiver suas credenciais da API do Social Blade:

1.  **Instale a biblioteca `requests`**:
    ```
    pip install requests
    ```
2.  **Edite o arquivo `gerador_relatorio.py`**:
    ```
    # Descomente esta linha no topo do arquivo
    # import requests

    # Altere estas variáveis de controle
    USAR_API_REAL = True
    CLIENT_ID = "seu_client_id_aqui"
    TOKEN = "seu_token_aqui"
    ```

## 👨‍💻 Autor

Feito com ❤️ por **Caio H RSantana**

- GitHub: [KaaioH013](https://github.com/KaaioH013)
- LinkedIn: [Caio H R Santana](https://www.linkedin.com/in/caio-henrique-r-santana-3443a3189/)

---
⭐ **Gostou do projeto? Deixe uma estrela!**
