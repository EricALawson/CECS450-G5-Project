import plotly.graph_objects as go
import pandas as pd
import preprocessing.additional_participant_data as meta_data
import preprocessing.fixation_ratio as fix_ratio

df = meta_data.get_meta_data()
aggData = fix_ratio.add_fix_ratio(df)

fig = go.Figure(data=
    go.Parcoords(
        line = dict(color = aggData['Category'],
                   colorscale = [[0,'purple'],[0.5,'lightseagreen'],[1,'gold']]),
        dimensions = list([
            dict(range = [1,4],
                 tickvals = [1, 2, 3, 4],
                 constraintrange = [0.8, 1.2],
                ticktext = ['TreeGeneral', 'GraphGeneral', 'TreeExpert', 'GraphExpert'],
                label = 'Subset', values = aggData['Category']),
            dict(range = [0.08, 0.5],
                 label = 'Avg Dilation (Overall Cognitive Overload)', values = aggData['Avg_Dilation']),
            dict(range = [0,1],
                label = 'Task Success', values = aggData['Task_Success']),
            dict(range = [5, 75],
                label = 'Total Time', values = aggData['Time_On_Task']),
            dict(range = [0,1],
                 label = "Percent Time Faxated",
                 values = aggData['Fixation_Ratio'])
        ])
    )
)

fig.show()