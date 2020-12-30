import plotly.express as px
import plotly.graph_objects as go

def generateInteractiveGraph(x, y, path, file="./static/file.html"):
    fig = go.Figure(go.Scatter(x=x, y=y, 
        mode="lines+markers", marker=dict(color=[0]),
        text=path,
        textposition="top center"
    ))
    fig.write_html(file)