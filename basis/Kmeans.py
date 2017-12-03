from numpy import *
def loadDataset(filename):
	datamat = []
	fr = open(filename)
	for line in fr.readlines():
		sline = line.strip().split('\t')
		fline = map(float, sline)
		datamat.append(fline)
	return datamat

def Dist_Eclud(vec_1, vec_2):
	return sqrt(sum(power(vec_1 - vec_2, 2)))

def rand_Mid(dataset, k):
	n = shape(dataset)[1]
	midpoints = mat(zeros((k, n)))
	for j in range(n):
		minJ = min(dataset[:, j])
		rangeJ = float(max(dataset[:, j]) - minJ)
		midpoints[:, j] = minJ + rangeJ *random.rand(k , 1)
	return midpoints

def Kmeans(dataset, k):
	m = shape(dataset)[0]
	cluster = mat(zeros((m , 2)))
	midpoints = rand_Mid(dataset , k)
	cluster_change = True
	while cluster_change:
		cluster_change = False
		for i in range(m):
			min_dist = inf;
			min_index = -1
			for j in range(k):
				distJI = Dist_Eclud(midpoints[j,:],dataset[i,:])
				if distJI < min_dist:
					min_dist = distJI;
					min_index = j
			if cluster[i,0] != min_index: cluster_change = True
			cluster[i,:] = min_index,min_dist**2
		print midpoints
		for mid in range(k):
			Update_cluster = dataset[nonzero(cluster[:,0].A == mid)[0]]
			midpoints[mid,:] = mean(Update_cluster, axis = 0)
	return midpoints, cluster
