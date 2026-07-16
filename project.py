# import streamlit as st 
# import plotly.express as px
# import plotly.io as pio
# import plotly.graph_objects as go
# import pandas as pd
# import seaborn as sns 
# import matplotlib.pyplot as plt 


# from streamlit_option_menu import option_menu 
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# st.set_page_config(page_title="Urban air quality and health analysis",page_icon="🌍",layout="wide")

# # ============================================================
# # 🎨 GLOBAL PLOTLY THEME — no white plot background / white gridlines,
# # so data never blends into the page or disappears.
# # ============================================================
# _custom_template = go.layout.Template()
# _custom_template.layout = go.Layout(
#     paper_bgcolor="rgba(0,0,0,0)",   # transparent -> shows the card behind it
#     plot_bgcolor="#eef3f7",          # light blue-grey, never plain white
#     font=dict(color="#1f3b4d", size=13),
#     title=dict(font=dict(size=18, color="#1f3b4d")),
#     xaxis=dict(gridcolor="#c7d2db", zerolinecolor="#c7d2db", linecolor="#8a97a3"),
#     yaxis=dict(gridcolor="#c7d2db", zerolinecolor="#c7d2db", linecolor="#8a97a3"),
#     colorway=["#2E6F95", "#E8743B", "#5FA777", "#C44E52", "#8172B2",
#               "#937860", "#DA8BC3", "#8C8C8C", "#CCB974", "#64B5CD"],
# )
# pio.templates["dashboard"] = _custom_template
# pio.templates.default = "dashboard"

# # ============================================================
# # 🎨 CUSTOM CSS — colorful headers, cards, tabs, badges
# # ============================================================
# CUSTOM_CSS = """
# <style>
# :root{
#     --primary:#2E6F95;
#     --secondary:#E8743B;
#     --tertiary:#5FA777;
#     --purple:#8172B2;
#     --pink:#DA8BC3;
#     --gold:#CCB974;
#     --red:#C44E52;
# }

# /* Page background */
# .stApp{
#     background: linear-gradient(180deg, #f7f9fc 0%, #ffffff 35%);
# }

# /* Sidebar */
# section[data-testid="stSidebar"]{
#     background: linear-gradient(180deg, #123a52 0%, #2E6F95 100%);
# }
# section[data-testid="stSidebar"] * { color:#f2f6fa !important; }

# /* Gradient page titles (h1) */
# h1{
#     background: linear-gradient(90deg, var(--primary), var(--tertiary));
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     background-clip: text;
#     font-weight: 800 !important;
# }

# /* Sub-headers (h2, h3) get a colored left bar */
# h2, h3{
#     color:#1f3b4d !important;
#     border-left: 6px solid var(--secondary);
#     padding-left: 12px;
# }

# /* st.metric cards */
# div[data-testid="stMetric"]{
#     background: #ffffff;
#     border: 1px solid #e5e9ef;
#     border-left: 6px solid var(--primary);
#     border-radius: 12px;
#     padding: 14px 16px;
#     box-shadow: 0 2px 8px rgba(0,0,0,0.06);
# }
# div[data-testid="stMetricLabel"]{ color: var(--primary) !important; font-weight:600; }
# div[data-testid="stMetricValue"]{ color:#1f3b4d !important; }

# /* Tabs */
# button[data-baseweb="tab"]{
#     font-weight:600;
#     color:#5a6b78;
# }
# button[data-baseweb="tab"][aria-selected="true"]{
#     color: var(--secondary) !important;
#     border-bottom: 3px solid var(--secondary) !important;
# }

# /* Expander */
# details{
#     border: 1px solid #e5e9ef;
#     border-radius: 10px;
#     background:#fbfcfe;
# }

# /* Colored inline text helpers */
# .badge{
#     display:inline-block;
#     padding:3px 12px;
#     border-radius:999px;
#     font-weight:700;
#     font-size:0.85rem;
#     color:white;
#     margin-right:6px;
# }
# .badge-blue{ background: var(--primary); }
# .badge-orange{ background: var(--secondary); }
# .badge-green{ background: var(--tertiary); }
# .badge-purple{ background: var(--purple); }
# .badge-pink{ background: var(--pink); }
# .badge-red{ background: var(--red); }

# .highlight-box{
#     border-radius: 12px;
#     padding: 16px 20px;
#     margin: 10px 0;
#     color: white;
#     font-size: 1rem;
#     line-height:1.5;
# }
# .box-blue{ background: linear-gradient(135deg, #2E6F95, #4a95bd); }
# .box-orange{ background: linear-gradient(135deg, #E8743B, #f0a274); }
# .box-green{ background: linear-gradient(135deg, #5FA777, #86c79c); }
# .box-purple{ background: linear-gradient(135deg, #8172B2, #a99bd1); }

# .finding-title{
#     font-size:1.3rem;
#     font-weight:800;
#     color:#1f3b4d;
# }

# /* Chart & dataframe cards — never plain white, so plotted data stays visible */
# div[data-testid="stPlotlyChart"]{
#     background:#eef3f7;
#     border-radius: 14px;
#     padding: 10px;
#     border: 1px solid #d8e0e8;
#     box-shadow: 0 2px 10px rgba(0,0,0,0.05);
# }
# div[data-testid="stDataFrame"], div[data-testid="stDataEditor"]{
#     background:#eef3f7;
#     border-radius: 12px;
#     padding: 6px;
#     border: 1px solid #d8e0e8;
# }

# /* ------------------------------------------------------------
#    FIX: Streamlit's dark-theme default text color (light grey)
#    was leaking through on plain paragraphs / bullet lists / labels,
#    making them nearly invisible against our light page background.
#    Force dark, readable text everywhere in the main content area.
#    ------------------------------------------------------------ */
# [data-testid="stAppViewContainer"] p,
# [data-testid="stAppViewContainer"] li,
# [data-testid="stAppViewContainer"] span,
# [data-testid="stAppViewContainer"] label,
# [data-testid="stAppViewContainer"] div[data-testid="stMarkdownContainer"],
# [data-testid="stAppViewContainer"] div[data-testid="stText"],
# [data-testid="stAppViewContainer"] div[data-testid="stMetricLabel"] p,
# [data-testid="stAppViewContainer"] div[data-testid="stCaptionContainer"]{
#     color:#1f3b4d !important;
# }

# /* Re-assert white text inside colored badges / highlight boxes
#    (must come AFTER the rule above so it wins the cascade) */
# .badge, .badge *{ color:#ffffff !important; }
# .highlight-box, .highlight-box *{ color:#ffffff !important; }
# </style>
# """
# st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# def colored_header(text, subtitle=None, color="var(--primary)", icon=""):
#     """Render a vibrant gradient-style header with an optional subtitle."""
#     st.markdown(
#         f"""
#         <div style="margin-bottom:14px;">
#             <div style="font-size:2rem; font-weight:800; color:{color};">{icon} {text}</div>
#             {f'<div style="font-size:1.05rem; color:#5a6b78; margin-top:2px;">{subtitle}</div>' if subtitle else ''}
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

