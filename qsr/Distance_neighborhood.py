def calculate_neighborhood_distance(data1, data2):
	RCC_neigh = {'dc': {'dc': 0, 'ec': 1, 'po': 2, 'tpp': 3, 'ntpp': 4, 'eq': 3, 'tppi': 3, 'ntppi': 4},
	             'ec': {'ec': 0, 'dc': 1, 'po': 1, 'tpp': 2, 'ntpp': 3, 'eq': 2, 'tppi': 2, 'ntppi': 3},
	             'po': {'po': 0, 'dc': 2, 'ec': 1, 'tpp': 1, 'ntpp': 2, 'eq': 1, 'tppi': 1, 'ntppi': 2},
	             'tpp': {'tpp': 0, 'dc': 3, 'ec': 2, 'po': 1, 'ntpp': 1, 'eq': 1, 'tppi': 2, 'ntppi': 2},
	             'ntpp': {'ntpp': 0, 'dc': 4, 'ec': 3, 'po': 2, 'tpp': 1, 'eq': 1, 'tppi': 2, 'ntppi': 2},
	             'eq': {'eq': 0, 'dc': 3, 'ec': 2, 'po': 1, 'tpp': 1, 'ntpp': 1, 'tppi': 1, 'ntppi': 1},
	             'tppi': {'tppi': 0, 'dc': 3, 'ec': 2, 'po': 1, 'tpp': 2, 'ntpp': 2, 'eq': 1, 'ntppi': 1},
	             'ntppi': {'ntppi': 0, 'dc': 4, 'ec': 3, 'po': 2, 'tpp': 2, 'ntpp': 2, 'eq': 1, 'tppi': 1}}
		
	Direct_neigh = {'n': {'n': 0, 'ne': 1, 'e': 2, 'se': 3, 's': 4, 'sw': 3, 'w': 2, 'nw': 1},
					'ne': {'n': 1, 'ne': 0, 'e': 1, 'se': 2, 's': 3, 'sw': 4, 'w': 3, 'nw':2 },
					'e': {'n': 2, 'ne': 1, 'e': 0, 'se': 1, 's': 2, 'sw': 3, 'w': 4, 'nw': 3},
					'se': {'n': 3, 'ne': 2, 'e': 1, 'se': 0, 's': 1, 'sw': 2, 'w': 3, 'nw': 4},
					's': {'n': 4, 'ne': 3, 'e': 2, 'se': 1, 's': 0, 'sw': 1, 'w': 2, 'nw': 3},
					'sw': {'n': 3, 'ne': 4, 'e': 3, 'se': 2, 's': 1, 'sw': 0, 'w': 1, 'nw': 2},
					'w': {'n': 2, 'ne': 3, 'e': 4, 'se': 3, 's': 2, 'sw': 1, 'w': 0, 'nw': 1},
					'nw': {'n': 1, 'ne': 2, 'e': 3, 'se': 4, 's': 3, 'sw': 2, 'w': 1, 'nw': 0}}
	
	QDC_neigh = {"0": {"0": 0, "1": 1, "2": 2}, "1": {"0": 1, "1": 0, "2": 1}, "2": {"0": 2, "1": 1, "2": 0}}

	Exist_neigh = {'0_0': {'0_0': 0, '0_1': 1, '1_1': 2, '1_0': 1},
					'0_1': {'0_0': 1, '0_1': 0, '1_1': 1, '1_0': 2},
					'1_1': {'0_0': 2, '0_1': 1, '1_1': 0, '1_0': 1},
					'1_0': {'0_0': 1, '0_1': 2, '1_1': 1, '1_0': 0}}
	
	QTC_neigh = {"['0', '+']": {"['0', '+']": 0, "['-', '0']": 2, "['0', '0']": 1, "['+', '-']": 3, "['-', '-']": 3, "['0', '-']": 2, "['+', '+']": 1, "['+', '0']": 2, "['-', '+']": 1},
				"['-', '0']": {"['0', '+']": 2, "['-', '0']": 0, "['0', '0']": 1, "['+', '-']": 3, "['-', '-']": 1, "['0', '-']": 2, "['+', '+']": 3, "['+', '0']": 2, "['-', '+']": 1},
				"['0', '0']": {"['0', '+']": 1, "['-', '0']": 1, "['0', '0']": 0, "['+', '-']": 2, "['-', '-']": 2, "['0', '-']": 1, "['+', '+']": 2, "['+', '0']": 1, "['-', '+']": 2},
				"['+', '-']": {"['0', '+']": 3, "['-', '0']": 3, "['0', '0']": 2, "['+', '-']": 0, "['-', '-']": 2, "['0', '-']": 1, "['+', '+']": 2, "['+', '0']": 1, "['-', '+']": 4},
				"['-', '-']": {"['0', '+']": 3, "['-', '0']": 1, "['0', '0']": 2, "['+', '-']": 2, "['-', '-']": 0, "['0', '-']": 1, "['+', '+']": 4, "['+', '0']": 3, "['-', '+']": 2},
				"['0', '-']": {"['0', '+']": 2, "['-', '0']": 2, "['0', '0']": 1, "['+', '-']": 1, "['-', '-']": 1, "['0', '-']": 0, "['+', '+']": 3, "['+', '0']": 2, "['-', '+']": 3},
				"['+', '+']": {"['0', '+']": 1, "['-', '0']": 3, "['0', '0']": 2, "['+', '-']": 2, "['-', '-']": 4, "['0', '-']": 3, "['+', '+']": 0, "['+', '0']": 1, "['-', '+']": 2},
				"['+', '0']": {"['0', '+']": 2, "['-', '0']": 2, "['0', '0']": 1, "['+', '-']": 1, "['-', '-']": 3, "['0', '-']": 2, "['+', '+']": 1, "['+', '0']": 0, "['-', '+']": 3},
				"['-', '+']": {"['0', '+']": 1, "['-', '0']": 1, "['0', '0']": 2, "['+', '-']": 4, "['-', '-']": 2, "['0', '-']": 3, "['+', '+']": 2, "['+', '0']": 3, "['-', '+']": 0}}
	mapping_dict = {0: RCC_neigh, 1: Direct_neigh, 2: QDC_neigh, 3: Exist_neigh, 4: QTC_neigh}
	mapping_maxnum = {0: 8, 1: 8, 2: 4, 3: 4, 4: 8}
	overall_distance = 0
	for i in range(len(data1)-1):
		list1 = data1[i].split("*")
		list2 = data2[i].split("*")
		dist1 = mapping_dict[i][list1[0]][list2[0]]/mapping_maxnum[i]
		dist2 = mapping_dict[i][list1[1]][list2[1]]/mapping_maxnum[i]

		overall_distance += dist1
		overall_distance += dist2
	return overall_distance