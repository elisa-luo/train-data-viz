# train-data-viz
Training data visualization & analysis through Python. A fun little tool for me to easily see and interpret the training I'm doing during quarantine, to make it less boring. Generates some fun stats to keep me motivated. #CircumnavigateTheGlobe
    - used the pandas library. https://pandas.pydata.org/docs/index.html
    - author: Elisa Luo eyl2130@columbia.edu. Columbia University Division I Women's Rowing. Yeah Lions!

Input:
    - a .csv file with 4 columns: date, mode (bike, erg, run, lift), time_elapsed, and distance in KM. (metric, because we're not savages here. But perhaps will add a conversion option)

Features:
    - automated calculation of adjusted distance, based on the following conversion factors:
        - erg x1
        - bike x0.5
        - run x1.25
    - currently generates the following charts:
        - stacked bar graph, by date and time elapsed per mode
        - stacked bar graph, by date and distance per mode
        - stacked bar graph, by date and adjusted distance per mode
        - pie graph, by mode and time elapsed
        - pie graph, by mode and distance
        - pie graph, by mode and adjusted distance
    - currently calcuates the following stats:
        - total time spent training in minutes, hours, and days
        - period of time the data spans (in days)
        - total distance travelled (in KM)
        - percentage of the way around the earth travelled
        - average amount of minutes spent training per day

Sample text output (with my real training data):
    You spent a total of 4728 minutes training over a period of 34 days! That's 78.8 hours or 3.283333333333333 days!
    You travelled a total of 1232.9 KM. That's 3.076481597005615% around the earth!
    You averaged 139.05882352941177 minutes of training per day!

Sample charts output (with my real training data):
    - bar.png
    - pie1.png
    - pie2.png

Sample data:
    - train2.csv

