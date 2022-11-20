import pandas as pd

import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 8)  # количество столбцов которое пандас позволяет отображать в терминале

general = pd.read_csv('general.csv')
prenatal = pd.read_csv('prenatal.csv')
sports = pd.read_csv('sports.csv')
prenatal.columns = general.columns
sports.columns = general.columns

g_p_s = pd.concat([general, prenatal, sports], ignore_index=True)
g_p_s.drop(columns=['Unnamed: 0'], inplace=True)
general.drop(columns=['Unnamed: 0'], inplace=True)

g_p_s.dropna(how='all', inplace=True)

g_p_s.loc[(g_p_s.gender == 'female'), 'gender'] = 'f'
g_p_s.loc[(g_p_s.gender == 'woman'), 'gender'] = 'f'
g_p_s.loc[(g_p_s.gender == 'man'), 'gender'] = 'm'
g_p_s.loc[(g_p_s.gender == 'male'), 'gender'] = 'm'

g_p_s['gender'].fillna('f', inplace=True)
g_p_s['bmi'].fillna(0, inplace=True)
g_p_s['diagnosis'].fillna(0, inplace=True)
g_p_s['blood_test'].fillna(0, inplace=True)
g_p_s['ecg'].fillna(0, inplace=True)
g_p_s['ultrasound'].fillna(0, inplace=True)
g_p_s['xray'].fillna(0, inplace=True)
g_p_s['children'].fillna(0, inplace=True)
g_p_s['months'].fillna(0, inplace=True)
g_p_s['mri'].fillna(0, inplace=True)


# print(g_p_s.sample(n=20, random_state=30))
# print(g_p_s.diagnosis.value_counts())


stomach = g_p_s.diagnosis.value_counts()['stomach']
# print(g_p_s.loc[g_p_s['hospital'] == 'general'].loc[g_p_s['blood_test'] == 't'])

count_general_stomach = \
    pd.pivot_table(g_p_s.loc[g_p_s['hospital'] == 'general'], index='diagnosis', aggfunc='count').loc['stomach'][0]
count_sports_dislocation = \
    pd.pivot_table(g_p_s.loc[g_p_s['hospital'] == 'sports'], index='diagnosis', aggfunc='count').loc['dislocation'][0]

mean_age_general = pd.pivot_table(g_p_s, index='hospital', values='age', aggfunc='median', ).round(3).loc['general'][0]
mean_age_sports = pd.pivot_table(g_p_s, index='hospital', values='age', aggfunc='median', ).round(3).loc['sports'][0]

# temp_t = pd.pivot_table(g_p_s, index=['hospital', 'blood_test'], values='blood_test', aggfunc='count')
df = g_p_s[['hospital', 'blood_test']].value_counts()
# print(df, df.max(), df.idxmax()[0])

first_answer = g_p_s.hospital.value_counts().idxmax()
second_answer = round(g_p_s.loc[(g_p_s['hospital'] == 'general') & (g_p_s['diagnosis'] == 'stomach')].shape[0] /
                      g_p_s.loc[g_p_s['hospital'] == 'general'].shape[0], 3)

third_answer = round(g_p_s.loc[(g_p_s['hospital'] == 'sports') & (g_p_s['diagnosis'] == 'dislocation')].shape[0] /
                     g_p_s.loc[g_p_s['hospital'] == 'sports'].shape[0], 3)

fourth_answer = mean_age_general - mean_age_sports
fifth_answer_1 = df.idxmax()[0]
fifth_answer_2 = df.max()

# print('The answer to the 1st question is', first_answer)
# print('The answer to the 2nd question is', second_answer)
# print('The answer to the 3rd question is', third_answer)
# print('The answer to the 4th question is', fourth_answer)
# print('The answer to the 5th question is', fifth_answer_1 + ',', fifth_answer_2, 'blood tests')

plt.figure(1)
plt.hist(g_p_s['age'])
plt.show()


plt.figure(2)
plt.pie(g_p_s['diagnosis'].value_counts(), labels=g_p_s['diagnosis'].value_counts().index)
plt.show()

plt.figure(3)
plt.violinplot(g_p_s['height'])
plt.show()

print('The answer to the 1st question: 15-35')
print('The answer to the 2nd question: pregnancy')
# print("The answer to the 3rd question: It's because...")
