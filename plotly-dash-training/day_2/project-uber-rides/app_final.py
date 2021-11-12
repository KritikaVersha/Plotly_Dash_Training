# Step 1: Import your libraries




# Step 2: Create an instance of Dash app
app = 

# Step 3: Add an app title
app.title = 

# Step4: Create an instance of server
server = 

# Step 5: Read the data from different csv files and combine them into one dataframe
# Initialize data frame
df1 = pd.read_csv("",dtype=object,)
df2 = pd.read_csv("",dtype=object,)
df3 = pd.read_csv("",dtype=object,)
df = pd.concat([], axis=0)
df["Date/Time"] = pd.to_datetime(df["Date/Time"], format="%Y-%m-%d %H:%M")
dfs = dict(tuple(df.groupby(df['Date/Time'].dt.date)))
df.index = df["Date/Time"]
print(df.head)

# Step 6: Read Plotly mapbox object token for scattermapbox access
mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A"


# Step 7: Create a dictionary of important locations in New York
list_of_locations = {
    "Madison Square Garden": {"lat": 40.7505, "lon": -73.9934},
    "Yankee Stadium": {"lat": 40.8296, "lon": -73.9262},
    "Empire State Building": {"lat": 40.7484, "lon": -73.9857},
    "New York Stock Exchange": {"lat": 40.7069, "lon": -74.0113},
    "JFK Airport": {"lat": 40.644987, "lon": -73.785607},
    "Grand Central Station": {"lat": 40.7527, "lon": -73.9772},
    "Times Square": {"lat": 40.7589, "lon": -73.9851},
    "Columbia University": {"lat": 40.8075, "lon": -73.9626},
    "United Nations HQ": {"lat": 40.7489, "lon": -73.9680},
}

# Step 8: Update the attributes for each component inside your layout
app.layout = html.Div(
    children=[

            # Column for menu selectors
            html.Div(
                className="row",
                children=[
                            
                    html.H2(""), #Update
                    html.P(
                            """ """ #Update
                        ),
                    html.Div(
                            className="div-for-dropdown",
                            children=[
                                dcc.DatePickerSingle(
                                    id="date-picker",
                                    min_date_allowed=, #Update
                                    max_date_allowed=, #Update
                                    initial_visible_month=, #Update
                                    date=dt(2014, 4, 1).date(),
                                    display_format="MMMM D, YYYY"                                    
                                )
                            ],
                        ),
                        # Change to side-by-side for mobile layout
                        html.Div(
                            className="row",
                            children=[
                                html.Div(
                                    className="div-for-dropdown",
                                    children=[
                                        # Dropdown for locations on map
                                        dcc.Dropdown(
                                            id="location-dropdown",
                                            options=[{"label": i, "value": i} for i in ], #Update
                                            placeholder="Select a location"   
                                        )
                                    ],
                                ),
                                html.Div(
                                    className="div-for-dropdown",
                                    children=[
                                        # Dropdown to select times
                                        dcc.Dropdown(
                                            id="bar-selector",
                                            options=[{"label": str(n) + ":00", "value": str(n),}  for n in range(24) ],
                                            multi=True,
                                            placeholder="Select certain hours"
                                        )
                                    ],
                                ),
                            ],
                        ),
                        html.P(id=""),  #Update
                        html.P(id=""),  #Update
                        html.P(id=""),  #Update                
                ],
                style={"border": "0px solid black",
                        "padding-top": "12px",
                        "padding-bottom": "12px",
                        "float": "", #Update
                        "width": "30%"
                    }
            ),

            # Column for app graphs and plots
                html.Div(
                    className="eight columns div-for-charts bg-grey",
                    children=[
                        dcc.Graph(id="map-graph"),
                        html.Div(
                            className="text-padding",
                            children=[
                                "Ride histogram"
                            ],
                        ),
                        dcc.Graph(id="histogram"),
                    ],
                    style={
                        "display": "flex",
                        "flex-direction": "", #Update
                        "height": "80vh",
                        "width": "60%"
                    }
                ),
            ]
        )


# # Callback function 1: Update the total number of rides Tag
# @app.callback(Output("", ""), [Input("date-picker", "date")]) # Update by adding output to callback
# def update_total_rides(): # Update by passing parameter
#     date_picked = dt.strptime(datePicked, "%Y-%m-%d")
#     return "Total Number of rides: {:,d}".format( 
#         # Update by returning the total ride count

#     )

