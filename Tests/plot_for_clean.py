import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

python_codex_protein = pd.read_csv("Tests/python_cite_protein.csv", index_col=0, header=0)
python_codex_protein = python_codex_protein.apply(pd.to_numeric)

r_codex_protein = pd.read_csv("Tests/cite_protein_clean.csv", index_col=0, header=0)
r_codex_protein = r_codex_protein.apply(pd.to_numeric)

fig, ax = plt.subplots(figsize=(12, 12))  # Creates a larger figure

for i, column in enumerate(r_codex_protein.columns):
    if(column not in ["B220", "CD44", "CD11c"]):
        x = r_codex_protein[[column]]
        y = python_codex_protein[[column]]
        ax.scatter(x, y, label=column)

ax.set_xlabel("R")
ax.set_ylabel("Python")
ax.set_title("Scatter Plot with Proteins other than B220, CD44, and CD11c")

ax.legend()
plt.show()

