import plotly.graph_objects as go
import plotly
import pandas as pd
import preprocessing.additional_participant_data as meta_data
import preprocessing.fixation_ratio as fix_ratio
import preprocessing.means as means
import preprocessing.quartiles as quartile_data
import preprocessing.scanpath as scan_data
import preprocessing.convexhull as hull_data


baseData = meta_data.get_meta_data()
aggData = hull_data.add_convex_hull(scan_data.add_scanpath_length(fix_ratio.add_fix_ratio(baseData)))
means = means.calc_means(aggData)
quartiles = quartile_data.calc_quartiles(aggData)

def lines_by_category(df):
    return dict(
        color = df['Category'],
        colorscale = [
           [0, "orange"],
           [0.3, "orange"],
           [0.3, "red"],
           [0.6, "red"],
           [0.6, "royalblue"],
           [0.9, "royalblue"],
           [0.9, "green"],
           [1.0, "green"]
        ]
    )

def dimensions_for(df):
    return list([
            dict(range = [1,2],
                 tickvals = [1, 2],
                ticktext = ['tree', 'graph'],
                label = 'Visualization', values = df['Visualization']),
            dict(range = [1,2],
                 tickvals = [1, 2],
                ticktext = ['general', 'expert'],
                label = 'Ontologies', values = df['Ontologies']),
            dict(range = [0,1],
                label = 'Task Success', values = df['Task_Success']),
            dict(range = [5, 75],
                label = 'Total Time', values = df['Time_On_Task']),
            dict(range = [0, 1],
                 label = "Percent Time Fixated",
                 values = df['Fixation_Ratio']),
            dict(range=[0.08, 0.5],
                 label='Avg Dilation (Overall Cognitive Overload)',
                 values=df['Avg_Dilation']),
            dict(range=[0, 20000],
                 label='Scanpath',
                 values=df['Scanpath_length']),
            dict(range = [0, 1_280_000],
                 label='Convex Hull Area',
                 values=df['Convex Hull Area'])

    ])

participant_trace = go.Parcoords(
    line = lines_by_category(aggData),
    dimensions = dimensions_for(aggData)
)
means_trace = go.Parcoords(
    line = lines_by_category(means),
    dimensions = dimensions_for(means)
)
quartile_trace = go.Parcoords(
    line = lines_by_category(quartiles),
    dimensions = dimensions_for(quartiles)
)

fig = go.Figure([participant_trace, means_trace, quartile_trace])

fig.update_layout(
    updatemenus = [
            go.layout.Updatemenu(
            type = 'buttons',
            active = 0,
            buttons=[
                dict(label='By Participant',
                     method='restyle',
                     args=['visible', [True, False, False]]),
                dict(label='By Mean',
                     method='restyle',
                     args=['visible', [False, True, False]]),
                dict(label='By Quartiles',
                     method='restyle',
                     args=['visible', [False, False, True]]),

            ]
        )
    ]
#    plot_bgcolor = 'rgb(50, 50, 50)',
#    paper_bgcolor = 'rgb(50, 50, 50)'
)

plotly.offline.plot(fig, filename='Visualization.html')
#fig.show()