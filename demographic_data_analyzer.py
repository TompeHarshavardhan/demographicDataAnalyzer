import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult_data.csv')
    print(df)
    #  How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    dic=dict()
    for k in df['race']:
        dic[k]=dic.get(k,0) + 1
    # print(dic)
    race_count = None
    race_count=pd.Series(dic.values())
    race_count.index=dic.keys()
    race_count

    # What is the average age of men?
    average_age_men = None
    average_age_men=round(df[df['sex']=='Male']['age'].mean(),1)


    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = None
    percentage_bachelors=round(len(df[df['education']=='Bachelors'])/len(df)*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    higher_education=round((len(df[(df['education-num']==13)|(df['education-num']==14)|(df['education-num']==16)])/len(df))*100,1)
    lower_education = None
    lower_education=100-higher_education

    # percentage with salary >50K
    higher_education_rich = None
    higher_education_rich=round((len(df[((df['education-num']==13)|(df['education-num']==14)|(df['education-num']==16))&(df['salary']=='>50K')])/len(df[(df['education-num']==13)|(df['education-num']==14)|(df['education-num']==16)]))*100,1)
    lower_education_rich = None
    lower_education_rich=round((len(df[((df['education-num']!=13)&(df['education-num']!=14)&(df['education-num']!=16))&(df['salary']=='>50K')])/len(df[((df['education-num']!=13)&(df['education-num']!=14)&(df['education-num']!=16))]))*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = None
    min_work_hours=df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None
    num_min_workers=df[df['hours-per-week']==df['hours-per-week'].min()]

    rich_percentage = None
    rich_percentage=(len((df[(df['hours-per-week']== df['hours-per-week'].min())&(df['salary']=='>50K')]))/len(df[df['hours-per-week']== df['hours-per-week'].min()]))*100

    # What country has the highest percentage of people that earn >50K?
    dic=dict()
    for k in df[df['salary']=='>50K']['native-country']:
       dic[k]=dic.get(k,0) + 1
    rickhCount=pd.Series(dic.values())
    rickhCount.index=dic.keys()
    dic=dict()
    for k in df['native-country']:
       dic[k]=dic.get(k,0) + 1
    normCount=pd.Series(dic.values())
    normCount.index=dic.keys()
    s=rickhCount/normCount
    highest_earning_country = None
    highest_earning_country= s.index[s==s.max()]
    highest_earning_country_percentage = round(s.max()*100,1)
    
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None
    dic=dict()
    for k in df[(df['native-country']=='India') & (df['salary']=='>50K')]['occupation']:
       dic[k]=dic.get(k,0) + 1
    scem=pd.Series(dic.values())
    scem.index=dic.keys()
    top_IN_occupation =scem.index[scem==scem.max()]
    

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
      print("Number of each race:\n", race_count)
      print("Average age of men:", average_age_men)
      print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
      print(
        f"Percentage with higher education that earn >50K: {higher_education_rich}%"
      )
      print(
        f"Percentage without higher education that earn >50K: {lower_education_rich}%"
      )
      print(f"Min work time: {min_work_hours} hours/week")
      print(
        f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
      )
      print("Country with highest percentage of rich:", highest_earning_country)
      print(
        f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
      )
      print("Top occupations in India:", top_IN_occupation)

    return {
      'race_count': race_count,
      'average_age_men': average_age_men,
      'percentage_bachelors': percentage_bachelors,
      'higher_education_rich': higher_education_rich,
      'lower_education_rich': lower_education_rich,
      'min_work_hours': min_work_hours,
      'rich_percentage': rich_percentage,
      'highest_earning_country': highest_earning_country,
      'highest_earning_country_percentage': highest_earning_country_percentage,
      'top_IN_occupation': top_IN_occupation
    }
