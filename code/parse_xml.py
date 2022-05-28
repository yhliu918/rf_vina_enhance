from xml.dom.minidom import parse
import xml.etree.ElementTree as ET


domTree = parse("./report.xml")

rootNode = domTree.documentElement
print(rootNode.nodeName)
interaction_names = {'hydrophobic_interaction':['dist'],'hydrogen_bond':['dist_h-a','dist_d-a'],'water_bridge':['dist_a-w','dist_d-w'],
'salt_bridge':['dist'],'pi_stack':['offset'],'pi_cation_interaction':['offset']}


total_feature_list = []
for kind in interaction_names.keys():
	# print(len(domTree.getElementsByTagName(str(kind))))
	features = interaction_names[str(kind)]
	for fea in features:
		avg_list = []
		# print('*'*10+str(kind)+'_'+str(fea)+'*'*10)
		total_feature_list.append(len(domTree.getElementsByTagName(str(kind))))
		for item in domTree.getElementsByTagName(str(kind)):
			tmpval = item.getElementsByTagName(str(fea))[0]
			avg_list.append(float(tmpval.childNodes[0].data))
		if len(avg_list):
			total_feature_list.append(sum(avg_list)/len(avg_list))
		else:
			total_feature_list.append(0)
header = ''
for item in interaction_names.keys():
	name = item
	for fea in interaction_names[item]:
		totalname = '#'+name+"_"+fea
		header+=totalname
		header+=','
	for fea in interaction_names[item]:
		totalname = 'avg_'+name+"_"+fea
		header+=totalname
		header+=','

output = ''
for item in total_feature_list:
	output+=str(item)
	output+=','

feature_file = 'feature.txt'
with open(feature_file,'a') as fo:
	# fo.write(header[:-1]+'\n')
	fo.write(output[:-1]+'\n')

	




