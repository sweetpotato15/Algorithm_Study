def solution(data, ext, val_ext, sort_by):
    # ext : 어떤 정보를 기준으로 뽑아낼지, val_ext : 뽑아낼 정보의 기준값, sort_by:정보를 정렬할 기준이 되는 문자열 
    data_index = {'code':0,'date':1,'maximum':2,'remain':3}
    data = [x for x in data if x[data_index[ext]] < val_ext]
    data = sorted(data, key = lambda x :x[data_index[sort_by]])

    return data