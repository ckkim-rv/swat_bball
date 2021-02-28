import os

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def run(file,i):
    df = pd.read_csv(pd.read_excel(file))

    rb = []
    rb_gf = []
    rb_ga = []

    rounds = np.arrange(1,11)

    for i in range(1,20,2):
        b = pd.to_numeric(rb.iloc[][i])
        c = pd.to_numeric(rb.iloc[][i+1])
        a = b-c
        rb.append(a)
        rb_gf.append(b)
        rb_ga.append(c)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=rounds, y=rb1,
                            mode='lines+markers',
                            name='19_20'))
        fig.add_trace(go.Scatter(x=rounds, y=rb2,
                            mode='lines+markers',
                            name='18-19'))
        fig.add_trace(go.Scatter(x=rounds, y=rb3,
                            mode='lines+markers', name='17-18'))

        fig.update_layout(title='Point difference by rounds')

        fig.write_image(Path("images/fig" + str(i)))
directory = Path('data/')

files = os.listdir(directory)

for file in files:
