from dash import Dash, dcc, html, Input, Output
import pandas as pd 
import plotly.express as px 
import seaborn as sns
import plotly.graph_objects as go



rDF = pd.read_csv("data/redWineDF.csv")

wDF = pd.read_csv("data/whiteWineDF.csv")



app = Dash(__name__)
server = app.server


app.layout = html.Div([
    html.Header("Graph Example (omfg it worked)", style={"fontSize":40,
                                        "textAlign":"center"}),
    dcc.Dropdown(id="csv-dropdown",
                 options=[
                     
                     {'label':'Red Wine','value':'Red Wine'},
                     {'label':'White Wine','value':'White Wine'}
                     ],
                 value = 'Red Wine',
                 style={"width":"50%","margin-left":"130px","margin-top":"60px"}),
    dcc.Graph(id="histogram")


])

@app.callback(Output('histogram',"figure"),
              Input('csv-dropdown',"value"))

def update_histogram(selected_csv):
    if selected_csv == 'Red Wine':
        data = rDF
    else:
        data = wDF
    fig = px.histogram(data,x='quality')
    return fig 


if __name__ == "__main__":
    app.run_server(debug=False)
