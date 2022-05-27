import pandas as pd
 
teste = input("Escreva algo: ")
teste2 = pd.Series(list(sorted(teste))).value_counts()

print(teste2[:3])