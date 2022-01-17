#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import datetime as dt
#matplotlib.use('Agg')
import seaborn as sns 

#Functions for date and time conversion
#convert date string to datetime format
def date_str(d,df):
    
 
    df['New_time'] = [dt.datetime.strptime(d,"%Y-%m-%d %H:%M:%S %Z") for d in d]
    df['start_time']= [dt.datetime.strptime(d,"%Y-%m-%d %H:%M:%S %Z").time() for d in d]
    df['start_time_hour']=[float(x.hour + x.minute/60) for x in df['start_time']]   
    return df

#convert time string to float time (decimal hours)
def time_str(d,df):


    df['New_ride_length']= [dt.datetime.strptime(d,"%H:%M:%S").time() for d in d]
    df['New_ride_length']=[float(x.hour + x.minute/60) for x in df['New_ride_length']]
    return df


#Remove Warnings
st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Analysis and Visualization of cyclistic-2021-data")


# open kaggle site for data inspection
link = '[DATA](https://www.kaggle.com/adehghani/cyclistic-2021-data)'
st.markdown(link, unsafe_allow_html=True)


#import dataset
trips = pd.read_csv('2021-tripdata.csv')
#First five rows
df = trips#.head(3000000)


st.write('shape of dataset',trips.shape)
#Display the table
st.table(trips.head(10))


# call convert time string to datetime format
date_obj=date_str(df['started_at'],df)



# call convert time string to float time
time_obj=time_str(date_obj['ride_length'],date_obj)



st.header("Statistics of data set")
#description of dataset
stat_trips=df.describe()
#display stat table
st.table(stat_trips)

st.header("Visualisation Using Seaborn")

#Histogram day_of_week

st.subheader("Histogram day of week")
sns.histplot(data=df, x=df['day_of_week'])
st.pyplot()

#Histogram member_casual

st.subheader("Histogram member_casual")
sns.histplot(df['member_casual'])
st.pyplot()

#Histogram rideable_type

st.subheader("Histogram rideable_type")
sns.histplot(df['rideable_type'])
st.pyplot()

#Histogram start time

st.subheader("Histogram start time")
sns.histplot(x='start_time_hour',data=time_obj)
st.pyplot()

#scatter between rider start time and ride_length
st.subheader("scatter  ride_length")
ax = plt.gca()
fig = plt.figure()
plt.scatter(x='start_time_hour',y='New_ride_length',data=time_obj)
plt.xlabel('start_time_hour')
plt.ylabel('ride_length')
plt.title('start_time_hour vs ride_length')
st.pyplot(fig)

#pairplot
st.subheader("Pairplot")
sns.pairplot(time_obj,hue='day_of_week',palette='rainbow')
st.pyplot()

#joinplot
st.subheader("JointPlot")
sns.jointplot(x='New_time',y='New_ride_length',data=time_obj,kind='scatter')
st.pyplot()
