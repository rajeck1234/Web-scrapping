from IPython.display import HTML
import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(1000), columns=['data'])

df.to_csv('submission.csv')

def create_download_link(title = "Download CSV file", filename = "data.csv"):  
    html = '<a href={filename}>{title}</a>'
    html = html.format(title=title,filename=filename)
    return HTML(html)

# create a link to download the dataframe which was saved with .to_csv method
create_download_link(filename='submission.csv')
