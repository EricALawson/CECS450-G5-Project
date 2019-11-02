import preprocessing.additional_participant_data as meta_data
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = meta_data.get_meta_data()

fig = make_subplots(rows=2, cols=2)

fig.add_trace(
    go.Scatter(
        x = data['Time_On_Task'],
        y = data['Task_Success'],
        mode = 'markers',
        marker = dict(
            color=data['Category']
        )
    ),
    row=1, col=1
)

fig.add_trace(
    go.Box(
        y=data[data.Category == 1]['Task_Success']
    ),
    row=1, col=2
)
fig.add_trace(
    go.Box(
        y=data[data.Category == 2]['Task_Success']
    ),
    row=1, col=2
)
fig.add_trace(
    go.Box(
        y=data[data.Category == 3]['Task_Success']
    ),
    row=1, col=2
)
fig.add_trace(
    go.Box(
        y=data[data.Category == 4]['Task_Success']
    ),
    row=1, col=2
)

fig.show()
