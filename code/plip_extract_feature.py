import os
success_prot = '/mnt/processed_data/success_protein.txt'
files = open(success_prot,'r')
wait_list =  [l[:-1] for l in files if l.strip()]
for item in wait_list[3538:]:
    os.system('cd /mnt/processed_data/pdb && plip -i '+str(item)+' -x')
    os.system('cd /mnt/processed_data/pdb && python3 parse_xml.py')
