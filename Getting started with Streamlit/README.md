# Streamlit | Getting Started

> The fastest way to build and share data apps

- Streamlit turns data scripts into shareable web apps in minutes.
- All in Python. All for free. No front‑end experience required.

**Open source community driven**

Website link: [https://streamlit.io/](https://streamlit.io/)

Github repo: [https://github.com/streamlit/streamlit](https://github.com/streamlit/streamlit)

Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.

- It is really similar to writing python scripts, this has been developed keeping the Data Scientists in mind

Streamlit cheatsheet: [https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py)

first_app tutorial: [https://docs.streamlit.io/en/stable/getting_started.html#draw-charts-and-maps](https://docs.streamlit.io/en/stable/getting_started.html#draw-charts-and-maps)

> Did you know you can also pass a URL to streamlit run? This is great when combined with Github Gists. For example:
$ streamlit run [https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py](https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py)

So easy to build apps, you just have to follow the defined guidelines

- Wanna add title

```sql
st.title('My first app')
```

- Add content

```sql
st.write('Body')
```

- st.write() is Streamlit’s “Swiss Army knife”. You can pass almost anything to st.write(): text, data, Matplotlib figures, Altair charts, and more. Don’t worry, Streamlit will figure it out and render things the right way.
- Write a data frame [There are other data specific functions like st.dataframe() and st.table() that you can also use for displaying data.]

```sql
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
```

- Magic commands (no need to call streamlit functions)

```sql
"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
```

- Draw a line chart

```sql
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
```

- Draw map

```sql
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
```

### Interactivity

- Use checkboxes to show/hide data

```sql
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
```

- Use a selectbox for options

```sql
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
```

Lay out your app

For a cleaner look, you can move your widgets into a sidebar. This keeps your app central, while widgets are pinned to the left. Let’s take a look at how you can use st.sidebar in your app.

```sql
option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option
```

Most of the elements you can put into your app can also be put into a sidebar using this syntax: `st.sidebar.[element_name]()`. Here are a few examples that show how it’s used: `st.sidebar.markdown()`, `st.sidebar.slider()`, `st.sidebar.line_chart()`.

You can also use `[st.beta_columns](https://docs.streamlit.io/en/latest/api.html#streamlit.beta_columns)` to lay out widgets side-by-side, or `[st.beta_expander](https://docs.streamlit.io/en/latest/api.html#streamlit.beta_expander)` to conserve space by hiding away large content.

```sql
left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")
```

- add progressbar

```sql
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
```