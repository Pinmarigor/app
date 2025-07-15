import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.DataFrame({
    'idade': [13, 25, 18, 69, 102, 97, 10],
    'nome' : ['italo', 'jose', 'mourinho', 'carlos', 'ronaldo', 'atadolfo', 'mario']
})

plt.hist(tabela['idade'])