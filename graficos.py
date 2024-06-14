import matplotlib.pyplot as plt
import pandas as pd

ruta = '/content/recursos.csv'

df = pd.read_csv(ruta, sep='[-]', engine='python')

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))

ax1.plot(df['Tiempo'], df['CPU'], color='blue', linestyle='--')
ax2.plot(df['Tiempo'], df['MEM'], color='red', linestyle='-')

ax1.set_xlabel('Tiempo')
ax1.set_ylabel('CPU')
ax1.set_title('CPU vs Tiempo')

ax2.set_xlabel('Tiempo')
ax2.set_ylabel('MEM')
ax2.set_title('MEM vs Tiempo')

plt.show()