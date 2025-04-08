%matplotlib inline
import zipfile
import numpy as np
import pandas as pd
import seaborn as sns

#z = zipfile.ZipFile("../data/athlete_events.zip")
df = pd.read_csv("athlete_events.csv")
df = df.dropna(subset=['Medal', "Age", "Height", "Weight"])
df.head()
df.info()
#1. Сколько мужчин и женщин получили золотые, серебрянные и бронзовые медали?
df.groupby(['Sex'])['Medal'].value_counts()
#2. Какая страна получила наибольшее количество золотых медалей за всю историю олимпийских игр?
dff = df.groupby(['Team'])['Medal'].describe() #сохранияю общее кол-во медалей по странам в обдельную переменную для дальнейшего поиска максимума
dff[dff['count']==dff['count'].max()] #нахожу строчку с максимальным кол-вом медалей, получается Unites States
#3. Выведите распределение пола участника олимпиады от вида спорта (crosstab)
pd.crosstab(df['Sex'], df['Sport'], margins=True)
#4.Выведите средний возраст и его стандартное отклонения для женщин, учавствовавших в хоккее на льду
Table = df.pivot_table(['Age'], ['Sport', 'Sex'], aggfunc=[np.mean, np.std]) #Сохраняю нужные столбцы с в переменную, при этом сразу считаем средний возраст и его ст.отклонение
tb = Table.query('Sport == ["Ice Hockey"]') # отсортировываем датасет, оставляя только данные по хоккею на льду
tb.query('Sex == ["F"]') # отсортировываем, оставляя только женщин
#5. У какой страны больше всего было больше всего женщин, получивших бронзовую медаль?
women_bronze = df.groupby(['Medal', 'Sex'])['Team'].value_counts()
women_bronze = pd.DataFrame(women_bronze)
women_bronze # у United States больше всего женщин с бронзой (360)
#6. Постройте гистограмму распределения количества медалей (бронза, серебро, золото) для первых трех стран, получивших наибольшее количество медалей
medal_count = df.groupby(['Team', 'Medal']).size().reset_index(name='Count') #reset_index заменяет индекс датафрейма на обычный индекс, состоящий из целых чисел 1.
top_3_countries = medal_count.groupby('Team').sum()['Count'].sort_values(ascending=False)[:3] #первые страны по количеству медалей
filtered_df = medal_count[medal_count['Team'].isin(top_3_countries.index)] #топ стран по количеству медалей c распределением по номиналу
filtered_df.pivot(index='Team', columns='Medal', values='Count').plot(kind='bar')
#7. Нарисуйте распределение веса мужчин, получивших серебрянную медаль(density или distplot)
silver_men_df = df[(df['Sex'] == 'M') & (df['Medal'] == 'Silver')]
# Строим график плотности распределения веса
sns.kdeplot(data=silver_men_df['Weight'], shade=True, label='Мужчины с серебряной медалью') #Функция kdeplot из библиотеки Seaborn используется для построения графика плотности распределения вероятностей. Она показывает, насколько часто встречаются значения в определенном диапазоне, сглаживая исходные данные с помощью ядра плотности.
#8. Постройте boxplot для возраста участника в зависимости от медали
sns.set(style="whitegrid") #установка стиля графика
ax = sns.boxplot(x='Medal', y='Age', data=df) #на Х - медаль, на у - Возраст
#9. Постройте pairplot для веса, возраста и роста участников от USA.
dfUSA = df[df.Team == 'United States'] #новый датафрейм с фильтром из оригинального датафрейма по комнаде США
sns.pairplot(df[['Age', 'Weight', 'Height']]) #парный график по трем параметрам