


## input descrption, params, returns,
## generate code
## exec answers with user-defined test cases

import streamlit as st
import pandas as pd


col1, col2 = st.columns([1, 1])

if "code" not in st.session_state:
    st.session_state.code = ""
 
with col1:
    function_name = st.text_input(label="Function name")
    print(function_name)

    st.text_area(label="Description")
    st.write("Parameters")
    df_params = st.data_editor(
        data=pd.DataFrame(columns=["name", "type", "description"]),
        key="params",
        num_rows="dynamic", 
        use_container_width=True
    )
    st.write("Returns")
    df_returns = st.data_editor(
        data=pd.DataFrame(columns=["name", "type", "description"]),
        key="returns",
        num_rows="dynamic", 
        use_container_width=True
    )

    generate = st.container()
    with generate:
        if st.button("Generate Code"):
            st.session_state.code = """import streamlit as st
print("HELLO@WORLD")
"""



with col2:
    st.write("Generated code")

    st.code(body=st.session_state["code"])
    st.write(st.session_state["params"])
    res = exec(st.session_state.code)
    st.write(res)
    

    
    

# inputs, returns