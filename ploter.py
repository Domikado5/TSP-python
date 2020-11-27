import plotly.express as px
import plotly.graph_objects as go

def generateInteractiveGraph(x, y):
    fig = go.Figure(go.Scatter(x=x, y=y))
    fig.write_html("./static/file.html")
    