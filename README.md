# Usecase-6-Project-3

This project is about Data Storytelling, an interactive streamlit story about an apartments dataset from the website https://sa.aqar.fm/

## Data Cleaning steps:

### 1.  Reliability

-   The dataset was scrapped from a website called Aqar in 2022.
-   Apartments: [https://sa.aqar.fm/شقق-للإيجار](https://sa.aqar.fm/%D8%B4%D9%82%D9%82-%D9%84%D9%84%D8%A5%D9%8A%D8%AC%D8%A7%D8%B1)
-   Licensed by: Real Estate General Authority

### 2.  Timeliness

-   The data is from the year 2022, due to the data being public and not downloadable from the source, we will continue using it.

### 3.  Consistency
 
-   The dataset has some inconsistencies in the 'UserName' column where some names were unclear.
-   A column named 'refresh' that had the same values as a column named 'last_update'.
-   Columns names followed a mix of naming styles.
-   Some column names meaning is vague like 'beds' when they meant bedrooms for example.
-   The 'area' column had values that were too little or illogically big, making no sense.

### 4.  Relevance

-   The dataset was relevant to the questions we asked.
-   Sample Appropriateness was good, our target was apartments and it covered that.
-   Variable Selections "after renaming":
    
|    |    |
|--|--|    
| user_id | id |
| price | bedrooms |
| living_rooms | bathroom |
| area | street_width |
| age | last_update |
| kitchen | air_conditioning |
| furnished | district |
| create_time | review |
| seller | verified |
| days_on_market | available_for_rent |
| longitude | latitude |
| Region | -

The remaining columns were dropped because they were unusable or irrelevant to our analysis.

### 5.  Uniqueness
    
-   No duplicates were found.
    
### 6.  Completeness

-   The dataset had about 5% of missing values, 9734 to be exact.
-   Dealing with columns affected with null:
                        
| Column | Missing | Filled with |
|--|--|--|
| content | - | Dropped for irrelevancy. |
| imgs | - | Dropped for irrelevancy. |
| area | Missing 175, Missing (%) 2.6%, | filled with zeros as there is no way to tell how much. |
| street_width | Missing 210, Missing (%) 3.1% | filled with zeros as there is no way to tell how much. |
| furnished | Missing 45, Missing (%) 0.7% | filled with zeros as the zeros of this column is 91% more than the value 1. |
| UserName | Missing 93, Missing (%) 1.4% | filled with 'unknown'. |
| iam_verified | Missing 146, Missing (%) 2.2% | filled with 0 as it represented unverified status. |
| livings | Missing 2, Missing (%) < 0.1% | filled with 0 as there is no way to tell. |
| kitchen | Missing 17, Missing (%) 0.3% | filled with 1 as the value 1 was dominant in the column by 86% |
| ac | Missing 17, Missing (%) 0.3% | filled with 1 as the value 1 was dominant in the column by 86%. |
| age | Missing 705, Missing (%) 10.4% | filled with the median of the column to preserve the distribution of the data. |

### 7.  Accuracy
Data types changed to a more logical approach:

| Column name | To type |
|--|--|
| Last_update  | datetime |
| create_time  | datetime |
| Kitchen | boolean |
| air_conditioning | boolean |
| furnished | boolean |
| verified | boolean |
| available_for_rent  | boolean |
| Living_rooms  | int |


## Team Members

- Abdulaziz Al Kathiri
- Raghad Al Malki
- Alaa Al Ahmadi
- Wadia 
- Salman Gassem
