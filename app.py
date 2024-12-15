# a Basic Chat Bot tha responds about one topic only 'AI'. Built using google gen ai

import streamlit as st
import json
from chatbot import Chatbot
# App Title
# Styled App Title
st.markdown("<h2 style='text-align: center; color: blue;'>🤖 Movies Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: red;'>Enter movie name to search: </h1>", unsafe_allow_html=True)

# Chat History State
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.form(key="message_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:", key="user_input")
    submit_button = st.form_submit_button("Send")

chatbot = Chatbot()

st.write("### Chat History:")
# Process User Input
if submit_button:
    if user_input.strip():
        # Add user's message to chat history
        st.session_state.messages.append(("user", user_input))
        
        # Show a spinner during processing
        with st.spinner("Bot is typing..."):
            # Placeholder chatbot logic 
            bot_response = chatbot.get_response(user_input)

        # Add bot's response to chat history
        st.session_state.messages.append(("bot", bot_response))
        
        # Clear the input box
        st.rerun()
# Display Chat History

# Display Chat History in Reverse Order by Pairs
for i in range(len(st.session_state.messages) - 1, -1, -2):  # Step backward in pairs
    if i > 0:
        # Display bot response first, then user query (reverse pair)
        bot_sender, bot_text = st.session_state.messages[i]
        user_sender, user_text = st.session_state.messages[i - 1]
        if user_sender == "user":
            st.markdown(f"**🧑 User:** {user_text}")
        if bot_sender == "bot":
            # st.markdown(f"**🤖 Bot:**")
            if bot_text == "Failed":
              st.markdown("No movie found!....")  
            else:
                response_dict = bot_text
                # st.markdown(f"Movie Name: {response_dict["Movie Name"]}")
                # st.markdown(f"Director: {response_dict["Director"]}")
                # st.markdown(f"Year: {response_dict["Year"]}")
                # st.markdown(f"Country: {response_dict["Country"]}")
                # st.markdown(f"Genre: {response_dict["Genre"]}")
                # st.markdown(f"Cast:")
                # for name in response_dict["Cast"]:
                #     st.markdown(name)
                # st.markdown(f"Plot: {response_dict["Plot"]}")
                # st.markdown(f"Recommended Movies: ")
                # for name in response_dict["Recommended Movies"]:
                #     st.markdown(name)
                table_html = f"""
                <style>
                    table {{
                        width: 80%;
                        margin: auto;
                        border-collapse: collapse;
                        border: 1px solid #ddd;
                        font-family: Arial, sans-serif;
                    }}
                    th, td {{
                        padding: 10px;
                        text-align: left;
                        border-bottom: 1px solid #ddd;
                    }}
                    th {{
                        background-color: #4CAF50;
                        color: white;
                    }}
                    tr:hover {{
                        background-color: #f1f1f1;
                    }}
                    .header {{
                        text-align: center;
                        font-size: 24px;
                        font-weight: bold;
                        margin-bottom: 20px;
                    }}
                </style>
                <div class="header">Movie Details</div>
                <table>
                    <tr>
                        <th>Attribute</th>
                        <th>Details</th>
                    </tr>
                    <tr>
                        <td>Movie Name</td>
                        <td>{response_dict["Movie Name"]}</td>
                    </tr>
                    <tr>
                        <td>Director</td>
                        <td>{response_dict["Director"]}</td>
                    </tr>
                    <tr>
                        <td>Year</td>
                        <td>{response_dict["Year"]}</td>
                    </tr>
                    <tr>
                        <td>Country</td>
                        <td>{response_dict["Country"]}</td>
                    </tr>
                    <tr>
                        <td>Genre</td>
                        <td>{response_dict["Genre"]}</td>
                    </tr>
                    <tr>
                        <td>Cast</td>
                        <td>{', '.join(response_dict["Cast"])}</td>
                    </tr>
                    <tr>
                        <td>Plot</td>
                        <td>{response_dict["Plot"]}</td>
                    </tr>
                    <tr>
                        <td>Recommended Movies</td>
                        <td>{', '.join(response_dict["Recommended Movies"])}</td>
                    </tr>
                </table>
                """

                # Display the table using Streamlit's markdown with unsafe_allow_html
                st.markdown(table_html, unsafe_allow_html=True)
    else:
        # Handle the case where there's an unmatched last message (e.g., user's query)
        sender, text = st.session_state.messages[i]
        if sender == "user":
            st.markdown(f"**🧑 User:** {text}")
        elif sender == "bot":
            st.markdown(f"**🤖 Bot:** {text}")

# Footer
st.write("---")
st.caption("Built by M. Saghir Abbasi")
