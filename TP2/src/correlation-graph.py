import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data = pd.read_csv("data/data.csv")


# CORRELATION GRAPH
corr = data.corr()

sb.set(rc = {'figure.figsize': (15,15) })
ax = sb.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sb.diverging_palette(20, 240, n=200),
    square=True,
    xticklabels=True,
    yticklabels=True,
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);
plt.show()


# É observável uma grande correlação entre os atributos 
# que descrevem o desempenho academico de um estudante ao longo do 1 e 2 semestre

# O nosso objetivo passará por criar modelos que consigam lidar com esta situação
# de forma a dar menor importancia à sua relação em vez de processar os dados ou eliminar colunas
# visto que na definição do trabalalho não existe uma concreta explicitação do significado de cada uma
# e que nem a escala de maior parte dos atributos é facilmente reconhecida.