import matplotlib.pyplot as plt

# União de dois gráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Gráfico de Linha
ax1.plot([1, 2, 3, 4], [1, 4, 2, 3], marker='o', linestyle='-', color='blue')
ax1.set_title('Line Chart')
ax1.set_xlabel('Eixo X')
ax1.set_ylabel('Eixo Y')
ax1.grid(False)


# Gráfico de Barras
ax2.bar(['A', 'B', 'C'], [10, 20, 15], color='purple')
ax2.set_title('Bar Chart')
ax2.set_xlabel('Categorias')
ax2.set_ylabel('Valores')


plt.tight_layout() # ajusta o espaçamento
plt.show()


