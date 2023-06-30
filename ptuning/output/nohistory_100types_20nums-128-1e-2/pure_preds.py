import json
test_file = '/home/hanzhang/GLMTest/ptuning/data/test_100_20_1.json'
file = 'generated_predictions.txt'
preds = []
with open(test_file,'r') as f:
    test = json.load(f)
res = test

with open(file,'r') as f:
    lines = f.readlines()
    for line in lines:
        dic = json.loads(line)
        i = dic['labels'].index('人工客服')
        dic['labels'] = dic['labels'][i:]
        preds.append(dic)

for i,pred_dic in enumerate(preds):
    for key,value in pred_dic.items():
        if key != 'labels':
            res[i][key] = value

print('res_len:',len(res))
print('preds_len',len(preds))

#print(res)
with open('preds.json','w') as f:
    json.dump(res,f,indent=4,ensure_ascii=False)
