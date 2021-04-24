 
from PyQt5.QtWidgets import QApplication, QLabel
# importing the required module 
import numpy as np   
import pandas as pd
import networkx as nx 
import sys
import matplotlib.pyplot as plt 
import array as arr


from PyQt5.QtWidgets import *
app = QApplication([])
app.setStyle('Breeze')
window = QWidget()
layout = QVBoxLayout()

window.setStyleSheet("width: 600px; background: #A1C7C4 ; ")
button = QPushButton('OK')
l1 = QLabel()
l1.setText("Select File:")
layout.addWidget(l1)
layout.addStretch()

b1 = QButtonGroup()
radiobutton1 = QRadioButton("Input10")
b1.addButton(radiobutton1)
radiobutton2 = QRadioButton("Input20")
b1.addButton(radiobutton2)
radiobutton3 = QRadioButton("Input30")
b1.addButton(radiobutton3)
radiobutton4 = QRadioButton("Input40")
b1.addButton(radiobutton4)
radiobutton5 = QRadioButton("Input50")
b1.addButton(radiobutton5)
radiobutton6 = QRadioButton("Input60")
b1.addButton(radiobutton6)
radiobutton7 = QRadioButton("Input70")
b1.addButton(radiobutton7)
radiobutton8 = QRadioButton("Input80")
b1.addButton(radiobutton8)
radiobutton9 = QRadioButton("Input90")
b1.addButton(radiobutton9)
radiobutton10 = QRadioButton("Input100")
b1.addButton(radiobutton10)
layout.addWidget(radiobutton1)
layout.addWidget(radiobutton2)
layout.addWidget(radiobutton3)
layout.addWidget(radiobutton4)
layout.addWidget(radiobutton5)
layout.addWidget(radiobutton6)
layout.addWidget(radiobutton7)
layout.addWidget(radiobutton8)
layout.addWidget(radiobutton9)
layout.addWidget(radiobutton10)
layout.addStretch()
layout.addStretch()


l3 = QLabel()
l3.setText("-----------------------------------------------------------------------------------------------")
layout.addWidget(l3)

l2 = QLabel()
l2.setText("Select Algorithm:")
layout.addWidget(l2)
layout.addStretch()
b2 = QButtonGroup()
algo1 = QRadioButton("Prims")
b2.addButton(algo1)
algo2 = QRadioButton("Kruskal")
b2.addButton(algo2)
algo3 = QRadioButton("Dijiksra")
b2.addButton(algo3)
algo4 = QRadioButton("Bellman Ford")
b2.addButton(algo4)
algo5 = QRadioButton("Floyd Warshall")
b2.addButton(algo5)
algo6 = QRadioButton("Clustering Coefficient")
b2.addButton(algo6)
layout.addWidget(algo1)
layout.addWidget(algo2)
layout.addWidget(algo3)
layout.addWidget(algo4)
layout.addWidget(algo5)
layout.addWidget(algo6)

button = QPushButton('Select')

 # utility function that returns the minimum egde weight node
def minDistance(dist, mstSet, V):
    min = sys.maxsize  # assigning largest numeric value to min
    min_index = 0
    for v in range(V):
        if mstSet[v] == False and dist[v] < min:
            min = dist[v]
            min_index = v
    return min_index


