import streamlit as st
from multiapp import MultiApp
from apps import home, data_stats, visual_app, visual_loss  # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data Stats", data_stats.app)
app.add_app("Huấn luyện", visual_loss.app)
app.add_app("Kết quả", visual_app.app)
# The main app
app.run()