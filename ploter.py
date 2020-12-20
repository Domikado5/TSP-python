import plotly.express as px
import plotly.graph_objects as go

def generateInteractiveGraph(x, y, path):
    fig = go.Figure(go.Scatter(x=x, y=y, 
        mode="lines+markers", marker=dict(color=[0]),
        text=path
    ))
    fig.write_html("./static/file.html")
    