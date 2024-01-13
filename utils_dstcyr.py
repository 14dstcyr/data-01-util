#"""This module provides a reusable byline for Cellular Development Services"""

import math
import statistics

# Define variables of different tyeps
Company_name: str = "Cellular Development, Inc."
Count_active_projects: int = 9
Has_international_presence: bool = False
Average_client_satisfaction: float = 4.9
Services_offered: list = ["Consultation", "Cell Lines", "Protcol Development", "Aseptic Training"]
Satisfaction_scores: list = [4.8, 4.7, 4.9, 5.0, 4.8, 4.6, 4.8, 4.9, 4.7]

# Define formatted strings
Active_projects_string: str = f"Active projects: {Count_active_projects}"
International_presence_string: str = f"International presence: {Has_international_presence}"
Client_satisfaction_string: str = f"Average client satisfaction: {Average_client_satisfaction}"

#Calculate descriptive statistics
import statistics
smallest=min(Satisfaction_scores)
largest=max(Satisfaction_scores)
total=sum(Satisfaction_scores)
count=len(Satisfaction_scores)
mean=statistics.mean(Satisfaction_scores)
mode=statistics.mode(Satisfaction_scores)
median=statistics.median(Satisfaction_scores)
standard_deviation=statistics.stdev(Satisfaction_scores)

stats_string: str = f"""
Descriptive statistics for our satisfaction scores:
  Smallest:{smallest}
  Largest:{largest}
  Total:{total}
  Count:{count}
  Mean:{mean}
  Mode:{mode}
  Median:{median}
  Standard Deviation:{standard_deviation}
  """
  
#Define byline string
byline: str = f"""
{Company_name}
{Active_projects_string}
{International_presence_string}
{Client_satisfaction_string}
{Services_offered}
{stats_string}
"""

#Define main function
def main():
    '''Display all output'''
    print(Company_name)
    print(Active_projects_string)
    print(International_presence_string)
    print(Client_satisfaction_string)
    print(Services_offered)
    print(stats_string)
    
if __name__ == '__main__':
    main()
    
