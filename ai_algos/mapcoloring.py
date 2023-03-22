import plotly.express as px
from csp_solvers import AC3

def MapColoring(constraint_graph,colors):
    D = {country: colors.copy() for country in constraint_graph.keys()} # color Domain    
    csp = (constraint_graph,D)
    if AC3(csp): return D
    
    return None

colors = ["red", "green", "blue"]
constraint_graph = {
    "WA" :["NT", "SA"], 
    "NT": [ "WA", "SA", "Q"], 
    "SA": ["WA", "NT", "Q"], 
    "Q": ["SA", "NT", "NSW"], 
    "NSW": ["SA", "Q", "V"],
    "V": ["NSW", "SA"], 
    "T":[]
    }


valid_assignment = MapColoring(constraint_graph,colors)
if valid_assignment: print(valid_assignment)
else: print("Can not be solved!")


#############################################################################################################
### just for visualization purposes
### uncoment the below program to visualize

# scope2 = "south america"
# colors2 = ["blue", "green", "red", "yellow"]
# constraint_graph2 = { 
#     "Argentina": ["Bolivia", "Brazil", "Chile", "Paraguay", "Uruguay"],
#     "Bolivia": ["Argentina", "Brazil", "Chile", "Paraguay", "Peru"],
#     "Brazil": ["Argentina", "Bolivia", "Colombia", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"],
#     "Chile": ["Argentina", "Bolivia", "Peru"],
#     "Colombia": ["Brazil", "Ecuador", "Peru", "Venezuela"],
#     "Ecuador": ["Colombia", "Bolivia", "Peru"],
#     "Falkland Islands": [],
#     "Guyana": ["Brazil", "Suriname", "Venezuela"],
#     "Paraguay": ["Argentina", "Bolivia", "Brazil"],
#     "Peru": ["Bolivia", "Brazil", "Chile", "Colombia", "Ecuador"],
#     "Suriname": ["Brazil", "Guyana"],
#     "Uruguay": ["Argentina", "Brazil"],
#     "Venezuela": ["Brazil", "Colombia", "Guyana"] 
#     }


# def plot_choropleth(D,scope):
#     colormap = {country: domain[0] for country,domain in D.items()}
#     countries = D.keys()
#     fig = px.choropleth(locationmode="country names",
#                         locations=countries,
#                         color=countries,
#                         color_discrete_sequence=[colormap[c] for c in D.keys()],
#                         scope=scope)
#     fig.show()

# valid_assignment = MapColoring(constraint_graph2,colors2)
# plot_choropleth(valid_assignment,"south america")