from main import Generate, Load
import greedy
import aco
import plotly.graph_objects as go
import subprocess
import os

instances = []
result_greedy = []
result_aco = []

file = open("./greedy_vs_aco.txt", "r")

line = file.readline().split(",")
instances = [float(num) for num in line]
line = file.readline().split(",")
result_greedy = [round(float(num), 2) for num in line]
line = file.readline().split(",")
result_aco = [float(num) for num in line]
file.close()

fig = go.Figure()
fig.add_trace(go.Bar(
    x=instances,
    y=result_greedy,
    # texttemplate="%{y}",
    # textposition="auto",
    # textangle=270,
    name="Greedy Algoritm"
))
fig.add_trace(go.Bar(
    x=instances,
    y=result_aco,
    # texttemplate="%{y}",
    # textposition="auto",
    # textangle=270,
    # textfont_size=100,

    name="Ant Colony Optimization"
))
for i in range(15):
    fig.add_annotation(
        x=instances[i], y=result_greedy[i],
        text=result_greedy[i],
        font=dict(
            size=18
        ),
        showarrow=True,
        textangle=90,
        xshift=-5,
        yshift=10
    )
    fig.add_annotation(
        x=instances[i], y=result_aco[i],
        text=result_aco[i],
        font=dict(
            size=18
        ),
        showarrow=True,
        textangle=90,
        xshift=25,
        yshift=10
    )
fig.update_layout(barmode='group', title_text="Greedy vs ACO")
# fig.update_xaxes(type='category')
fig.show()

# for instance in instances:
#     print(instance)
#     cities = Generate(size=instance, filename="input")
#     distance, path, coordinates = greedy.main(cities)
#     result_greedy.append(distance)
#     print("Greedy: ", distance)

#     FNULL = open(os.devnull, 'w')
#     args = "aco.exe {} {} {} {} {} {}".format("./data/input.txt", 2000, 
#         1000000, 1.0, 
#         12.0, 0.6)
#     subprocess.call(args, shell=False)
#     file = open("./output.txt", "r")
#     distance = float(file.readline())
#     result_aco.append(distance)
#     print("ACO: ", distance)

# print(instances,"\n\n\n")
# print(result_greedy,"\n\n\n")
# print(result_aco,"\n\n\n")