# def badge(text, kind="blue"):
#     return f'<span class="badge badge-{kind}">{text}</span>'

# def highlight_box(text, kind="blue"):
#     st.markdown(f'<div class="highlight-box box-{kind}">{text}</div>', unsafe_allow_html=True)

# df=pd.read_csv("aird.csv")

# with st.sidebar:
#     st.sidebar.title("🌍Current air metrics")
#     selected=option_menu(menu_title="Main Menu",options=["Home","Data-set","Processing","Graphs","Findings","About"],icons=["house","table","bar-chart","house","house","person"],default_index=0)

# if selected=="Home":

#     colored_header(
#         "Weather & Health Risk Dashboard",
#         subtitle="Welcome to your automated weather analytics and risk visualization platform!",
#         icon="🏠",
#     )
#     st.markdown(
#         f"{badge('Live Data', 'green')}{badge('Python', 'blue')}{badge('Streamlit', 'orange')}{badge('Plotly', 'purple')}",
#         unsafe_allow_html=True,
#     )
#     st.write("This application is built entirely using Python to clean, process, and display environmental conditions and health risk scores on-the-fly.")

#     # st.title("Home")
#     # st.write("welcome to  home page ")
   
#     # Load your data (Mock dataframe for illustration)
#     # df = pd.read_csv("your_weather_data.csv")

#     # 1. Calculate the values for your metrics
#     avg_temp = df['temp'].mean()
#     avg_feels = df['feelslike'].mean()
#     total_precip = df['precip'].sum()
#     max_uv = df['uvindex'].max()
#     avg_humidity = df['humidity'].mean()
#     max_severity = df['Severity_Score'].max()

#     # 2. Create 6 columns layout in Streamlit
#     col1, col2, col3, col4= st.columns(4)

#     # 3. Populate columns with colorful metric cards

#     def metric_card(icon, label, value, kind):
#         st.markdown(
#             f"""
#             <div class="highlight-box box-{kind}" style="text-align:center;">
#                 <div style="font-size:1.8rem;">{icon}</div>
#                 <div style="font-size:0.9rem; opacity:0.9;">{label}</div>
#                 <div style="font-size:1.6rem; font-weight:800;">{value}</div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#     with col1:
#         metric_card("💧", "Total Rain", f"{total_precip:.2f} mm", "blue")

#     with col2:
#         metric_card("☀️", "Max UV Index", int(max_uv), "orange")

#     with col3:
#         metric_card("☁️", "Avg Humidity", f"{avg_humidity:.0f}%", "green")

#     with col4:
#         metric_card("⚠️", "Max Severity", f"{max_severity:.1f}", "purple")


        
#     st.markdown("### 🚀 Quick Start Guide")
#     st.markdown(
#         f'{badge("Step 1", "blue")} Open the **📂 Dataset View** in the sidebar to review raw log information and summaries.',
#         unsafe_allow_html=True,
#     )
#     st.markdown(
#         f'{badge("Step 2", "orange")} Navigate to **⚙️ Graph Processing** to customize filters and render interactive graphs.',
#         unsafe_allow_html=True,
#     )


#     import streamlit as st
#     import pandas as pd
#     import plotly.express as px

#     # 1. Prepare data (Group by weather conditions and count occurrences)
#     condition_counts = df['conditions'].value_counts().reset_index()
#     condition_counts.columns = ['Condition', 'Count']

#     # 2. Create the Plotly Donut Chart
#     fig = px.pie(
#         condition_counts, 
#         values='Count', 
#         names='Condition', 
#         hole=0.5,  # This 'hole' parameter turns the pie chart into a donut chart
#         color_discrete_sequence=["#2E6F95", "#E8743B", "#5FA777", "#C44E52", "#8172B2", "#CCB974"]
#     )

#     # 3. Clean up the layout
#     fig.update_traces(textinfo='percent+label', textposition='inside')
#     fig.update_layout(
#         showlegend=False,
#         margin=dict(t=30, b=10, l=10, r=10),
#         height=400
#     )

#     # 4. Display in Streamlit
#     st.subheader("🌦️ Weather Conditions Distribution")
#     st.plotly_chart(fig, use_container_width=True)


# elif selected=="Data-set":
#     st.write("Data Management Page")
#     t1,t2,t3=st.tabs(["Data","Info","Summary"])
    
    
#     with t1:
#         st.title("Data-set")

#         st.dataframe(df.head(20))

        
#         import io


#         st.title("📂 Weather & Health Risk Dataset Overview")
#         st.subheader("Explore dataset structure, dimensions, and attribute details.")
        
#         # 1. High-Level Summary Statistics
#         num_rows, num_cols = df.shape
#         missing_elements = df.isnull().sum().sum()
        
#         col1, col2, col3 = st.columns(3)
#         col1.metric("📊 Total Rows", f"{num_rows:,}")
#         col2.metric("📋 Total Columns", f"{num_cols}")
#         col3.metric("❌ Missing Cells", f"{missing_elements:,}")
        
#         # 2. Interactive Data Preview
#         st.markdown("### 🔍 Raw Dataset Preview")
#         rows_to_show = st.slider("Select number of rows to preview:", min_value=5, max_value=1000, value=10)
#         st.dataframe(df.head(rows_to_show), use_container_width=True)
        
#         # 3. Custom Pandas info() Reconstruction for Streamlit
#         st.markdown("### 📋 Columns Metadata & Structural Info")
        
#         # Capture df.info() as a string using a buffer
#         buffer = io.StringIO()
#         df.info(buf=buffer)
#         info_string = buffer.getvalue()
        
#         # Alternatively, create a structured table for much better scannability
#         info_df = pd.DataFrame({
#             "Data Type": df.dtypes.astype(str),
#             "Non-Null Count": df.notnull().sum(),
#             "Null Count": df.isnull().sum(),
#             "Unique Values": df.nunique()
#         })
        
#         tab1, tab2 = st.tabs(["📊 Structured Info Table", "💻 Raw df.info() Output"])
        
#         with tab1:
#             st.dataframe(info_df, use_container_width=True)
            
#         with tab2:
#             st.code(info_string, language="text")

#         # 4. Data Dictionary (Context for your specific columns)
#         with st.expander("📚 View Column Definitions & Data Dictionary"):
#             st.markdown("""
#             * **datetime**: Timestamp of the weather observation.
#             * **temp / feelslike / temp_range**: Actual temp, perceived temp, and daily temperature variation.
#             * **dew / humidity**: Atmospheric dew point and relative humidity percentage.
#             * **precip / snow**: Precipitation and snowfall amounts.
#             * **pressure / cloudcover / visibility**: Barometric pressure, cloud percentages, and visual range.
#             * **solarradiation / solarenergy / uvindex**: Solar metrics and ultraviolet radiation risk level.
#             * **moonphase / conditions / description**: Lunar cycles and general descriptive weather summaries.
#             * **city / month / season / day_of_week**: Geographic and temporal dimensions.
#             * **heat_index / severity_score / health_risk_score**: Calculated risk indices for human health and weather severity.
#             """)


    
    
