import streamlit as st

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "Requester", "Responder", "Admin"]


def login():

    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()


role = st.session_state.role

logout_page = st.Page(logout, title="")
settings = st.Page("settings.py", title="")
admin_1 = st.Page(
    "admin/admin_1.py",
    title="",
    default=(role == "Admin"),
)
admin_2 = st.Page("admin/admin_2.py", title="")

account_pages = [logout_page, settings]
admin_pages = [admin_1, admin_2]

st.title("Request manager")

page_dict = {}
if st.session_state.role == "Admin":
    page_dict["Admin"] = admin_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()
