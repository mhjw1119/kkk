import os
import requests
import pprint
from dotenv import load_dotenv


APIkey = '02bf9475c1d5dedbfea1723a0982ad15'
URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={APIkey}&topFinGrpNo=020000&pageNo=1&financdCd=0010587'
data = requests.get(URL).json()
print(data.keys())

print(data['result'].keys())
####################################a완료

# pprint.pprint(data['result']['baseList'])

#####################################b완료

# for i in data['result'] :
#     print(i)
pprint.pprint(data['result']['optionList'])
def return_dict (info) :
    data_list = []
    data_dict = {}
    for x in range(len(info['result']['optionList'])) :
        for i in info['result']['optionList'][x] :
            print(i)
            if i == 'dcls_month' :
                pass
            elif i == 'fin_co_no' :
                data_list[x][data_dict['금융상품코드']] =  info['result']['optionList'][x][i]
            elif i == 'intr_rate' :
                data_dict['저축 금리'] =  info['result']['optionList'][x][i]
            elif i == 'save_trm' :
                data_dict['저축 기간'] =  info['result']['optionList'][x][i]
            elif i == 'intr_rate_type' :
                data_dict['저축 금리 유형'] =  info['result']['optionList'][x][i]
            elif i == 'intr_rate_type_nm' :
                data_dict['저축 금리 유형명'] =  info['result']['optionList'][x][i]
            elif i == 'intr_rate2' :
                data_dict['최고 우대금리'] =  info['result']['optionList'][x][i]
            data_list.append(data_dict)
    return  data_list
pprint.pprint(return_dict(data))
return_dict(data)