#     with t2:

#         info_df = pd.DataFrame(
#             {
#                 "Column": df.columns,
#                 "Data Type": df.dtypes.astype(str),
#                 "Non-Null Count": df.notnull().sum().values,
#             }
#         )
#         st.text(f"Total Rows: {len(df)} | Total Columns: {len(df.columns)}")
#         st.dataframe(info_df, height=400, use_container_width=True)
#         st.write("### Raw Column List")
#         st.write(list(df.columns))
#         st.title("Info")
#         df.info()
#         max_cols=len(df.columns) 
#         st.write(df.columns)

#         df.groupby(["solarradiation"])["City"].value_counts()

        

    
    

    
#     with t3:
#         st.title("Summary")
#         st.write(df.describe())
       

# elif selected=="Processing":

#     st.title("Processing")
#     st.write("This is a processing page ")
#     t1,t2=st.tabs(["Before Processing","After Processing"])
#     with t1:
        
#         st.write(df.isna().sum())
#     with t2:
#         df.rename(columns=str.lower,inplace=True)
#         st.write(df.columns.tolist())
#         df.drop(columns=["precipcover","preciptype","condition_code","snowdepth","datetimeepoch","tempmax","tempmin","feelslikemin","feelslikemax","icon","sunriseepoch","sunsetepoch","precipprob","severerisk","sunrise","sunset","windgust","conditions","winddir","stations","windspeed"],inplace=True)
#         st.write(df.isna().sum())
#         info_df = pd.DataFrame(
#             {
#                 "Column": df.columns,
#                 "Data Type": df.dtypes.astype(str),
#                 "Non-Null Count": df.notnull().sum().values,
#             }
#         )
#         st.text(f"Total Rows: {len(df)} | Total Columns: {len(df.columns)}")
#         st.dataframe(info_df, height=400, use_container_width=True)
#         csv_data = df.to_csv(index=False)
    
#         df1=pd.read_csv("processed_weather_data.csv")
#         import pandas as pd
#         import io


#         st.title("📂 Weather & Health Risk Dataset Overview")
#         st.subheader("Explore dataset structure, dimensions, and attribute details.")
        
#         # 1. High-Level Summary Statistics
#         num_rows, num_cols = df.shape
#         missing_elements = df.isnull().sum().sum()
        
#         col1, col2, col3 = st.columns(3)
#         col1.metric("📊 Total Rows", f"{num_rows:,}")
#         col2.metric("📋 Total Columns", f"{num_cols}")
#         col3.metric("❌ Missing Cells", f"{missing_elements:,}")
        
#         # 2. Interactive Data Preview
#         st.markdown("### 🔍 Raw Dataset Preview")
#         rows_to_show = st.slider("Select number of rows to preview:", min_value=5, max_value=100, value=10)
#         st.dataframe(df.head(rows_to_show), use_container_width=True)
        
#         # 3. Custom Pandas info() Reconstruction for Streamlit
#         st.markdown("### 📋 Columns Metadata & Structural Info")
        
#         # Capture df.info() as a string using a buffer
#         buffer = io.StringIO()
#         df.info(buf=buffer)
#         info_string = buffer.getvalue()
        
#         # Alternatively, create a structured table for much better scannability
#         info_df = pd.DataFrame({
#             "Data Type": df.dtypes.astype(str),
#             "Non-Null Count": df.notnull().sum(),
#             "Null Count": df.isnull().sum(),
#             "Unique Values": df.nunique()
#         })
        
#         tab1, tab2 = st.tabs(["📊 Structured Info Table", "💻 Raw df.info() Output"])
        
#         with tab1:
#             st.dataframe(info_df, use_container_width=True)
            
#         with tab2:
#             st.code(info_string, language="text")

#         # 4. Data Dictionary (Context for your specific columns)
#         with st.expander("📚 View Column Definitions & Data Dictionary"):
#             st.markdown("""
#             * **datetime**: Timestamp of the weather observation.
#             * **temp / feelslike / temp_range**: Actual temp, perceived temp, and daily temperature variation.
#             * **dew / humidity**: Atmospheric dew point and relative humidity percentage.
#             * **precip / snow**: Precipitation and snowfall amounts.
#             * **pressure / cloudcover / visibility**: Barometric pressure, cloud percentages, and visual range.
#             * **solarradiation / solarenergy / uvindex**: Solar metrics and ultraviolet radiation risk level.
#             * **moonphase / conditions / description**: Lunar cycles and general descriptive weather summaries.
#             * **city / month / season / day_of_week**: Geographic and temporal dimensions.
#             * **heat_index / severity_score / health_risk_score**: Calculated risk indices for human health and weather severity.
#             """)

            
# elif selected=="Graphs":

#     df1=pd.read_csv("processed_weather_data.csv")
#     st.write("GRAPH DASHBOARD ")
#     t1,t2,t3,t4,t5,t6=st.tabs(["Univariate -Distributions","Categorical Breakdown","Relationships","Lineplots","3D Scatter Plot","Sunburst Chart"])
    

#     PRIMARY = "#2E6F95"
#     SECONDARY = "#E8743B"
#     TERTIARY = "#5FA777"

#     CITY_PALETTE = ["#2E6F95", "#E8743B", "#5FA777", "#C44E52", "#8172B2",
#                     "#937860", "#DA8BC3", "#8C8C8C", "#CCB974", "#64B5CD"]
    
#     HOVER_BASIC = ["city", "datetime"]



#     with t1:
#         st.header("1. Univariate Distribution")

#         col1, col2, col3 = st.columns(3)

#         with col1:
                
        
        
#                 fig = px.histogram(
#                     df1, x="temp", nbins=15, color_discrete_sequence=[PRIMARY],
#                     hover_data=HOVER_BASIC, title="Temperature Distribution",
#                 )
#                 st.plotly_chart(fig, use_container_width=True)

#         with col2:
#                 fig = px.histogram(
#                     df1, x="health_risk_score", nbins=15, color_discrete_sequence=[SECONDARY],
#                     marginal="rug", hover_data=HOVER_BASIC, title="Health Risk Score Distribution",
#                 )
#                 st.plotly_chart(fig, use_container_width=True)

#         with col3:
#                 fig = px.histogram(
#                     df1, x="uvindex", nbins=12, color_discrete_sequence=[TERTIARY],
#                     marginal="rug", hover_data=HOVER_BASIC, title="UV Index Distribution",
#                 )
#                 st.plotly_chart(fig, use_container_width=True)