# defining the actions on the button show output
def on_button_clicked(b):
	alert = QMessageBox()
	if radiobutton1.isChecked()==True:
		file1="Input10.txt"
		alert.setText('1!')
	if radiobutton2.isChecked()==True:
		file1="Input20.txt"
		alert.setText('2!')
	if radiobutton3.isChecked()==True:
		file1="Input30.txt"
		alert.setText('3!')
	if radiobutton4.isChecked()==True:
		file1="Input40.txt"
		alert.setText('4!')
	if radiobutton5.isChecked()==True:
		file1="Input50.txt"
		alert.setText('5!')
	if radiobutton6.isChecked()==True:
		file1="Input60.txt"
		alert.setText('6!')
	if radiobutton7.isChecked()==True:
		file1="Input70.txt"
		alert.setText('7!')
	if radiobutton8.isChecked()==True:
		file1="Input80.txt"
		alert.setText('8!')
	if radiobutton9.isChecked()==True:
		file1="Input90.txt"
		alert.setText('9!')
	if radiobutton10.isChecked()==True:
		file1="Input100.txt"
		alert.setText('10!')
	alert.exec_()
	vertices=[]
	vertex=[]
	edges=[]
	b=[]
	G = nx.MultiDiGraph();
	f= open(file1,'r')
	print(f.readline())
	print(f.readline())

	num= int(f.readline())
	j=0
	print(f.readline())
	for j in range(0,num):
		
		vertices.append(f.readline().split())
		vertex.append(vertices[j][0])
	print(f.readline())
	for j in range(0,num):
		edges.append(f.readline().split())
		b.append(edges[j].pop(0))



	for i in range(0,num):	
		for j in range(0,num):
			# print(b[0])
			ij= j *4;
			ij2= ij + 2;
			if ij < len(edges[i]):
				a = edges[i][ij]
				cost = float(edges[i][ij2])
				if G.has_edge(b[i],a)  :
					prev_Cost = G.get_edge_data(b[i],a)
					if prev_Cost[0]['weight'] >cost:
						G.remove_edge(b[i],a)
						G.add_edge(b[i],a,weight= cost)
				else:
				 	G.add_edge(b[i],a,weight= cost)

	#displaying original graph
	pos = nx.spring_layout(G)
	nx.draw(G,with_labels=True,node_color='skyblue', node_size=220, width=1, edge_cmap=plt.cm.OrRd,arrowstyle='->',arrowsize=20,font_size=10,pos=nx.random_layout(G, seed=13)) 
	plt.show()
	if algo1.isChecked()==True:
		#prims
		print("Algo1");
		G=G.to_undirected()
		pos = nx.spring_layout(G)
		T=nx.MultiGraph()
		V = len(G.nodes())  # V denotes the number of vertices in G
		dist = []  # dist[i] will hold the minimum weight edge value of node i to be included in MST
		parent = [None] * V  # parent[i] will hold the vertex connected to i, in the MST edge
		mstSet = []  # mstSet[i] will hold true if vertex i is included in the MST
		for i in range(V):
			dist.append(sys.maxsize)
			mstSet.append(False)
		n=0
		dist.append(0)
		parent.append(-1) # starting vertex is itself the root, and hence has no paren
		for count in range(V - 1):
			# print(count)
			u = minDistance(dist, mstSet, V)
			# print(u)  # pick the minimum distance vertex from the set of vertices
			mstSet[u] = True
			for v in range(V):
				a=str(u)
				b=str(v)
				if G.has_edge(a, b):
					# print("I am Here")
					
					
					d='weight'
					c=G[a][b] 
					# print(c[0]['weight'])
					e=c[0]['weight']
					if mstSet[v] == False and e< dist[v]:
						dist[v] = e
						# print(dist[v])
						parent[v] = u
		for X in range(V):
			if parent[X] != -1:  # ignore the parent of the starting node
				if (str(parent[X]),str(X)) in G.edges():
					T.add_edge( parent[X], X, weight=dist[X]) 
		nx.draw(T,with_labels=True,node_color='skyblue', node_size=220, width=1, edge_cmap=plt.cm.OrRd,arrowstyle='->',arrowsize=20,font_size=10,pos=nx.random_layout(T, seed=20)) 
		alert_m="Cost is "+str(T.size(weight='weight')/10000000)
		alert.setText(alert_m)
		alert.exec_()
		plt.show()


	if algo2.isChecked()==True:
		#kruskal
		print("Algo1");
		G=G.to_undirected()
		T= (nx.minimum_spanning_tree(G))
		print(sorted(T.edges(data=True)))
		pos = nx.spring_layout(T)
		alert_m="Cost is "+str(T.size(weight='weight')/10000000)
		alert.setText(alert_m)
		alert.exec_()
		nx.draw(T,with_labels=True,node_color='skyblue', node_size=220, width=1, edge_cmap=plt.cm.OrRd,
        arrowstyle='->',arrowsize=20,
        font_size=10, font_weight="bold",
        pos=nx.random_layout(G, seed=13))
		plt.show()
	if algo3.isChecked()==True:
		#Dijiskra
		# print("Algo1");
		if nx.has_path(G,str('1'),str('5')):
			TCost = nx.dijkstra_path_length(G, '1', '5', 'weight')
		else:
			TCost = float('inf');
		alert_m="Cost of Directed to node 5 is " + str(TCost /10000000)
		G=G.to_undirected()
		if nx.has_path(G,str('1'),str('5')):
			TCost = nx.dijkstra_path_length(G, '1', '5', 'weight')
		else:
			TCost = float('inf');
		alert_m= alert_m + "\nCost of Undirected to node 5 is " + str(TCost /10000000)
		alert.setText(alert_m)
		alert.exec_()
		#...............................
	if algo4.isChecked()==True:
		#Bellman Ford
		# print("Algo1");
		# T=nx.bellman_ford_path(G,'1','5',weight='weight')
		alert_m="Cost of Directed: "
		if nx.has_path(G,str(1) , '5'):
			TCost= nx.bellman_ford_path_length(G,str(1),'5',weight='weight')
		else:
			TCost=float('inf');
		alert_m=alert_m + str(TCost/10000000) +"\n"
		G=G.to_undirected()
		alert_m=alert_m +"Cost of Undirected: "
		if nx.has_path(G,str(1) , '5'):
			TCost= nx.bellman_ford_path_length(G,str(1),'5',weight='weight')
		else:
			TCost=0
		alert_m=alert_m + str(TCost/10000000) +"\n"
		alert.setText(alert_m)
		alert.exec_()
		
	if algo5.isChecked()==True:
		#Floyd Warshal
		# print("Algo1");
		path_lengths=nx.floyd_warshall(G)
		alert_m=""
		Cost_t=0;
		for i in range(1,num):
			for j in range(1,num):
				if path_lengths[str(i)][str(j)] != float('inf'):
					Cost_t = Cost_t + path_lengths[str(i)][str(j)]

		TCost=path_lengths['1']['5']
		alert_m="Cost is : "+str(Cost_t/10000000)+ "+" + str(TCost/10000000) 
		alert.setText(alert_m)
		alert.exec_()
	if algo6.isChecked()==True:
		#Clustering Coefficient
		print("Algo1");
		G=G.to_undirected()
		G=nx.Graph(G)
		coef=nx.average_clustering(G)
		alert_m="Coefficient is " + str(coef)
		alert.setText(alert_m)
		alert.exec_()

	f.close()
	pos = nx.spring_layout(G)
	

button.clicked.connect(on_button_clicked)
# button.linkHovered.connect(hovered)

layout.addStretch()
layout.addWidget(button)
window.setLayout(layout)
window.show()
app.exec_()






