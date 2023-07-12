from dash import Dash, dcc, html, Input, Output
import pandas as pd 
import plotly.express as px 


rDF = pd.read_csv("../data/redWineDF.csv")

wDF = pd.read_csv("../data/whiteWineDF.csv")

app = Dash(__name__)


app.layout = html.Div([
    html.Header("Graph Example", style={"fontSize":40,
                                        "textAlign":"center"}),
    dcc.Dropdown(id="mydropdown",
                 options=rDF["quality"].unqiue(),
                 value = "6",
                 style={"width":"50%","margin-left":"130px","margin-top":"60px"}),
    dcc.Graph(id="scatter_plot")


])

@app.callback(Output("scatter_plot","figure"),
              Input("mydropdown","value"))

def sync_input(quality_selection):
    fig = px.scatter(rDF.loc[rDF["quality"]== quality_selection],
                     x="quality",
                     y="quality",
                     hover_name="Oshit it worked")
    return fig 


if __name__ == "__main__":
    app.run_server(debug=False)