#         col4, col5 = st.columns(2)

#         with col4:
#                 fig = px.histogram(
#                     df1, x="humidity", nbins=15, color_discrete_sequence=[PRIMARY],
#                     marginal="rug", hover_data=HOVER_BASIC, title="Humidity Distribution",
#                 )
#                 st.plotly_chart(fig, use_container_width=True)

#         with col5:
#                 fig = px.histogram(
#                     df1, x="severity_score", nbins=15, color_discrete_sequence=[SECONDARY],
#                     marginal="rug", hover_data=HOVER_BASIC, title="Severity Score Distribution",
#                 )
#                 st.plotly_chart(fig, use_container_width=True)
                

            


#     with t2:
#         st.header("2. Categorical Breakdown")
        
#         city_counts = df1["city"].value_counts().reset_index()
#         city_counts.columns = ["city", "count"]
#         fig = px.bar(
#             city_counts, x="city", y="count", color_discrete_sequence=[PRIMARY],
#             hover_data={"city": True, "count": True}, title="Records per City",
#         )
#         st.plotly_chart(fig, use_container_width=True)

    
#         dow_counts = (
#             df1["day_of_week"]
#             .value_counts()
#             .reindex(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
#             .reset_index()
#         )
#         dow_counts.columns = ["day_of_week", "count"]
#         fig = px.bar(
#             dow_counts, x="day_of_week", y="count", color_discrete_sequence=[PRIMARY],
#             hover_data={"day_of_week": True, "count": True}, title="Records by Day of Week",
#         )
#         st.plotly_chart(fig, use_container_width=True)
        
    
#         weekend_counts = df1["is_weekend"].value_counts().reset_index()
#         weekend_counts.columns = ["is_weekend", "count"]
#         weekend_counts["label"] = weekend_counts["is_weekend"].map({True: "Weekend", False: "Weekday"})
#         fig = px.pie(
#             weekend_counts, names="label", values="count",
#             color_discrete_sequence=[PRIMARY, SECONDARY],
#             hover_data={"count": True}, title="Weekday vs Weekend Records",
#         )
#         st.plotly_chart(fig, use_container_width=True)


#     with t3:
#         st.header("3. Relationships Between Variables")
    
        
        
    
#         fig = px.scatter(
#             df1, x="severity_score", y="health_risk_score",
#             color_discrete_sequence=[PRIMARY],
#             hover_data=["city", "datetime"],
#             title="Severity Score vs Health Risk Score",
#         )
#         st.plotly_chart(fig, use_container_width=True)

    
#         fig = px.scatter(
#             df1, x="temp", y="solarenergy", color="city",
#             color_discrete_sequence=CITY_PALETTE,
#             hover_data=["datetime", "humidity"],
#             title="Temperature vs Solar Energy",
#         )
#         st.plotly_chart(fig, use_container_width=True)

    
#         cols = ["temp", "humidity", "dew", "uvindex", "pressure", "cloudcover",
#                 "severity_score", "health_risk_score"]
#         corr = df1[cols].corr()
#         fig = px.imshow(
#             corr, text_auto=".2f", color_continuous_scale="RdBu_r",
#             title="Correlation Heatmap",
#         )
#         fig.update_traces(hovertemplate="%{x} vs %{y}<br>corr = %{z:.2f}<extra></extra>")
#         st.plotly_chart(fig, use_container_width=True)

#         highlight_box(
#             "🔗 <b>Correlation Drivers:</b> The correlation heatmap shows which weather variables move together "
#             "with the health risk score — use it to spot what's actually driving risk (usually temperature and "
#             "UV index rather than pressure or cloud cover).",
#             "blue",
#         )

    

#     with t4:
#         st.header("4. Trends Over Time")

#         daily_temp = df1.groupby(["datetime", "city"])["temp"].mean().reset_index()
#         fig = px.line(
#             daily_temp, x="datetime", y="temp", color="city",
#             color_discrete_sequence=CITY_PALETTE, markers=True,
#             hover_data={"temp": ":.1f"}, title="Average Daily Temperature by City",
#         )
#         st.plotly_chart(fig, use_container_width=True)

#         highlight_box(
#             "🌡️ <b>Temperature Extremes:</b> Phoenix and Dallas sit at the hot end of the temperature range, "
#             "while cities like San Jose and San Diego stay milder.",
#             "orange",
#         )

#         col1, col2 = st.columns(2)

#         with col1:
#             daily_health = df1.groupby("datetime")["health_risk_score"].mean().reset_index()
#             fig = px.line(
#                 daily_health, x="datetime", y="health_risk_score", markers=True,
#                 color_discrete_sequence=[SECONDARY], hover_data={"health_risk_score": ":.2f"},
#                 title="Average Health Risk Score Over Time",
#             )
#             st.plotly_chart(fig, use_container_width=True)

#         with col2:
#             daily_uv = df1.groupby("datetime")["uvindex"].mean().reset_index()
#             fig = px.line(
#                 daily_uv, x="datetime", y="uvindex", markers=True,
#                 color_discrete_sequence=[TERTIARY], hover_data={"uvindex": ":.2f"},
#                 title="Average UV Index Over Time",
#             )
#             st.plotly_chart(fig, use_container_width=True)

#         daily_solar = df.groupby("datetime")["solarenergy"].mean().reset_index()
#         fig = px.line(
#             daily_solar, x="datetime", y="solarenergy", markers=True,
#             color_discrete_sequence=[PRIMARY], hover_data={"solarenergy": ":.2f"},
#             title="Average Solar Energy Over Time",
#         )
#         st.plotly_chart(fig, use_container_width=True)


#     with t5:
#         st.header("5. 3D Scatter Plot")

#         fig = px.scatter_3d(
#             df1, x="temp", y="humidity", z="health_risk_score",
#             color="city", color_discrete_sequence=CITY_PALETTE,
#             hover_data={"datetime": True, "temp": True, "humidity": True, "health_risk_score": True},
#             title="Temperature vs Humidity vs Health Risk Score",
#         )
#         fig.update_traces(marker=dict(size=4))
#         fig.update_layout(height=600)
#         st.plotly_chart(fig, use_container_width=True)
    
#         highlight_box(
#             "🧩 <b>Risk Synergy:</b> The 3D plot lets you rotate and explore whether high temperature "
#             "<i>and</i> high humidity together push the health risk score up more than either one alone.",
#             "purple",
#         )
#     with t6:
#         st.header("6. Sunburst Chart")

#         sunburst_df = (
#             df1.groupby(["city", "day_of_week"])
#             .agg(count=("health_risk_score", "size"), avg_health_risk=("health_risk_score", "mean"))
#             .reset_index()
#         )

