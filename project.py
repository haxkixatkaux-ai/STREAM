import streamlit as st 
import plotly.express as px
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 


from streamlit_option_menu import option_menu 
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

st.set_page_config(page_title="Urban air quality and health analysis",page_icon="🌍",layout="wide")
 
df=pd.read_csv("aird.csv")

with st.sidebar:
    st.sidebar.title("🌍Current air metrics")
    selected=option_menu(menu_title="Main Menu",options=["Home","Data-set","Processing","Graphs","Findings","About"],icons=["house","table","bar-chart","house","house","person"],default_index=0)

if selected=="Home":

    st.title("🏠 Weather & Health Risk Dashboard Home")
    st.subheader("Welcome to your automated weather analytics and risk visualization platform!")
    st.write("This application is built entirely using Python to clean, process, and display environmental conditions and health risk scores on-the-fly.")

    # st.title("Home")
    # st.write("welcome to  home page ")
   
    # Load your data (Mock dataframe for illustration)
    # df = pd.read_csv("your_weather_data.csv")

    # 1. Calculate the values for your metrics
    avg_temp = df['temp'].mean()
    avg_feels = df['feelslike'].mean()
    total_precip = df['precip'].sum()
    max_uv = df['uvindex'].max()
    avg_humidity = df['humidity'].mean()
    max_severity = df['Severity_Score'].max()

    # 2. Create 6 columns layout in Streamlit
    col1, col2, col3, col4= st.columns(4)

    # 3. Populate columns with metrics
    
    with col1:
        st.metric(label="💧 Total Rain", value=f"{total_precip:.2f} mm")

    with col2:
        st.metric(label="☀️ Max UV Index", value=int(max_uv))

    with col3:
        st.metric(label="☁️ Avg Humidity", value=f"{avg_humidity:.0f}%")

    with col4:
        st.metric(label="⚠️ Max Severity", value=f"{max_severity:.1f}")


        
    st.markdown("### 🚀 Quick Start Guide")
    st.markdown("1. Open the **📂 Dataset View** in the sidebar to review raw log information and summaries.")
    st.markdown("2. Navigate to **⚙️ Graph Processing** to customize filters and render interactive graphs.")


    import streamlit as st
    import pandas as pd
    import plotly.express as px

    # 1. Prepare data (Group by weather conditions and count occurrences)
    condition_counts = df['conditions'].value_counts().reset_index()
    condition_counts.columns = ['Condition', 'Count']

    # 2. Create the Plotly Donut Chart
    fig = px.pie(
        condition_counts, 
        values='Count', 
        names='Condition', 
        hole=0.5,  # This 'hole' parameter turns the pie chart into a donut chart
        color_discrete_sequence=px.colors.sequential.RdBu
    )

    # 3. Clean up the layout
    fig.update_traces(textinfo='percent+label', textposition='inside')
    fig.update_layout(
        showlegend=False,
        margin=dict(t=30, b=10, l=10, r=10),
        height=400
    )

    # 4. Display in Streamlit
    st.subheader("🌦️ Weather Conditions Distribution")
    st.plotly_chart(fig, use_container_width=True)


