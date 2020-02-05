import pandas as pd

df = pd.read_csv('data.csv')
df_ = df.drop(['Class'], axis = 1) 

print(df)

p = 3/8
n = 5/8

def Gini_s(p, n):
    return 1 - (p/ (p+n))**2 - (n/ (p+n))**2

#Calculating Gini(s) of entire data:
Gini_s_val = Gini_s(p, n)

def Gini_index(plist, nlist):
    result = 0
    for i in range(len(plist)):
        result += ((plist[i] + nlist[i])/ df.shape[0]) * Gini_s(plist[i], nlist[i])
        print(result)
    return result

def Gini_gain(Gini_i):
    return Gini_s_val - Gini_i

columns = df_.columns
Gi_list,GGain_list = [], []
for attribute in columns:
    set_ = set(df_[attribute])
    p_temp,n_temp = 0,0
    pi,ni,Gini_attr = [],[],[]
    for attr_val in set_:
        if (df[df[attribute] == attr_val].Class.value_counts(sort = False).shape == (2,)):
            p_temp = df[df[attribute] == attr_val].Class.value_counts(sort = False).loc['Yes']
            n_temp = df[df[attribute] == attr_val].Class.value_counts(sort = False).loc['No']
        elif(df[df[attribute] == attr_val].Class.value_counts(sort = False).index[0] == 'Yes'):
            p_temp = df[df[attribute] == attr_val].Class.value_counts(sort = False).loc['Yes']
            n_temp = 0
        else:
            p_temp = 0
            n_temp = df[df[attribute] == attr_val].Class.value_counts(sort = False).loc['No']
        pi.append(p_temp)
        ni.append(n_temp)
        Gini_attr_val = Gini_s(p_temp,n_temp)
        Gini_attr.append(Gini_attr_val)
#     print(Gini_attr)
    Gini_index_val = Gini_index(pi, ni)
    Gi_list.append(Gini_index_val)
    GGain_val = Gini_gain(Gini_index_val)
    GGain_list.append(GGain_val)

print("Gini Index of Attributes:",Gi_list, "\nGini Gain of Attributes:", GGain_list)    

print("The Root Of the Decision Tree Is:", df.columns[GGain_list.index(max(GGain_list))])

