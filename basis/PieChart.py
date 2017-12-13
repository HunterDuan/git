#饼图
import matplotlib.pyplot as plt
labels = ['Computer Science', 'Foreign Languages', 'Analytical Chemistry',
'Education', 'Humanities', 'Physics', 'Biolopy', 'Math and Statistics',
'Engineering']
sizes = [21, 4, 7, 7, 8, 9, 10, 15, 19]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 
'red', 'purple', '#f280de', 'orange', 'green']
explode = (0, 0, 0, 0, 0, 0, 0, 0, 0.2) # 让饼图中的某一块凸出来
plt.pie(sizes, explode = explode, labels = labels, 
	autopct = '%1.1f%%', colors = colors)
plt.axis('equal')
plt.show()

#散点图
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import	seaborn as sns
sutdents = pd.read_csv('ucdavis.csv') 
g = sns.FacetGrid(sutdents, palette = 'Set1', size = 7)
g.map(plt.scatter, 'momheight','height', s = 140, linewidth = .7, 
	edgecolor = '#ffad40', color = '#ff8000')
g.set_axis_labels('Mothers Height', 'Sutdents Height')
plt.show()

#气泡图
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
sns.set(style = 'whitegrid')
mov = pd.read_csv('ucdavis.csv')
x = mov.dadheight
y = mov.exercise
z = mov.exercise

cm = plt.cm.get_cmap('RdYlBu')
fig , ax = plt.subplots(figsize = (12, 10))

sc = ax.scatter(x, y, s = 3*z, c =z, cmap = cm, linewidth = 0.2, alpha = 0.5)
ax.grid()
fig.colorbar(sc)

ax.set_xlabel('ProductionCost', fontsize = 14)
ax.set_ylabel('Gross Profits', fontsize = 14)
plt.show()
