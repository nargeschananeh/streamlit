# import streamlit as st
# import pandas as pd 
# import numpy as np

# st.title('this is streamlit project')
# st.write('this is firs app')


# x = st.slider('please select your age', 5,78, step = 5)
# st.write(f'your age is {x}')

# y = st.selectbox('please select your favorite city',
#              ('london', 'paris', 'ahwaz'))
# st.write(f'your favorite city is {y}')

# z = st.multiselect('select your hobbies',
#                ('sport', 'movie', 'reading'))
# st.write(f'your hobbies are {z}')

# st.radio('select your degree',
#          ('BE', 'MS', 'DR', 'PDR'))

# if st.toggle('on/off'):
#     st.write('toggle is On')

# if st.checkbox('display/hide'):
#     st.write('show is activated')

# st.success('your action don')
# st.warning('be careful')
# st.error('Danger')

# col1, col2, col3 = st.columns(3)

# col1.title('First Column')
# col1.slider('choose grade', 0, 20)
# col2.title('Second Column')
# col2.number_input('enter your age', step=1, min_value=10, max_value=50)
# col3.title('Third Column')
# col3.text_input('enter your field')

# if st.checkbox('show/hide'):
#     data = pd.DataFrame(np.random.randn(20, 4),
#                     columns=['x', 'y', 'z', 't'])
#     st.line_chart(data)
#     st.bar_chart(data)
#     data

# st.image('./image/cat.JPG.jpg')
# st.image('./image/red-rose.jpg')
# st.audio('./audio/C.mp3')

# st.sidebar.title('select your option')
# salary = st.sidebar.slider('select salary', 1000,5000)
# st.write(f'salary is {salary}')
# option = st.sidebar.selectbox('choose your option',
#                                ('image', 'audio', 'diagram', 'funny'))

# if option == 'image':
#     st.image('./image/cat.JPG.jpg')
# elif option == 'audio' :
#     st.audio('./audio/C.mp3')
# elif option == 'diagram':
#     data = pd.DataFrame(np.random.randn(20, 4),
#                         columns=['x', 'y', 'z', 't'])
#     st.line_chart(data)
#     st.bar_chart(data)
#     data
# elif option == 'funny':
#     st.balloons()