#         fig = px.sunburst(
#             sunburst_df, path=["city", "day_of_week"], values="count",
#             color="avg_health_risk", color_continuous_scale="RdYlBu_r",
#             hover_data={"count": True, "avg_health_risk": ":.2f"},
#             title="Records by City & Day of Week (size = count, color = avg health risk)",
#         )
#         fig.update_layout(height=600)
#         st.plotly_chart(fig, use_container_width=True)
#         highlight_box(
#             "🌆 <b>Condition Breakdown:</b> The sunburst chart makes it easy to see, city by city, which weather "
#             "condition is most common and whether that condition carries a higher average health risk.",
#             "green",
#         )
# ####
# elif selected=="Findings":

#     colored_header("Weather and Health Risk Analytics", subtitle="Key Insights", icon="🔎")

#     t1,t2,t3,=st.tabs(["🔵 First finding","🟠 Second finding","🟢 Third finding"])
#     with t1:
#         st.markdown(f'<div class="finding-title">{badge("Finding 1", "blue")} </div>', unsafe_allow_html=True)
#         st.image("s1.png")
#     with t2:
#         st.markdown(f'<div class="finding-title">{badge("Finding 2", "orange")} </div>', unsafe_allow_html=True)
#         st.image("s2.png")
#     with t3:
#         st.markdown(f'<div class="finding-title">{badge("Finding 3", "green")} </div>', unsafe_allow_html=True)
#         st.image("s3.png")
    


# elif selected=="About":
#     st.header("About")
#     # st.write("""
#     # This is a simple weather data dashboard project made using Python.

#     # **Libraries used:**
#     # - Pandas and NumPy for data handling
#     # - Matplotlib and Seaborn for graphs
#     # - Plotly for interactive 3D and sunburst charts
#     # - Streamlit for building the web app 
#     #     """)
     
    

#     # def about_page():
#     #     st.title("ℹ️ About This Project")

#     st.markdown(f'## {badge("Overview", "blue")}', unsafe_allow_html=True)
#     st.write("""
#     This project analyzes a weather dataset covering **1,000 daily records**
#     across **10 major U.S. cities** — Chicago, New York City, Phoenix, Dallas,
#     Philadelphia, Los Angeles, San Diego, San Jose, Houston, and San Antonio —
#     for **September 2024 (Fall season)**. The goal is to explore weather
#     patterns, temperature behavior, and their relationship to a derived
#     health-risk indicator across cities and days of the week.
#     """)

#     st.markdown(f'## {badge("Objectives", "orange")}', unsafe_allow_html=True)
#     st.markdown("""
#     - Clean and prepare raw weather data for analysis
#     - Explore distributions of temperature, humidity, and weather conditions
#     - Identify relationships between weather variables (temp, dew, humidity,
#     UV index, solar energy, pressure, cloud cover)
#     - Test whether weather **severity** is associated with **health risk**
#     - Compare weather patterns across cities and days of the week
#     """)

#     st.markdown(f'## {badge("Dataset Summary", "green")}', unsafe_allow_html=True)
#     col1, col2, col3 = st.columns(3)
#     col1.metric("Records", "1,000")
#     col2.metric("Cities", "10")
#     col3.metric("Time Period", "Sep 2024")

#     st.markdown(f'## {badge("Data Cleaning Steps", "purple")}', unsafe_allow_html=True)
#     st.markdown("""
#     - Removed columns with heavy missing data: `preciptype` (622 missing),
#     `snowdepth` (71 missing), `Condition_Code`
#     - Dropped redundant/low-value columns: `tempmax`, `tempmin`,
#     `feelslikemax/min`, `sunriseEpoch`, `sunsetEpoch`, `windgust`,
#     `precipprob`, `precipcover`, `stations`, `source`, `windspeed`, `winddir`
#     - Verified no duplicate records
#     - Flagged data quality anomalies (e.g. negative UV index / precipitation
#     values, indicating the dataset is likely synthetic/simulated)
#     """)

#     st.markdown(f'## {badge("Techniques Used", "pink")}', unsafe_allow_html=True)
#     st.markdown("""
#     - **Univariate analysis:** histograms, bar charts, pie charts
#     - **Bivariate analysis:** scatter plots, line plots, box plots, violin plots
#     - **Multivariate analysis:** grouped bar/count plots, catplots, pairplot
#     - **Correlation analysis:** heatmap of temp, humidity, dew, UV index,
#     severity score
#     - **Statistical testing:** Pearson correlation between severity score
#     and health risk score
#     """)

#     st.markdown(f'## {badge("Tools & Libraries", "blue")}', unsafe_allow_html=True)
#     st.markdown("""
#     `pandas` · `numpy` · `seaborn` · `matplotlib` · `scipy` · `streamlit`
#     """)

#     st.markdown(f'## {badge("Key Limitations", "red")}', unsafe_allow_html=True)
#     st.markdown("""
#     - Data spans only **one month/season** (September 2024, Fall), so no
#     seasonal or year-over-year comparison is possible
#     - Class imbalance in `conditions` (57% Clear) and `day_of_week`
#     (Saturday overrepresented)
#     - Some fields show physically implausible values, suggesting simulated
#     rather than real observed data
#     """)




                

        


    
   
import streamlit as st 
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 


from streamlit_option_menu import option_menu 
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

st.set_page_config(page_title="Urban air quality and health analysis",page_icon="🌍",layout="wide")

# ============================================================
# 🎨 GLOBAL PLOTLY THEME — no white plot background / white gridlines,
# so data never blends into the page or disappears.
# ============================================================
_custom_template = go.layout.Template()
_custom_template.layout = go.Layout(
    paper_bgcolor="rgba(0,0,0,0)",   # transparent -> shows the card behind it
    plot_bgcolor="#eef3f7",          # light blue-grey, never plain white
    font=dict(color="#1f3b4d", size=16),
    title=dict(font=dict(size=22, color="#1f3b4d")),
    legend=dict(font=dict(size=14)),
    xaxis=dict(gridcolor="#c7d2db", zerolinecolor="#c7d2db", linecolor="#8a97a3",
               title=dict(font=dict(size=16)), tickfont=dict(size=13)),
    yaxis=dict(gridcolor="#c7d2db", zerolinecolor="#c7d2db", linecolor="#8a97a3",
               title=dict(font=dict(size=16)), tickfont=dict(size=13)),
    colorway=["#2E6F95", "#E8743B", "#5FA777", "#C44E52", "#8172B2",
              "#937860", "#DA8BC3", "#8C8C8C", "#CCB974", "#64B5CD"],
)
pio.templates["dashboard"] = _custom_template
pio.templates.default = "dashboard"

