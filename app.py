import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

# sidebar contents
with st.sidebar:
    st.title("This is a title of sider bar!")
    st.markdown('''
    ## About
    This app is an budget planner for Vera & Tom. Building tools for this app: 
    - [Streamlit](https://streamlit.io/)
    ''')
    add_vertical_space(5)
    st.write("Made with ❤️ by Vera")
def main():
    st.write("Hello!")

if __name__ == '__main__':
    main()