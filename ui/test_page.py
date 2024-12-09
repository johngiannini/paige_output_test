import streamlit as st

from output.output import Output
from functions.lets_do_this_II import lets_do_this


st.set_page_config(
    layout="wide",
    page_title="paige",
    page_icon="🥸",
)


def main():
    st.header("Output Test")
    st.write("Press button to begin test:")
    if st.button(label="Begin Test", key="begin_test"):
        st.write("Test started.")
        status_container = st.status("Initializing...",
                                     expanded=True)
        Output().configure(
            on_log=lambda m: status_container.write(m),
            on_error=lambda m: status_container.error(m),
            on_status=lambda m: status_container.update(label=m),
            on_complete=lambda m: status_container.update(label=m, state="complete", expanded=False),
            on_terminal_error=lambda m: status_container.update(label=m, state="error"),
            verbose=True
        )

        lets_do_this(status_container)



if __name__ == "__main__":
    main()
