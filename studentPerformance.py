import csv
import pandas as pd
import plotly.figure_factory as pff
import statistics 
import plotly.graph_objects as go

df=pd.read_csv("StudentsPerformance.csv")
data=df["reading score"].tolist()

mean=sum(data)/len(data)
print (mean)

mode=statistics.mode(data)
print (mode)
median=statistics.median(data)
print (median)

std_dev=statistics.stdev(data)
print (std_dev)

first_stdev_start,first_stdev_end=mean-std_dev,mean+std_dev

second_stdev_start,second_stdev_end=mean-(2*std_dev),mean+(2*std_dev)

third_stdev_start,third_stdev_end=mean-(3*std_dev),mean+(3*std_dev)

list_of_data_within_1_std_deviation = [result for result in data if result > first_stdev_start and result < first_stdev_end]

list_of_data_within_2_std_deviation = [result for result in data if result > second_stdev_start and result < second_stdev_end]

list_of_data_within_3_std_deviation = [result for result in data if result > third_stdev_start and result < third_stdev_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))

print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))

print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))

fig=pff.create_distplot([data],["reading score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_stdev_start, first_stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_stdev_start, second_stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()