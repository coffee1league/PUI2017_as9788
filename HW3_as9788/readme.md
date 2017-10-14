
This is a summary for Homework 3 comprising 3 assignments.

Update: In addition to the original idea of trying to see how the Winter citibike ride trips compared to the Summer citibike ride trips, I submitted a second ipython notebook exploring the idea of ratio of number of "subscribers" (long term cutomers) versus "customers" (short term customers) during the week vs the weekend. The two data sets that were used were were from January 2016 and July 2016. A z test was conducted on both counts and ratios. 




The first assignment was about following a skelleton notebook prepared for the assignment and reproducing probability distributions and mean plots for four additional distributions. I followed the steps in the notebook and looked up the documentation for the random dstribution functions for the different types on SciPy. Then I compared the distributions with my homework partner for this assignment. One of the graphs that seemed off in my notebook was the binomial distribution as the means looked like a straight increasing slope line rather than a somewhat bell shaped curve. 

The Citibike project assignment was worked on in a group with Assel (AD4336).

My contribution so far was in brainstorming various different hypothesis to test;  loading the data ; prepping the data in a data frame, and dropping relevant columns. 

The next steps are to count the total number of riders in each of the data sets for July 2016 and January 2016 and perform a statistical test to determine if July 2016 had greater than or equeal to the number of riders as the January 206 data set. 

The idea behind this analysis was that theree would be greater number of riders during the warmer summer months than the cooler winter months. The Null Hypothesis for this test was the number of riders in July 2016 is greater than or equal to the number of riders in  January 2016. The alternative hypthoseis is that the number of riders in July 2016 is less than the number of riders in January 2016.The alpha level is .05.Because we are taking counts of each of the months we should use a poisson related test since the poisson distribution is used to meausre counts. 
