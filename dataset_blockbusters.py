import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1.carregar os dados
df = pd.read_csv("movie_blockbusters.csv")
print("dimensões do dataset:", df.shape)
print(df.head())

# 2. Análise exploratoria e metricas de negocio
print("\n--- Estatísticas Gerais ---")
print(df[['budget_usd', 'revenue_usd', 'roi', 'profit_usd']].describe())

#Taxa geral de blockbusters
blockbuster_rate = df['blockbuster'].mean() * 100
print(f"\nTaxa Geral de Blockbusters: {blockbuster_rate:.2f}%")

#Taxa de blockbusters por gênero
genre_success = df.groupby('genre')['blockbuster'].mean().reset_index()
genre_success['blockbuster_rate_%'] = genre_success['blockbuster'] * 100
genre_success = genre_success.sort_values(by='blockbuster_rate_%', ascending=False)
print("\nTaxa de Sucesso por Gênero (%):")
print(genre_success)

#3. Geração de Graficos Profissionais

#Configuração visual padrão
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

#Grafico 1: Taxa de blockbusters por gênero
plt.figure(figsize=(10, 6))
sns.barplot(
    data=genre_success,
    x='blockbuster_rate_%',
    y='genre',
    color='#1f77b4'
)
plt.title('Blockbuster Success Rate by Movie Genre(1980-2024)', fontsize=14, fontweight='bold')
plt.xlabel('Blockbuster Rate (%)', fontsize=12)
plt.ylabel('Genre', fontsize=12)
plt.tight_layout()
plt.savefig('blockbuster_rate_by_genre.png', dpi=300)
plt.show()

#grafico 2: Relação entre orçamento e receita (log scale)
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x='budget_usd',
    y='revenue_usd',
    hue='blockbuster',
    palette={0: '#d9d9d9', 1: '#ff7f0e'},
    alpha=0.7,
    s=50
)
plt.title('Budget vs. Revenue (Blockbuster Analysis)', fontsize=14, fontweight='bold')
plt.xlabel('Production Budget (USD - Log Scale)', fontsize=12)
plt.ylabel('Box Office Revenue (USD - Log Scale)', fontsize=12)

plt.xscale('log')
plt.yscale('log')

handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles=handles, labels=['No (0)', 'Yes (1)'], title='Is Blockbuster?')

plt.tight_layout()
plt.savefig('budget_vs_revenue.png', dpi=300)
plt.show()


#Exportar base tratada
df.to_csv("movie_blockbusters_cleaned.csv", index=False)
print("\nAnálise concluída com sucesso e gráficos salvos!")