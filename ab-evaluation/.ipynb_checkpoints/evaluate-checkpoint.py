import pandas
from IPython.core.display_functions import display
from ipywidgets import widgets

df = pandas.read_csv("responses.csv")
df.sample(frac=1).reset_index(drop=True)
response_index = 0
df['feedback'] = pandas.Series(dtype='str')

def on_button_clicked(b):
    global response_index
    user_feedback = 1 if b.description == "\U0001F44D" else 0
    df.at[response_index, 'feedback'] = user_feedback
    response_index += 1
    if response_index < len(df):
        update_response()
    else:
        df.to_csv("results.csv", index=False)
    print("A/B testing completed. Here's the results:")
    summary_df = df.groupby('variant').agg(
        count=('feedback', 'count'),
        score=('feedback', 'mean')).reset_index()
    print(summary_df)

def update_response():
    new_response = df.iloc[response_index]['response']
    if pandas.notna(new_response):
        new_response = '<p>' + new_response + "</p>"
    else:
        new_response = "<p>No response</p>"
    response.value = new_response
    count_label.value = f"Response: {response_index + 1}"
    count_label.value += f"/{len(df)}"

response = widgets.HTML()
count_label = widgets.Label()

update_response()

thumbs_up_button = widgets.Button(description='\U0001F44D')
thumbs_up_button.on_click(on_button_clicked)
thumbs_down_button = widgets.Button(description='\U0001F44E')
thumbs_down_button.on_click(on_button_clicked)
button_box = widgets.HBox([thumbs_down_button, thumbs_up_button])

display(response, button_box, count_label)
