import os

# feature input & vinascore & rfscore split into train and test due to core_set_protein.txt
vina_score = '/mnt/processed_data/vina_score_refineset.txt'
feature_file = '/mnt/processed_data/model_feaure_output.txt'
deltavinarf20_score = '/mnt/processed_data/deltavinarf20_score_refineset.txt'
core_set_file = '/mnt/processed_data/core_set_protein.txt'
refined_set_file = '/mnt/processed_data/success_protein.txt'

core_set = []
with open(core_set_file,'r') as fi:
    core_set = [l[:-1] for l in fi if l.strip()]

refined_set = []
with open(refined_set_file,'r') as fi:
    refined_set = [l[:-1] for l in fi if l.strip()]
refined_set = list(set(refined_set) - set(core_set))

vina_score_total = {}
with open(vina_score,'r') as fi:
    vina_list = [l[:-1] for l in fi if l.strip()]
    for vinapair in vina_list:
        vinapair = vinapair.split(' ')
        vina_score_total[vinapair[0]] = float(vinapair[1])

deltavinarf20_score_total={}
with open(deltavinarf20_score,'r') as fi:
    deltavinarf20_score_list = [l[:-1] for l in fi if l.strip()]
    for deltavinarf20pair in deltavinarf20_score_list:
        deltavinarf20pair = deltavinarf20pair.split(' ')
        deltavinarf20_score_total[deltavinarf20pair[0]] = float(deltavinarf20pair[1])

total_feature = {}
with open(feature_file,'r') as fi:
    total_feature_list= [l[:-1] for l in fi if l.strip()]
    for featurepair in total_feature_list:
        featurepair_ = featurepair.split(',')
        total_feature[featurepair_[0]] = featurepair

vina_score_test = '/mnt/processed_data/vina_score_test.txt'
vina_score_train = '/mnt/processed_data/vina_score_train.txt'

deltavinarf20_score_test = '/mnt/processed_data/deltavinarf20_score_test.txt'
deltavinarf20_score_train = '/mnt/processed_data/deltavinarf20_score_train.txt'

feature_test = '/mnt/processed_data/feature_test.txt'
feature_train = '/mnt/processed_data/feature_train.txt'

# with open(vina_score_test,'w') as fo:
#     for corepro in core_set:
#         fo.write(corepro+','+str(vina_score_total[corepro])+'\n')

with open(vina_score_train,'w') as fo:
    for refinepro in refined_set :
        if refinepro not in vina_score_total.keys():
            continue
        fo.write(refinepro+','+str(vina_score_total[refinepro])+'\n')
  

# with open(deltavinarf20_score_test,'w') as fo:
#     for corepro in core_set:
#         fo.write(corepro+','+str(deltavinarf20_score_total[corepro])+'\n')

with open(deltavinarf20_score_train,'w') as fo:
    for refinepro in refined_set:
        if refinepro not in deltavinarf20_score_total.keys():
            continue
        fo.write(refinepro+','+str(deltavinarf20_score_total[refinepro])+'\n')


# with open(feature_test,'w') as fo:
#     for corepro in core_set:
#         fo.write(total_feature[corepro]+'\n')

with open(feature_train,'w') as fo:
    for refinepro in refined_set:
        if refinepro not in total_feature.keys():
            continue
        fo.write(total_feature[refinepro]+'\n')