# # Callback function 2: Update the total number of rides in selected times
# @app.callback(
#     # Pass the list of input and output components inside the callback decorator
# )
# def update_total_rides_selection(datePicked, selection):
#     firstOutput = ""
#     date_picked = dt.strptime(datePicked, "%Y-%m-%d")
#     df_day = # Update: Use dfs to select the dataframe matching with the date picked by the user
#     if selection != None:
#         selection = list(map(int, selection))
#         ride_count = 0
#         if df_day.shape[0] > 0:
#             for hr in selection:
#                 start_time = date_picked + timedelta(hours=hr)
#                 end_time = date_picked + timedelta(hours=hr+1)
#                 df_hour = df_day[(df_day['Date/Time'] > start_time) & (df_day['Date/Time'] < end_time)]
#                 ride_count += df_hour.shape[0]
#         firstOutput = "Total rides at selected hours (inclusive of all locations): {:,d}".format() # Return ride count for the hour selected

#     if (datePicked == None or selection == None or len(selection) == 24 or len(selection) == 0):
#         return firstOutput, (, " - showing hour(s): All") # Update: If user does not select hours in the dropdown, display data for all hours in the day

#     # holder: fetches the hour selected by the user from the dropdown and sorts it
#     holder = sorted([int(x) for x in selection]) 

#     if holder == list(range(min(holder), max(holder) + 1)):
#         return (
#             firstOutput,
#             (datePicked," - showing hour(s): ", holder[0],"-",holder[len(holder) - 1],),
#         )

#     holder_to_string = ", ".join(str(x) for x in holder)
#     return firstOutput, (datePicked, " - showing hour(s): ", ) # Update: Update the return value with holder_to_string variable


# # Callback function 3: Update histogram figure based on date and time selected from the dropdown
# @app.callback(
# # Update the callback function by adding input and output component id
# )
# def update_histogram(datePicked, hour_value, hist_clicks):
#     date_picked = dt.strptime(datePicked, "%Y-%m-%d")
#     df_day = dfs[date_picked.date()]
#     df_day['Date/Time'] = df_day['Date/Time'].astype('datetime64[h]')

#     colorVal = {0:"#F4EC15",1:"#DAF017",2:"#BBEC19",3:"#9DE81B",4:"#80E41D",5:"#66E01F",6:"#4CDC20",7:"#34D822",
#     8:"#24D249",9:"#25D042",10:"#26CC58",11:"#28C86D",12:"#29C481",13:"#2AC093",14:"#2BBCA4",15:"#2BB5B8",
#     16:"#2C99B4",17:"#2D7EB0",18:"#2D65AC",19:"#2E4EA4",20:"#2E38A4",21:"#3B2FA0",22:"#4E2F9C",23:"#603099"}

    
#     selected_hours = []
#     if hour_value is not None:
#         selected_hours.extend(hour_value)
#         for hour in hour_value:
#             colorVal[int(hour)] = "" # Update the colorVar dictionary by changing the color to white for selected hour in the dropdown

#     #Update print hist_clicks        
#     if hist_clicks is not None:
#         click_event = hist_clicks['points'][0]
#         x_event = strptime(click_event['x'], "%Y-%m-%d %H:%M")
#         selected_hours.append(str(x_event.tm_hour))
#         #selected_hours = [str(x_event.tm_hour)]
#         colorVal[x_event.tm_hour] = "" # Update the colorVar dictionary by changing the color to white for user clicked hour in the graph

#     fig = px.histogram(df_day, x="Date/Time", color = df_day['Date/Time'].dt.hour, color_discrete_map=colorVal)
#     #fig = px.histogram(df_day, x="Date/Time", color = df_day['Date/Time'].dt.hour, color_discrete_sequence=px.colors.sequential.Viridis_r)
#     #df_hist = df_day.groupby([pd.Grouper(key='Date/Time',freq='H')]).size().reset_index(name='count')
#     #fig = px.bar(df_hist, x='Date/Time', y='count', color = df_hist['Date/Time'].dt.hour , color_continuous_scale=px.colors.sequential.Viridis_r)
#     #fig.update_traces(marker_color='red')
    
#     return(fig, list(set(selected_hours)))


# # Callback function 4: Update Map Graph based on date-picker, selected data on histogram and location dropdown
# @app.callback(
#     Output("map-graph", "figure"),
#     [
#         Input("date-picker", "date"),
#         Input("bar-selector", "value"),
#         Input("location-dropdown", "value"),
#     ],
# )
# def update_graph(datePicked, selectedData, selectedLocation):
#     zoom = 
#     latInitial = # Update
#     lonInitial = # Update
#     bearing = # Update

