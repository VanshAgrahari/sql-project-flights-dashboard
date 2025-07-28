import streamlit as st
import plotly.express as px
import pandas as pd
from db import my_db
dbo=my_db()
st.set_page_config(layout='wide')
st.sidebar.title('Flights Analytics')
opn=st.sidebar.selectbox('Menu',['Choose option','View Flight','Analytics'])

if opn=='View Flight':
    st.title('View Flights')
    city=dbo.fetch_city()
    col1,col2=st.columns(2)
    with col1:
        source_city=st.selectbox('Source',sorted(city))
    with col2:
        city.remove(source_city)
        dest_city=st.selectbox('Destination',sorted(city))
    btn=st.button('Click to apply')
    
    if btn:
        table=dbo.fetch_table(source_city,dest_city)
        st.dataframe(table,column_config={1:'Airline',2:'Date_of_Journey',3:'Dep_Time',4:'Duration',5:'Total_Stops',6:'Price'})
    

elif opn=='Analytics':
    st.title('View Flights Analytics')


# 1-airline piechart
    Airline,frequency=dbo.fetch_airline_freq()
    data={'Airline':Airline,'Frequency':frequency}



    df=pd.DataFrame(data)

    fig = px.pie(
        df,
    names="Airline",
    values="Frequency",
    title="Airline PieChart"
    )

    # Display in Streamlit
    st.plotly_chart(fig)


 # 2->barchart busy city
    city,frequency=dbo.busy_airport()

    # Sample data – you can replace this with SQL query result
    data = {
        "City": city,
        "Frequency": frequency
    }

    df = pd.DataFrame(data)

    # Create bar chart using Plotly
    fig = px.bar(
        df,
        x="City",
        y="Frequency",
        title="Number of Flights by City",
        labels={"Count": "Total Flights"},
        color="City"
    )

    # Show in Streamlit
    st.plotly_chart(fig)

# 3->Find all distinct airlines
    st.subheader('Daily Number Of flights Line chart')
    data=dbo.find_distinct_airlines()
    airline=st.selectbox('Select Airline',sorted(data))

    Date,Frequency=dbo.day_by_day(airline)
    data = {
        "Date": Date,
        "Frequency": Frequency
    }
    df=pd.DataFrame(data)
    fig = px.line(
        df,
        x="Date",
        y="Frequency",
        title="Number of Flights  of {} by Date".format(airline),
    )

    # Show in Streamlit
    st.plotly_chart(fig)

# flights between cities
    st.subheader('flights between cities')
    cities,frequency=dbo.flights_between_cities()
    data={'cities':cities,'frequency':frequency}
    df=pd.DataFrame(data)

    fig = px.pie(
        df,
    names="cities",
    values="frequency",
    )

    st.plotly_chart(fig)

    






else:
    st.title('Overview')
    st.markdown("""
Welcome to the **Flight Analytics Dashboard** — an interactive platform to explore flight data insights across routes, airlines, and travel dates.

This tool enables you to:
- 🔍 **Search flights** between any selected **source and destination**
- 📊 View **analytics** such as:
    - Most frequent routes  
    - Top-performing airlines  
    - Average delays by airline or route  
    - Daily and monthly flight trends

Powered by structured **SQL queries** and **interactive visualizations**, this dashboard helps travelers, analysts, and aviation enthusiasts discover meaningful patterns in flight operations.

> Use the filters on the sidebar to get started — select your source, destination, and time range to see customized results.
""")