# ============================================================
# 🎨 CUSTOM CSS — colorful headers, cards, tabs, badges
# ============================================================
CUSTOM_CSS = """
<style>
:root{
    --primary:#2E6F95;
    --secondary:#E8743B;
    --tertiary:#5FA777;
    --purple:#8172B2;
    --pink:#DA8BC3;
    --gold:#CCB974;
    --red:#C44E52;
}

/* ------------------------------------------------------------
   READABILITY: scale up the root font size. Streamlit's own
   widgets are sized in rem, so this alone enlarges badges,
   metric cards, headers, and body text together proportionally.
   Everything below adds explicit bumps for the few elements
   (tables, code blocks, tabs) that don't fully inherit it.
   ------------------------------------------------------------ */
html{
    font-size: 19px;
}

/* Page background */
.stApp{
    background: linear-gradient(180deg, #f7f9fc 0%, #ffffff 35%);
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background: linear-gradient(180deg, #123a52 0%, #2E6F95 100%);
}
section[data-testid="stSidebar"] * { color:#f2f6fa !important; font-size:1.05rem !important; }
section[data-testid="stSidebar"] .nav-link { font-size:1.15rem !important; padding:12px 10px !important; }

/* Gradient page titles (h1) */
h1{
    background: linear-gradient(90deg, var(--primary), var(--tertiary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 800 !important;
    font-size: 2.6rem !important;
}

/* Sub-headers (h2, h3) get a colored left bar */
h2, h3{
    color:#1f3b4d !important;
    border-left: 6px solid var(--secondary);
    padding-left: 12px;
}
h2{ font-size: 1.9rem !important; }
h3{ font-size: 1.5rem !important; }

/* st.metric cards */
div[data-testid="stMetric"]{
    background: #ffffff;
    border: 1px solid #e5e9ef;
    border-left: 6px solid var(--primary);
    border-radius: 12px;
    padding: 14px 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
div[data-testid="stMetricLabel"]{ color: var(--primary) !important; font-weight:600; font-size:1.05rem !important; }
div[data-testid="stMetricValue"]{ color:#1f3b4d !important; font-size:2rem !important; }

/* Tabs */
button[data-baseweb="tab"]{
    font-weight:600;
    color:#5a6b78;
    font-size:1.1rem !important;
}
button[data-baseweb="tab"] p{ font-size:1.1rem !important; }
button[data-baseweb="tab"][aria-selected="true"]{
    color: var(--secondary) !important;
    border-bottom: 3px solid var(--secondary) !important;
}

/* Expander */
details{
    border: 1px solid #e5e9ef;
    border-radius: 10px;
    background:#fbfcfe;
}
details summary{ font-size:1.1rem !important; }

/* Colored inline text helpers */
.badge{
    display:inline-block;
    padding:5px 14px;
    border-radius:999px;
    font-weight:700;
    font-size:1rem;
    color:white;
    margin-right:6px;
}
.badge-blue{ background: var(--primary); }
.badge-orange{ background: var(--secondary); }
.badge-green{ background: var(--tertiary); }
.badge-purple{ background: var(--purple); }
.badge-pink{ background: var(--pink); }
.badge-red{ background: var(--red); }

.highlight-box{
    border-radius: 12px;
    padding: 18px 22px;
    margin: 10px 0;
    color: white;
    font-size: 1.15rem;
    line-height:1.6;
}
.box-blue{ background: linear-gradient(135deg, #2E6F95, #4a95bd); }
.box-orange{ background: linear-gradient(135deg, #E8743B, #f0a274); }
.box-green{ background: linear-gradient(135deg, #5FA777, #86c79c); }
.box-purple{ background: linear-gradient(135deg, #8172B2, #a99bd1); }

.finding-title{
    font-size:1.6rem;
    font-weight:800;
    color:#1f3b4d;
}

/* Chart & dataframe cards — never plain white, so plotted data stays visible */
div[data-testid="stPlotlyChart"]{
    background:#eef3f7;
    border-radius: 14px;
    padding: 10px;
    border: 1px solid #d8e0e8;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}
div[data-testid="stDataFrame"], div[data-testid="stDataEditor"]{
    background:#eef3f7;
    border-radius: 12px;
    padding: 6px;
    border: 1px solid #d8e0e8;
}
/* Dataframe/table cell + header text was rendering tiny by default */
div[data-testid="stDataFrame"] *, div[data-testid="stDataEditor"] *{
    font-size:1rem !important;
}

/* st.code() / st.text() blocks (e.g. df.info() output) */
div[data-testid="stCodeBlock"] code, div[data-testid="stCodeBlock"] pre{
    font-size:1rem !important;
    line-height:1.5 !important;
}

/* st.slider label / value text */
div[data-testid="stSlider"] label, div[data-testid="stSlider"] * {
    font-size:1.05rem !important;
}

/* ------------------------------------------------------------
   FIX: Streamlit's dark-theme default text color (light grey)
   was leaking through on plain paragraphs / bullet lists / labels,
   making them nearly invisible against our light page background.
   Force dark, readable text everywhere in the main content area.
   ------------------------------------------------------------ */
[data-testid="stAppViewContainer"] p,
[data-testid="stAppViewContainer"] li,
[data-testid="stAppViewContainer"] span,
[data-testid="stAppViewContainer"] label,
[data-testid="stAppViewContainer"] div[data-testid="stMarkdownContainer"],
[data-testid="stAppViewContainer"] div[data-testid="stText"],
[data-testid="stAppViewContainer"] div[data-testid="stMetricLabel"] p,
[data-testid="stAppViewContainer"] div[data-testid="stCaptionContainer"]{
    color:#1f3b4d !important;
    font-size:1.08rem !important;
    line-height:1.6 !important;
}

/* Re-assert white text inside colored badges / highlight boxes
   (must come AFTER the rule above so it wins the cascade) */
.badge, .badge *{ color:#ffffff !important; }
.highlight-box, .highlight-box *{ color:#ffffff !important; }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

def colored_header(text, subtitle=None, color="var(--primary)", icon=""):
    """Render a vibrant gradient-style header with an optional subtitle."""
    st.markdown(
        f"""
        <div style="margin-bottom:14px;">
            <div style="font-size:2.4rem; font-weight:800; color:{color};">{icon} {text}</div>
            {f'<div style="font-size:1.25rem; color:#5a6b78; margin-top:2px;">{subtitle}</div>' if subtitle else ''}
        </div>
        """,
        unsafe_allow_html=True,
    )

def badge(text, kind="blue"):
    return f'<span class="badge badge-{kind}">{text}</span>'

def highlight_box(text, kind="blue"):
    st.markdown(f'<div class="highlight-box box-{kind}">{text}</div>', unsafe_allow_html=True)

df=pd.read_csv("aird.csv")

with st.sidebar:
    st.sidebar.title("🌍Current air metrics")
    selected=option_menu(menu_title="Main Menu",options=["Home","Data-set","Processing","Graphs","Findings","About"],icons=["house","table","bar-chart","house","house","person"],default_index=0)

if selected=="Home":

    colored_header(
        "Weather & Health Risk Dashboard",
        subtitle="Welcome to your automated weather analytics and risk visualization platform!",
        icon="🏠",
    )
    st.markdown(
        f"{badge('Live Data', 'green')}{badge('Python', 'blue')}{badge('Streamlit', 'orange')}{badge('Plotly', 'purple')}",
        unsafe_allow_html=True,
    )
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

    # 3. Populate columns with colorful metric cards

    def metric_card(icon, label, value, kind):
        st.markdown(
            f"""
            <div class="highlight-box box-{kind}" style="text-align:center;">
                <div style="font-size:2.1rem;">{icon}</div>
                <div style="font-size:1.05rem; opacity:0.9;">{label}</div>
                <div style="font-size:1.9rem; font-weight:800;">{value}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col1:
        metric_card("💧", "Total Rain", f"{total_precip:.2f} mm", "blue")

    with col2:
        metric_card("☀️", "Max UV Index", int(max_uv), "orange")

    with col3:
        metric_card("☁️", "Avg Humidity", f"{avg_humidity:.0f}%", "green")

    with col4:
        metric_card("⚠️", "Max Severity", f"{max_severity:.1f}", "purple")


        
    st.markdown("### 🚀 Quick Start Guide")
    st.markdown(
        f'{badge("Step 1", "blue")} Open the **📂 Dataset View** in the sidebar to review raw log information and summaries.',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'{badge("Step 2", "orange")} Navigate to **⚙️ Graph Processing** to customize filters and render interactive graphs.',
        unsafe_allow_html=True,
    )


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
        color_discrete_sequence=["#2E6F95", "#E8743B", "#5FA777", "#C44E52", "#8172B2", "#CCB974"]
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
                

            

     # ============================================================
    # Add this once, right after your existing CUSTOM_CSS block
    # (near the top of the file, before df=pd.read_csv(...))
    # ============================================================
    STABLE_COLUMNS_CSS = """
    <style>
    /* Force st.columns to always stay side-by-side, never stack */
    div[data-testid="stHorizontalBlock"]{
        flex-wrap: nowrap !important;
        align-items: stretch !important;
        gap: 1rem;
    }
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]{
        min-width: 0 !important;   /* lets columns shrink instead of wrapping */
    }

    /* Vertically center whatever sits inside the "text" column */
    .side-text-wrap{
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    </style>
    """
    st.markdown(STABLE_COLUMNS_CSS, unsafe_allow_html=True)


