import streamlit as st
import function as fu

items1 = fu.getTodos()

def add_todo():
    new_data = st.session_state["new_todo"] + '\n'
    items1.append(new_data)
    fu.writeTodos(items1)

st.title('My Todo App')

st.subheader('This is my todo app')

st.write('This is first version for web base app')

for index , item in enumerate(items1):
    new_item = st.checkbox(item, key=f'item{index}')
    if new_item:
        items1.pop(index)
        fu.writeTodos(items1)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label="Add a todo", placeholder='Add a todo...', on_change=add_todo,
              key='new_todo')
print('hello')
