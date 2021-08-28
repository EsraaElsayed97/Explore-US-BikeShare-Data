## **This project is the first project in Data Analysis Professional Nanodegree on Udacity**
 
 ## **Overview**
In this project, you will make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. 

In this project, you will use data provided by [Motivate](https://www.motivateco.com/), a bike-share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

The Datasets

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

Start Time (e.g., 2017-01-01 00:07:57)

End Time (e.g., 2017-01-01 00:20:53)

Trip Duration (in seconds - e.g., 776)

Start Station (e.g., Broadway & Barry Ave)

End Station (e.g., Sedgwick St & North Ave)

User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

Gender

Birth Year

![](Aspose.Words.4f987563-12af-48c1-ad5e-8379a6e4efbf.001.png)


The original files are much larger and messier, and you don't need to download them, but they can be accessed here if you'd like to see them ([Chicago](https://www.divvybikes.com/system-data), [New York City](https://www.citibikenyc.com/system-data), [Washington](https://www.capitalbikeshare.com/system-data)). These files had more columns and they differed in format in many cases. Some [data wrangling](https://en.wikipedia.org/wiki/Data_wrangling) has been performed to condense these files to the above core six columns to make your analysis and the evaluation of your Python skills more straightforward. In the Data Wrangling course that comes later in the Data Analyst Nanodegree program, students learn how to wrangle the dirtiest, messiest datasets, so don't worry, you won't miss out on learning this important skill!
## **Statistics Computed**
You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:

**#1 Popular times of travel** (i.e., occurs most often in the start time)

- most common month
- most common day of week
- most common hour of day

**#2 Popular stations and trip**

- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

**#3 Trip duration**

- total travel time
- average travel time

**#4 User info**

- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)

