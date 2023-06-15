# Demographic Data Analyzer

This project focuses on analyzing demographic data using the powerful data manipulation and analysis library, Pandas. The dataset used for this analysis is extracted from the 1994 Census database. By leveraging Pandas, we can answer several insightful questions about the dataset.

## Dataset Overview

The dataset consists of demographic information for various individuals. It includes features such as age, workclass, education, marital status, occupation, race, sex, capital gain, capital loss, hours per week, native country, and salary. Here is a sample of the dataset:

|    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
|---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
|  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | <=50K    |
|  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | <=50K    |
|  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | <=50K    |

## Questions to Answer

To gain valuable insights from the dataset, we will answer the following questions:

1. How many people of each race are represented in this dataset? This will be a Pandas Series with race names as the index labels.
2. What is the average age of men?
3. What is the percentage of people who have a Bachelor's degree?
4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
5. What percentage of people without advanced education make more than 50K?
6. What is the minimum number of hours a person works per week?
7. What percentage of people who work the minimum number of hours per week have a salary of more than 50K?
8. Which country has the highest percentage of people who earn more than 50K, and what is that percentage?
9. Identify the most popular occupation for those who earn more than 50K in India.

## File Structure

The project files are organized as follows:

- `demographic_data_analyzer.py`: The main Python script containing the code for demographic data analysis.
- `adult.data.csv`: The CSV file containing the dataset used for analysis.
- `test_module.py`: The unit test file that ensures the correctness of the implemented functions.

## Running the Unit Tests

To validate the accuracy of the implemented code, unit tests are provided in the `main.py` file. 

The unit tests will be executed, and the test results will be displayed, indicating whether each test has passed or failed.

## Conclusion

The demographic data analysis project provides a deeper understanding of the dataset by using Pandas to answer various questions related to demographics. By running the code and reviewing the results, you will gain insights into the dataset's characteristics and demographics-related patterns.

Note: Ensure that you have Pandas installed on your system before running the code or the unit tests. 