elif selected=="Data-set":
    st.write("Data Management Page")
    t1,t2,t3=st.tabs(["Data","Info","Summary"])
    
    
    with t1:
        st.title("Data-set")

        st.dataframe(df.head(20))

        
        import io


        st.title("📂 Weather & Health Risk Dataset Overview")
        st.subheader("Explore dataset structure, dimensions, and attribute details.")
        
        # 1. High-Level Summary Statistics
        num_rows, num_cols = df.shape
        missing_elements = df.isnull().sum().sum()
        
        col1, col2, col3 = st.columns(3)
        col1.metric("📊 Total Rows", f"{num_rows:,}")
        col2.metric("📋 Total Columns", f"{num_cols}")
        col3.metric("❌ Missing Cells", f"{missing_elements:,}")
        
        # 2. Interactive Data Preview
        st.markdown("### 🔍 Raw Dataset Preview")
        rows_to_show = st.slider("Select number of rows to preview:", min_value=5, max_value=1000, value=10)
        st.dataframe(df.head(rows_to_show), use_container_width=True)
        
        # 3. Custom Pandas info() Reconstruction for Streamlit
        st.markdown("### 📋 Columns Metadata & Structural Info")
        
        # Capture df.info() as a string using a buffer
        buffer = io.StringIO()
        df.info(buf=buffer)
        info_string = buffer.getvalue()
        
        # Alternatively, create a structured table for much better scannability
        info_df = pd.DataFrame({
            "Data Type": df.dtypes.astype(str),
            "Non-Null Count": df.notnull().sum(),
            "Null Count": df.isnull().sum(),
            "Unique Values": df.nunique()
        })
        
        tab1, tab2 = st.tabs(["📊 Structured Info Table", "💻 Raw df.info() Output"])
        
        with tab1:
            st.dataframe(info_df, use_container_width=True)
            
        with tab2:
            st.code(info_string, language="text")

        # 4. Data Dictionary (Context for your specific columns)
        with st.expander("📚 View Column Definitions & Data Dictionary"):
            st.markdown("""
            * **datetime**: Timestamp of the weather observation.
            * **temp / feelslike / temp_range**: Actual temp, perceived temp, and daily temperature variation.
            * **dew / humidity**: Atmospheric dew point and relative humidity percentage.
            * **precip / snow**: Precipitation and snowfall amounts.
            * **pressure / cloudcover / visibility**: Barometric pressure, cloud percentages, and visual range.
            * **solarradiation / solarenergy / uvindex**: Solar metrics and ultraviolet radiation risk level.
            * **moonphase / conditions / description**: Lunar cycles and general descriptive weather summaries.
            * **city / month / season / day_of_week**: Geographic and temporal dimensions.
            * **heat_index / severity_score / health_risk_score**: Calculated risk indices for human health and weather severity.
            """)


    
    
    with t2:

        info_df = pd.DataFrame(
            {
                "Column": df.columns,
                "Data Type": df.dtypes.astype(str),
                "Non-Null Count": df.notnull().sum().values,
            }
        )
        st.text(f"Total Rows: {len(df)} | Total Columns: {len(df.columns)}")
        st.dataframe(info_df, height=400, use_container_width=True)
        st.write("### Raw Column List")
        st.write(list(df.columns))
        st.title("Info")
        df.info()
        max_cols=len(df.columns) 
        st.write(df.columns)

        df.groupby(["solarradiation"])["City"].value_counts()

        

    
    

    
    with t3:
        st.title("Summary")
        st.write(df.describe())
       

