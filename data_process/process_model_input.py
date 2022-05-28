import os
vina_file = '/mnt/processed_data/vina_score_refineset.txt'
feature_file = '/mnt/processed_data/feature_total.txt'
feature_order_file = '/mnt/processed_data/success_protein.txt'
ground_truth_file = '/mnt/processed_data/refined-set/index/INDEX_refined_data.2019'

ground_truth = {}
vina_score = {}
feature={}
vina_pair=[]
ground_truth_list = []
with open(vina_file,'r') as fi:
    vina_pair =  [l[:-1] for l in fi if l.strip()]

with open(ground_truth_file,'r') as fi:
    ground_truth_list =  [l[:-1] for l in fi if l.strip()]
    
for vinapair in vina_pair:
    vinapair = vinapair.split(' ')
    vina_score[str(vinapair[0])] = float(vinapair[1])

for groundtruthpair in ground_truth_list:
    groundtruthpair = groundtruthpair.split('  ')
    ground_truth[str(groundtruthpair[0])] = float(groundtruthpair[3])


success_protein = []
with open(feature_order_file,'r') as fi:
    success_protein =  [l[:-1] for l in fi if l.strip()]
feature_list = []
with open(feature_file,'r') as fi:
    feature_list =  [l[:-1] for l in fi if l.strip()]
for i in range(len(success_protein)):
    feature[str(success_protein[i])] = str(feature_list[i])

output_file = '/mnt/processed_data/model_feaure_output.txt'
with open(output_file,'w') as fo:
    for protein in vina_score.keys():
        delta = float(ground_truth[protein])- float(vina_score[protein])
        fo.write(protein+','+feature[protein]+','+str(delta)+'\n')