# ============================================================
# t2 — Categorical Breakdown (city + day-of-week combo charts)
# ============================================================
    with t2:
        st.header("2. Categorical Breakdown")

        from plotly.subplots import make_subplots
        import plotly.graph_objects as go

        # --- Records per City + Average Health Risk per City ---
        city_stats = (
            df1.groupby("city")
            .agg(count=("city", "size"), avg_health_risk=("health_risk_score", "mean"))
            .reset_index()
            .sort_values("count", ascending=False)
        )

        col_chart, col_text = st.columns([2.2, 1])

        with col_chart:
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            fig.add_trace(
                go.Bar(x=city_stats["city"], y=city_stats["count"], name="Record Count",
                       marker_color=PRIMARY),
                secondary_y=False,
            )
            fig.add_trace(
                go.Scatter(x=city_stats["city"], y=city_stats["avg_health_risk"], name="Avg Health Risk",
                           mode="lines+markers", line=dict(color=SECONDARY, width=3),
                           marker=dict(size=8)),
                secondary_y=True,
            )
            fig.update_layout(title="Records per City vs Average Health Risk",
                               legend=dict(orientation="h", y=1.12), height=480)
            fig.update_yaxes(title_text="Record Count", secondary_y=False)
            fig.update_yaxes(title_text="Avg Health Risk Score", secondary_y=True)
            st.plotly_chart(fig, use_container_width=True)

        with col_text:
            st.markdown('<div class="side-text-wrap">', unsafe_allow_html=True)
            highlight_box(
                "🏙️ <b>What this shows:</b> Bars tell you how many records came from each "
                "city, while the orange line tracks average health risk for that same city — "
                "so you can spot if a city with fewer records still carries higher risk.",
                "blue",
            )
            st.markdown(f"{badge('City-wise', 'blue')}", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # --- Records by Day of Week + Average Temperature per Day ---
        dow_stats = (
            df1.groupby("day_of_week")
            .agg(count=("day_of_week", "size"), avg_temp=("temp", "mean"))
            .reindex(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
            .reset_index()
        )

        col_chart, col_text = st.columns([2.2, 1])

        with col_chart:
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            fig.add_trace(
                go.Bar(x=dow_stats["day_of_week"], y=dow_stats["count"], name="Record Count",
                       marker_color=PRIMARY),
                secondary_y=False,
            )
            fig.add_trace(
                go.Scatter(x=dow_stats["day_of_week"], y=dow_stats["avg_temp"], name="Avg Temperature",
                           mode="lines+markers", line=dict(color=TERTIARY, width=3),
                           marker=dict(size=8)),
                secondary_y=True,
            )
            fig.update_layout(title="Records by Day of Week vs Average Temperature",
                               legend=dict(orientation="h", y=1.12), height=480)
            fig.update_yaxes(title_text="Record Count", secondary_y=False)
            fig.update_yaxes(title_text="Avg Temperature", secondary_y=True)
            st.plotly_chart(fig, use_container_width=True)

        with col_text:
            st.markdown('<div class="side-text-wrap">', unsafe_allow_html=True)
            highlight_box(
                "📅 <b>What this shows:</b> Bars show how many records fall on each day, "
                "while the green line tracks that day's average temperature — useful for "
                "checking whether the oversampled day (Saturday) also happens to run hotter "
                "or cooler than the rest.",
                "green",
            )
            st.markdown(f"{badge('Day-wise', 'green')}", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

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

            # --- Severity Score vs Health Risk Score ---
            col_chart, col_text = st.columns([2.2, 1])

            with col_chart:
                fig = px.scatter(
                    df1, x="severity_score", y="health_risk_score",
                    color_discrete_sequence=[PRIMARY],
                    hover_data=["city", "datetime"],
                    title="Severity Score vs Health Risk Score",
                )
                st.plotly_chart(fig, use_container_width=True)

            with col_text:
                st.markdown("<div style='padding-top:2.5rem;'></div>", unsafe_allow_html=True)
                highlight_box(
                    "📈 <b>What this shows:</b> As weather gets more severe, health risk "
                    "goes up too. The dots climb from bottom-left to top-right, which means "
                    "the two are closely linked — worse weather generally means higher risk "
                    "to health.",
                    "blue",
                )
                st.markdown(f"{badge('Bivariate', 'blue')}", unsafe_allow_html=True)

            # --- Temperature vs Solar Energy, colored by city ---
            col_chart, col_text = st.columns([2.2, 1])

            with col_chart:
                fig = px.scatter(
                    df1, x="temp", y="solarenergy", color="city",
                    color_discrete_sequence=CITY_PALETTE,
                    hover_data=["datetime", "humidity"],
                    title="Temperature vs Solar Energy",
                )
                st.plotly_chart(fig, use_container_width=True)

            with col_text:
                st.markdown("<div style='padding-top:2.5rem;'></div>", unsafe_allow_html=True)
                highlight_box(
                    "🏙️ <b>What this shows:</b> Temperature alone doesn't explain solar "
                    "energy — instead, each city sticks to its own band. Phoenix stays high "
                    "and hot, Chicago stays low and cool. So the city you're in matters more "
                    "than the day's temperature.",
                    "purple",
                )
                st.markdown(f"{badge('Multivariate', 'orange')}", unsafe_allow_html=True)
    
        
            cols = ["temp", "humidity", "dew", "uvindex", "pressure", "cloudcover",
                    "severity_score", "health_risk_score"]
            corr = df1[cols].corr()
            fig = px.imshow(
                corr, text_auto=".2f", color_continuous_scale="RdBu_r",
                title="Correlation Heatmap",
            )
            fig.update_traces(hovertemplate="%{x} vs %{y}<br>corr = %{z:.2f}<extra></extra>")
            st.plotly_chart(fig, use_container_width=True)

            highlight_box(
                "🔗 <b>Correlation Drivers:</b> The correlation heatmap shows which weather variables move together "
                "with the health risk score — use it to spot what's actually driving risk (usually temperature and "
                "UV index rather than pressure or cloud cover).",
                "blue",
            )

    

    with t4:
        st.header("4. Trends Over Time")

        daily_temp = df1.groupby(["datetime", "city"])["temp"].mean().reset_index()
        fig = px.line(
            daily_temp, x="datetime", y="temp", color="city",
            color_discrete_sequence=CITY_PALETTE, markers=True,
            hover_data={"temp": ":.1f"}, title="Average Daily Temperature by City",
        )
        st.plotly_chart(fig, use_container_width=True)

        highlight_box(
            "🌡️ <b>Temperature Extremes:</b> Phoenix and Dallas sit at the hot end of the temperature range, "
            "while cities like San Jose and San Diego stay milder.",
            "orange",
        )

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
    
        highlight_box(
            "🧩 <b>Risk Synergy:</b> The 3D plot lets you rotate and explore whether high temperature "
            "<i>and</i> high humidity together push the health risk score up more than either one alone.",
            "purple",
        )
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
        highlight_box(
            "🌆 <b>Condition Breakdown:</b> The sunburst chart makes it easy to see, city by city, which weather "
            "condition is most common and whether that condition carries a higher average health risk.",
            "green",
        )
####
elif selected=="Findings":

    colored_header("Weather and Health Risk Analytics", subtitle="Key Insights", icon="🔎")

    t1,t2,=st.tabs(["🔵 First finding","🟠 Second finding"])
    
    with t1:
        st.markdown(f'<div class="finding-title">{badge("Finding 1", "orange")} </div>', unsafe_allow_html=True)
        st.image("s2.png")
    with t2:
        st.markdown(f'<div class="finding-title">{badge("Finding 2", "green")} </div>', unsafe_allow_html=True)
        st.image("s3.png")
    


elif selected=="About":
    st.header("About")
    # st.write("""
    # This is a simple weather data dashboard project made using Python.

    # **Libraries used:**
    # - Pandas and NumPy for data handling
    # - Matplotlib and Seaborn for graphs
    # - Plotly for interactive 3D and sunburst charts
    # - Streamlit for building the web app 
    #     """)
     
    

    # def about_page():
    #     st.title("ℹ️ About This Project")

    st.markdown(f'## {badge("Overview", "blue")}', unsafe_allow_html=True)
    st.write("""
    This project analyzes a weather dataset covering **1,000 daily records**
    across **10 major U.S. cities** — Chicago, New York City, Phoenix, Dallas,
    Philadelphia, Los Angeles, San Diego, San Jose, Houston, and San Antonio —
    for **September 2024 (Fall season)**. The goal is to explore weather
    patterns, temperature behavior, and their relationship to a derived
    health-risk indicator across cities and days of the week.
    """)

    st.markdown(f'## {badge("Objectives", "orange")}', unsafe_allow_html=True)
    st.markdown("""
    - Clean and prepare raw weather data for analysis
    - Explore distributions of temperature, humidity, and weather conditions
    - Identify relationships between weather variables (temp, dew, humidity,
    UV index, solar energy, pressure, cloud cover)
    - Test whether weather **severity** is associated with **health risk**
    - Compare weather patterns across cities and days of the week
    """)

    st.markdown(f'## {badge("Dataset Summary", "green")}', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("Records", "1,000")
    col2.metric("Cities", "10")
    col3.metric("Time Period", "Sep 2024")

    st.markdown(f'## {badge("Data Cleaning Steps", "purple")}', unsafe_allow_html=True)
    st.markdown("""
    - Removed columns with heavy missing data: `preciptype` (622 missing),
    `snowdepth` (71 missing), `Condition_Code`
    - Dropped redundant/low-value columns: `tempmax`, `tempmin`,
    `feelslikemax/min`, `sunriseEpoch`, `sunsetEpoch`, `windgust`,
    `precipprob`, `precipcover`, `stations`, `source`, `windspeed`, `winddir`
    - Verified no duplicate records
    - Flagged data quality anomalies (e.g. negative UV index / precipitation
    values, indicating the dataset is likely synthetic/simulated)
    """)

    st.markdown(f'## {badge("Techniques Used", "pink")}', unsafe_allow_html=True)
    st.markdown("""
    - **Univariate analysis:** histograms, bar charts, pie charts
    - **Bivariate analysis:** scatter plots, line plots, box plots, violin plots
    - **Multivariate analysis:** grouped bar/count plots, catplots, pairplot
    - **Correlation analysis:** heatmap of temp, humidity, dew, UV index,
    severity score
    - **Statistical testing:** Pearson correlation between severity score
    and health risk score
    """)

    st.markdown(f'## {badge("Tools & Libraries", "blue")}', unsafe_allow_html=True)
    st.markdown("""
    `pandas` · `numpy` · `seaborn` · `matplotlib` · `scipy` · `streamlit`
    """)

    st.markdown(f'## {badge("Key Limitations", "red")}', unsafe_allow_html=True)
    st.markdown("""
    - Data spans only **one month/season** (September 2024, Fall), so no
    seasonal or year-over-year comparison is possible
    - Class imbalance in `conditions` (57% Clear) and `day_of_week`
    (Saturday overrepresented)
    - Some fields show physically implausible values, suggesting simulated
    rather than real observed data
    """)




                

        


    
   