elif selected=="Processing":

    st.title("Processing")
    st.write("This is a processing page ")
    t1,t2=st.tabs(["Before Processing","After Processing"])
    with t1:
        
        st.write(df.isna().sum())
    with t2:
        df.rename(columns=str.lower,inplace=True)
        st.write(df.columns.tolist())
        df.drop(columns=["precipcover","preciptype","condition_code","snowdepth","datetimeepoch","tempmax","tempmin","feelslikemin","feelslikemax","icon","sunriseepoch","sunsetepoch","precipprob","severerisk","sunrise","sunset","windgust","conditions","winddir","stations","windspeed"],inplace=True)
        st.write(df.isna().sum())
        info_df = pd.DataFrame(
            {
                "Column": df.columns,
                "Data Type": df.dtypes.astype(str),
                "Non-Null Count": df.notnull().sum().values,
            }
        )
        st.text(f"Total Rows: {len(df)} | Total Columns: {len(df.columns)}")
        st.dataframe(info_df, height=400, use_container_width=True)
        csv_data = df.to_csv(index=False)
    
        df1=pd.read_csv("processed_weather_data.csv")
        import pandas as pd
        import io


        st.title("📂 Weather & Health Risk Dataset Overview")
        st.subheader("Explore dataset structure, dimensions, and attribute details.")
        
        # 1. High-Level Summary Statistics
        num_rows, num_cols = df.shape
        missing_elements = df.isnull().sum().sum()
        
        col1, col2, col3 = st.columns(3)
        col1.metric("📊 Total Rows", f"{num_rows:,}")
        col2.metric("📋 Total Columns", f"{num_cols}")
        col3.metric("❌ Missing Cells", f"{missing_elements:,}")
        
        # 2. Interactive Data Preview
        st.markdown("### 🔍 Raw Dataset Preview")
        rows_to_show = st.slider("Select number of rows to preview:", min_value=5, max_value=100, value=10)
        st.dataframe(df.head(rows_to_show), use_container_width=True)
        
        # 3. Custom Pandas info() Reconstruction for Streamlit
        st.markdown("### 📋 Columns Metadata & Structural Info")
        
        # Capture df.info() as a string using a buffer
        buffer = io.StringIO()
        df.info(buf=buffer)
        info_string = buffer.getvalue()
        
        # Alternatively, create a structured table for much better scannability
        info_df = pd.DataFrame({
            "Data Type": df.dtypes.astype(str),
            "Non-Null Count": df.notnull().sum(),
            "Null Count": df.isnull().sum(),
            "Unique Values": df.nunique()
        })
        
        tab1, tab2 = st.tabs(["📊 Structured Info Table", "💻 Raw df.info() Output"])
        
        with tab1:
            st.dataframe(info_df, use_container_width=True)
            
        with tab2:
            st.code(info_string, language="text")

        # 4. Data Dictionary (Context for your specific columns)
        with st.expander("📚 View Column Definitions & Data Dictionary"):
            st.markdown("""
            * **datetime**: Timestamp of the weather observation.
            * **temp / feelslike / temp_range**: Actual temp, perceived temp, and daily temperature variation.
            * **dew / humidity**: Atmospheric dew point and relative humidity percentage.
            * **precip / snow**: Precipitation and snowfall amounts.
            * **pressure / cloudcover / visibility**: Barometric pressure, cloud percentages, and visual range.
            * **solarradiation / solarenergy / uvindex**: Solar metrics and ultraviolet radiation risk level.
            * **moonphase / conditions / description**: Lunar cycles and general descriptive weather summaries.
            * **city / month / season / day_of_week**: Geographic and temporal dimensions.
            * **heat_index / severity_score / health_risk_score**: Calculated risk indices for human health and weather severity.
            """)

            
