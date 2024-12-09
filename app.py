import streamlit as st
from chatbot import Chatbot
# App Title
# Styled App Title
st.markdown("<h2 style='text-align: center; color: blue;'>🤖 AI Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: red;'>Ask me anything about Artificial Intelligence</h1>", unsafe_allow_html=True)

# Chat History State
if "messages" not in st.session_state:
    st.session_state.messages = []


# # User Input
# st.write("---")
# user_input = st.text_input("Type your message:", key="user_input")

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
            st.markdown(f"**🤖 Bot:** {bot_text}")
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
