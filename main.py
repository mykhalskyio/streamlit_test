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
request_1 = st.Page(
    "request/request_1.py",
    title="",
    default=(role == "Requester"),
)
request_2 = st.Page(
    "request/request_2.py", title=""
)
respond_1 = st.Page(
    "respond/respond_1.py",
    title="",
    default=(role == "Responder"),
)
respond_2 = st.Page(
    "respond/respond_2.py", title="",
)
admin_1 = st.Page(
    "admin/admin_1.py",
    title="",
    default=(role == "Admin"),
)
admin_2 = st.Page("admin/admin_2.py", title="")

account_pages = [logout_page, settings]
request_pages = [request_1, request_2]
respond_pages = [respond_1, respond_2]
admin_pages = [admin_1, admin_2]

st.title("Request manager")

page_dict = {}
if st.session_state.role in ["Requester", "Admin"]:
    page_dict["Request"] = request_pages
if st.session_state.role in ["Responder", "Admin"]:
    page_dict["Respond"] = respond_pages
if st.session_state.role == "Admin":
    page_dict["Admin"] = admin_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()