elif selected=="Graphs":

    df1=pd.read_csv("processed_weather_data.csv")
    st.write("GRAPH DASHBOARD ")
    t1,t2,t3,t4,t5,t6=st.tabs(["Univariate -Distributions","Categorical Breakdown","Relationships","Lineplots","3D Scatter Plot","Sunburst Chart"])
    

    PRIMARY = "#2E6F95"
    SECONDARY = "#E8743B"
    TERTIARY = "#5FA777"

    CITY_PALETTE = ["#2E6F95", "#E8743B", "#5FA777", "#C44E52", "#8172B2",
                    "#937860", "#DA8BC3", "#8C8C8C", "#CCB974", "#64B5CD"]
    
    HOVER_BASIC = ["city", "datetime"]



    with t1:
        st.header("1. Univariate Distribution")

        col1, col2, col3 = st.columns(3)

        with col1:
                fig = px.histogram(
                    df1, x="temp", nbins=15, color_discrete_sequence=[PRIMARY],
                    hover_data=HOVER_BASIC, title="Temperature Distribution",
                )
                st.plotly_chart(fig, use_container_width=True)

        with col2:
                fig = px.histogram(
                    df1, x="health_risk_score", nbins=15, color_discrete_sequence=[SECONDARY],
                    marginal="rug", hover_data=HOVER_BASIC, title="Health Risk Score Distribution",
                )
                st.plotly_chart(fig, use_container_width=True)

        with col3:
                fig = px.histogram(
                    df1, x="uvindex", nbins=12, color_discrete_sequence=[TERTIARY],
                    marginal="rug", hover_data=HOVER_BASIC, title="UV Index Distribution",
                )
                st.plotly_chart(fig, use_container_width=True)

        col4, col5 = st.columns(2)

        with col4:
                fig = px.histogram(
                    df1, x="humidity", nbins=15, color_discrete_sequence=[PRIMARY],
                    marginal="rug", hover_data=HOVER_BASIC, title="Humidity Distribution",
                )
                st.plotly_chart(fig, use_container_width=True)

        with col5:
                fig = px.histogram(
                    df1, x="severity_score", nbins=15, color_discrete_sequence=[SECONDARY],
                    marginal="rug", hover_data=HOVER_BASIC, title="Severity Score Distribution",
                )
                st.plotly_chart(fig, use_container_width=True)
                

            


    with t2:
        st.header("2. Categorical Breakdown")
        col1, col2 ,col3 = st.columns(3)

        with col1:
            city_counts = df1["city"].value_counts().reset_index()
            city_counts.columns = ["city", "count"]
            fig = px.bar(
                city_counts, x="city", y="count", color_discrete_sequence=[PRIMARY],
                hover_data={"city": True, "count": True}, title="Records per City",
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            dow_counts = (
                df1["day_of_week"]
                .value_counts()
                .reindex(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
                .reset_index()
            )
            dow_counts.columns = ["day_of_week", "count"]
            fig = px.bar(
                dow_counts, x="day_of_week", y="count", color_discrete_sequence=[PRIMARY],
                hover_data={"day_of_week": True, "count": True}, title="Records by Day of Week",
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col3:
                weekend_counts = df1["is_weekend"].value_counts().reset_index()
                weekend_counts.columns = ["is_weekend", "count"]
                weekend_counts["label"] = weekend_counts["is_weekend"].map({True: "Weekend", False: "Weekday"})
                fig = px.pie(
                    weekend_counts, names="label", values="count",
                    color_discrete_sequence=[PRIMARY, SECONDARY],
                    hover_data={"count": True}, title="Weekday vs Weekend Records",
                )
                st.plotly_chart(fig, use_container_width=True)
    

    with t3:
        st.header("3. Relationships Between Variables")
        col1, col2 = st.columns(2)
        
        
        with col1:
            fig = px.scatter(
                df1, x="severity_score", y="health_risk_score",
                color_discrete_sequence=[PRIMARY],
                hover_data=["city", "datetime"],
                title="Severity Score vs Health Risk Score",
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            fig = px.scatter(
                df1, x="temp", y="solarenergy", color="city",
                color_discrete_sequence=CITY_PALETTE,
                hover_data=["datetime", "humidity"],
                title="Temperature vs Solar Energy",
            )
            st.plotly_chart(fig, use_container_width=True)

        col3, col4 = st.columns(2)

        with col3:
            cols = ["temp", "humidity", "dew", "uvindex", "pressure", "cloudcover",
                    "severity_score", "health_risk_score"]
            corr = df1[cols].corr()
            fig = px.imshow(
                corr, text_auto=".2f", color_continuous_scale="RdBu_r",
                title="Correlation Heatmap",
            )
            fig.update_traces(hovertemplate="%{x} vs %{y}<br>corr = %{z:.2f}<extra></extra>")
            st.plotly_chart(fig, use_container_width=True)

        with col4:
            fig = px.violin(
                df1, x="city", y="health_risk_score", color_discrete_sequence=[PRIMARY],
                box=True, points="all", hover_data=["datetime"],
                title="Health Risk Score Spread by City",
            )
            st.plotly_chart(fig, use_container_width=True)

    

    with t4:
        st.header("4. Trends Over Time")

        daily_temp = df1.groupby(["datetime", "city"])["temp"].mean().reset_index()
        fig = px.line(
            daily_temp, x="datetime", y="temp", color="city",
            color_discrete_sequence=CITY_PALETTE, markers=True,
            hover_data={"temp": ":.1f"}, title="Average Daily Temperature by City",
        )
        st.plotly_chart(fig, use_container_width=True)

        col1, col2 = st.columns(2)

        with col1:
            daily_health = df1.groupby("datetime")["health_risk_score"].mean().reset_index()
            fig = px.line(
                daily_health, x="datetime", y="health_risk_score", markers=True,
                color_discrete_sequence=[SECONDARY], hover_data={"health_risk_score": ":.2f"},
                title="Average Health Risk Score Over Time",
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            daily_uv = df1.groupby("datetime")["uvindex"].mean().reset_index()
            fig = px.line(
                daily_uv, x="datetime", y="uvindex", markers=True,
                color_discrete_sequence=[TERTIARY], hover_data={"uvindex": ":.2f"},
                title="Average UV Index Over Time",
            )
            st.plotly_chart(fig, use_container_width=True)

        daily_solar = df.groupby("datetime")["solarenergy"].mean().reset_index()
        fig = px.line(
            daily_solar, x="datetime", y="solarenergy", markers=True,
            color_discrete_sequence=[PRIMARY], hover_data={"solarenergy": ":.2f"},
            title="Average Solar Energy Over Time",
        )
        st.plotly_chart(fig, use_container_width=True)


    with t5:
        st.header("5. 3D Scatter Plot")

        fig = px.scatter_3d(
            df1, x="temp", y="humidity", z="health_risk_score",
            color="city", color_discrete_sequence=CITY_PALETTE,
            hover_data={"datetime": True, "temp": True, "humidity": True, "health_risk_score": True},
            title="Temperature vs Humidity vs Health Risk Score",
        )
        fig.update_traces(marker=dict(size=4))
        fig.update_layout(height=600)
        st.plotly_chart(fig, use_container_width=True)
    

    with t6:
        st.header("6. Sunburst Chart")

        sunburst_df = (
            df1.groupby(["city", "day_of_week"])
            .agg(count=("health_risk_score", "size"), avg_health_risk=("health_risk_score", "mean"))
            .reset_index()
        )

        fig = px.sunburst(
            sunburst_df, path=["city", "day_of_week"], values="count",
            color="avg_health_risk", color_continuous_scale="RdYlBu_r",
            hover_data={"count": True, "avg_health_risk": ":.2f"},
            title="Records by City & Day of Week (size = count, color = avg health risk)",
        )
        fig.update_layout(height=600)
        st.plotly_chart(fig, use_container_width=True)

####
elif selected=="Findings":
     
    # Header 
    st.title("A: Weather and Health Risk Analytics")

    # Insights and Observations
    st.subheader("Key Insights")

    st.markdown("""
    * **Temperature Extremes**: Phoenix and Dallas sit at the hot end of the temperature range, while cities like San Jose and San Diego stay milder.
    * **Correlation Drivers**: The correlation heatmap shows which weather variables move together with the health risk score—use it to spot what's actually driving risk (usually temperature and UV index rather than pressure or cloud cover).
    * **Condition Breakdown**: The sunburst chart makes it easy to see, city by city, which weather condition is most common and whether that condition carries a higher average health risk.
    * **Risk Synergy**: The 3D plot lets you rotate and explore whether high temperature *and* high humidity together push the health risk score up more than either one alone.
    """)


elif selected=="About":
    st.header("About")
    st.write("""
    This is a simple weather data dashboard project made using Python.

    **Libraries used:**
    - Pandas and NumPy for data handling
    - Matplotlib and Seaborn for graphs
    - Plotly for interactive 3D and sunburst charts
    - Streamlit for building the web app 
        """)





                

        


       
