# from main import Generate, Load
# import greedy
# import aco
import plotly.graph_objects as go
import subprocess
import os

instances = [
    './known-solutions/berlin52.txt',
    # './known-solutions/ch130.txt',
    # './known-solutions/ch150.txt',
    # './known-solutions/gil262.txt',
    # './known-solutions/rat99.txt',
    # './known-solutions/rat195.txt',
    # './known-solutions/rat575.txt',
    # './known-solutions/rat783.txt',
    # './known-solutions/st70.txt',
    # './known-solutions/tsp225.txt'
]
result_known = [
    7542,
    # 6110,
    # 6528,
    # 2378,
    # 1211,
    # 2323,
    # 6773,
    # 8806,
    # 675,
    # 3919
]
result_aco = []

# file = open("./greedy_vs_aco.txt", "r")

# line = file.readline().split(",")
# instances = [float(num) for num in line]
# line = file.readline().split(",")
# result_greedy = [round(float(num), 2) for num in line]
# line = file.readline().split(",")
# result_aco = [float(num) for num in line]
# file.close()

# fig = go.Figure()
# fig.add_trace(go.Bar(
#     x=instances,
#     y=result_greedy,
#     # texttemplate="%{y}",
#     # textposition="auto",
#     # textangle=270,
#     name="Greedy Algoritm"
# ))
# fig.add_trace(go.Bar(
#     x=instances,
#     y=result_aco,
#     # texttemplate="%{y}",
#     # textposition="auto",
#     # textangle=270,
#     # textfont_size=100,

#     name="Ant Colony Optimization"
# ))
# for i in range(15):
#     fig.add_annotation(
#         x=instances[i], y=result_greedy[i],
#         text=result_greedy[i],
#         font=dict(
#             size=18
#         ),
#         showarrow=True,
#         textangle=90,
#         xshift=-5,
#         yshift=10
#     )
#     fig.add_annotation(
#         x=instances[i], y=result_aco[i],
#         text=result_aco[i],
#         font=dict(
#             size=18
#         ),
#         showarrow=True,
#         textangle=90,
#         xshift=25,
#         yshift=10
#     )
# fig.update_layout(barmode='group', title_text="Greedy vs ACO")
# # fig.update_xaxes(type='category')
# fig.show()
i = 0
names = []
for instance in instances:
    print(instance)
    print("Best known: ", result_known[i])
    i+=1


    FNULL = open(os.devnull, 'w')
    args = "aco.exe {} {} {} {} {} {}".format(instance, 2000, 
        1000000, 1.0, 
        12.0, 0.6) # beta 6 10 12 - 0% 1% 5%
    subprocess.call(args, shell=False)
    file = open("./output.txt", "r")
    distance = float(file.readline())
    result_aco.append(distance)
    print("ACO: ", distance)

    name = instance.split("/")
    names.append(name[2])



print(names,"\n")
print(result_known,"\n")
print(result_aco)