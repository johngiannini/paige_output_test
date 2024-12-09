# Paige: Output Test

Streamlit, while an excellent tool in many ways, poses challenges if one wants to generate output from within a concurrent contenxt. 

(This is because Streamlit itself uses concurrency, with each session existing as a separate thread under a single process. Each thread may thus not have access to important state, such as st.sessionstate, while truly global objects will transcend any given session potentially leading to conflicts.)

This project is to help diagnose and solve this issue. It will begin with a minimal recreation of the problem and then allow easy testing of potential solutions. Currently lets_do_this.py contains a function that will cause the error, while lets_do_this_II.py contains a fixed version. You can switch beetween them in the ui by just changing the import line.