#     if selectedLocation:
#         zoom = # Update
#         latInitial = list_of_locations[selectedLocation][""] # Use list_of_locations dictionary to feed the scattermapbox with latitude of the selected location
#         lonInitial = list_of_locations[selectedLocation][""] # Use list_of_locations dictionary to feed the scattermapbox with latitude of the selected location

#     date_picked = dt.strptime(datePicked, "%Y-%m-%d")
    
#     df_day = dfs[date_picked.date()]
#     if df_day.shape[0] > 0:
#         df_day['hour'] = df_day["Date/Time"].dt.hour
#         if selectedData != None:
#             df_hour = df_day[df_day['hour'].isin(selectedData)]
#         else:
#             df_hour = df_day
#         df_hour.index = df_hour["Date/Time"]

#     return go.Figure(
#         data=[
#             # Scattermapbox 1: Data for all rides based on date and time
#             Scattermapbox(
#                 lat= # Update,
#                 lon= # Update,
#                 mode="markers",
#                 hoverinfo="lat+lon+text",
#                 text= # Update,
#                 marker=dict(
#                     showscale=True,
#                     color=np.append(np.insert(df_hour.index.hour, 0, 0), 23),
#                     opacity=0.5,
#                     size=5,
#                     colorscale=[
#                         [0, "#F4EC15"],
#                         [0.04167, "#DAF017"],
#                         [0.0833, "#BBEC19"],
#                         [0.125, "#9DE81B"],
#                         [0.1667, "#80E41D"],
#                         [0.2083, "#66E01F"],
#                         [0.25, "#4CDC20"],
#                         [0.292, "#34D822"],
#                         [0.333, "#24D249"],
#                         [0.375, "#25D042"],
#                         [0.4167, "#26CC58"],
#                         [0.4583, "#28C86D"],
#                         [0.50, "#29C481"],
#                         [0.54167, "#2AC093"],
#                         [0.5833, "#2BBCA4"],
#                         [1.0, "#613099"],
#                     ],
#                     colorbar=dict(
#                         title="Time of<br>Day",
#                         x=0.93,
#                         xpad=0,
#                         nticks=24,
#                         tickfont=dict(color="#d8d8d8"),
#                         titlefont=dict(color="#d8d8d8"),
#                         thicknessmode="pixels",
#                     ),
#                 ),
#             ),
#             # Plot of important locations on the map
#             Scattermapbox(
#                 lat=[list_of_locations[i][""] for i in list_of_locations], # Update
#                 lon=[list_of_locations[i][""] for i in list_of_locations], # Update
#                 mode="markers",
#                 hoverinfo="text",
#                 text=[i for i in list_of_locations],
#                 marker=dict(size=8, color="#ffa0a0"),
#             ),
#         ],
#         layout=Layout(
#             autosize=True,
#             margin=go.layout.Margin(l=0, r=35, t=0, b=0),
#             showlegend=False,
#             mapbox=dict(
#                 accesstoken=, # Update with mapbox_access_token
#                 center=dict(lat=latInitial, lon=lonInitial),  # 40.7272  # -73.991251
#                 style="dark",
#                 bearing=bearing,
#                 zoom=zoom,
#             ),
#             updatemenus=[
#                 dict(
#                     buttons=(
#                         [
#                             dict(
#                                 args=[
#                                     {
#                                         "mapbox.zoom": 12,
#                                         "mapbox.center.lon": "-73.991251",
#                                         "mapbox.center.lat": "40.7272",
#                                         "mapbox.bearing": 0,
#                                         "mapbox.style": "dark",
#                                     }
#                                 ],
#                                 label="Reset Zoom",
#                                 method="relayout",
#                             )
#                         ]
#                     ),
#                     direction="left",
#                     pad={"r": 0, "t": 0, "b": 0, "l": 0},
#                     showactive=False,
#                     type="buttons",
#                     x=0.45,
#                     y=0.02,
#                     xanchor="left",
#                     yanchor="bottom",
#                     bgcolor="#323130",
#                     borderwidth=1,
#                     bordercolor="#6d6d6d",
#                     font=dict(color="#FFFFFF"),
#                 )
#             ],
#         ),
#     )

# if __name__ == "__main__":
#     app.run_server(debug=True)