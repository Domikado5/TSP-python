import plotly.graph_objects as go
file = open("./benchmarks.txt", "r")

line = file.readline().split(",")
instances = [num for num in line]
line = file.readline().split(",")
best = [float(num) for num in line]
line = file.readline().split(",")
result_aco = [float(num) for num in line]
file.close()

relative_error = [ round((abs(best[i] - result_aco[i])/best[i])*100, 2) for i in range(10)]

fig = go.Figure()
fig.add_trace(go.Bar(
    x=instances,
    y=best,
    # texttemplate="%{y}",
    # textposition="auto",
    # textangle=270,
    name="Best known solution"
))
fig.add_trace(go.Bar(
    x=instances,
    y=result_aco,
    # text=relative_error,
    # textposition="inside",
    # # textangle=270,
    # textfont_size=20,

    name="Ant Colony Optimization"
))
for i in range(10):
    fig.add_annotation(
        x=instances[i], y=best[i],
        text=best[i],
        font=dict(
            size=18
        ),
        showarrow=True,
        arrowhead=5,
        textangle=0,
        xshift=-25,
        yshift=10
    )
    fig.add_annotation(
        x=instances[i], y=result_aco[i],
        text=result_aco[i],
        font=dict(
            size=18
        ),
        showarrow=True,
        arrowhead=5,
        textangle=0,
        xshift=40,
        yshift=10
    )
    fig.add_annotation(
        x=instances[i], y=result_aco[i],
        text=str(relative_error[i])+'%',
        font=dict(
            size=18
        ),
        showarrow=False,
        textangle=0,
        xshift=40,
        yshift=60
    )
fig.update_layout(barmode='group', title_text="Benchmark")
# fig.update_xaxes(type='category')
fig.show()