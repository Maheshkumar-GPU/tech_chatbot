import streamlit as st
import ollama
import time

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Gear Force AI",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------
# PURPLE & BLACK PREMIUM DARK THEME (CSS)
# -----------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

/* Global Overrides */
html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    background-color: #0B0813 !important; /* Deep black-purple */
    color: #E2E8F0 !important;
}

/* Main Container Constraint */
[data-testid="stMainBlockContainer"] {
    max-width: 850px;
    margin: 0 auto;
    padding-top: 4rem;
    padding-bottom: 6rem;
}

/* Header UI */
.header-container {
    text-align: left;
    margin-bottom: 3rem;
}

.main-title {
    font-size: 42px;
    font-weight: 700;
    background: linear-gradient(135deg, #A855F7 0%, #6366F1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -1px;
    margin-bottom: 0.25rem;
}

.subtitle {
    color: #94A3B8;
    font-size: 15px;
    font-weight: 400;
}

/* Sidebar Dark Theme Styling */
[data-testid="stSidebar"] {
    background-color: #07050C !important;
    border-right: 1px solid #1E1B4B !important;
}

/* Code block typography fix */
code, pre {
    font-family: 'JetBrains Mono', monospace !important;
}

/* Transparent native chat message boxes to blend with background */
[data-testid="stChatMessage"] {
    background-color: transparent !important;
    border-bottom: 1px solid #1E1A3A !important;
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important;
}

/* Chat Input styling (Purple border glow) */
[data-testid="stChatInputForm"] {
    border-radius: 16px !important;
    border: 1px solid #3B0764 !important;
    background-color: #0F0B21 !important;
    box-shadow: 0 0 20px rgba(168, 85, 247, 0.05) !important;
}

[data-testid="stChatInputForm"]:focus-within {
    border-color: #A855F7 !important;
    box-shadow: 0 0 25px rgba(168, 85, 247, 0.15) !important;
}

/* Hide native Streamlit layout headers */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }

/* Interactive Sidebar Pill Components */
.example-pill {
    background-color: #120E2E;
    border: 1px solid #2E1065;
    padding: 0.6rem 1rem;
    border-radius: 12px;
    font-size: 13px;
    color: #C084FC;
    margin-bottom: 0.6rem;
    font-weight: 500;
}

/* Custom Thinking Indicator Styling */
.thinking-box {
    display: flex;
    align-items: center;
    gap: 10px;
    color: #A855F7;
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    padding: 1rem 0;
}

.dot-flashing {
    position: relative;
    width: 6px;
    height: 6px;
    border-radius: 5px;
    background-color: #A855F7;
    color: #A855F7;
    animation: dot-flashing 1s infinite linear alternate;
    animation-delay: .5s;
}

@keyframes dot-flashing {
    0% { background-color: #A855F7; }
    50%, 100% { background-color: rgba(168, 85, 247, 0.2); }
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# HEADER
# -----------------------------------

st.markdown(
    """
    <div class="header-container">
        <div class="main-title">Gear Force AI</div>
        <div class="subtitle">Next-generation engineering workspace environment.</div>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------------
# SIDEBAR
# -----------------------------------

with st.sidebar:
    st.markdown("<p style='color: #A855F7; font-weight: 600; font-size: 11px; letter-spacing: 1px;'>CORE SYSTEMS</p>",
                unsafe_allow_html=True)
    st.subheader("Gear Force Node")

    st.markdown(
        """
        <p style='color: #94A3B8; font-size: 13px;'>Optimized for technical syntax highlighting, cryptographic verification architectures, and distributed systems logic.</p>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        "<p style='color: #A855F7; font-weight: 600; font-size: 11px; letter-spacing: 1px;'>PROMPT SUGGESTIONS</p>",
        unsafe_allow_html=True)
    examples = [
        "Debug thread deadlocks in Rust",
        "Design an idempotent API gateway",
        "Explain Zero-Knowledge proofs simply",
        "Optimize a database indexing strategy"
    ]

    for ex in examples:
        st.markdown(f'<div class="example-pill">⚡ {ex}</div>', unsafe_allow_html=True)

    st.divider()

    # Custom styled button container
    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #2E1065 !important;
        color: #E9D5FF !important;
        border: 1px solid #7E22CE !important;
        border-radius: 10px !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #5B21B6 !important;
        border-color: #A855F7 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    if st.button("Reset Secure Thread", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# -----------------------------------
# SESSION STATE INITIALIZATION
# -----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------------
# DISPLAY MESSAGES (NATIVE INTEGRATION)
# -----------------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------------
# USER INPUT & EXECUTION AREA
# -----------------------------------

if user_input := st.chat_input("Inject payload or ask a engineering question..."):

    # 1. Render user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({"role": "user", "content": user_input})

    # 2. System Instruction Configuration
    system_prompt = """You are Gear Force AI, an elite engineering assistant.
- Provide highly technical, exact responses.
- Present clean, language-tagged code blocks for practical execution.
- Maintain a highly professional tone."""

    # 3. Generate Streamed Response
    with st.chat_message("assistant"):
        # Custom "thinking......" UI container matching request
        thinking_placeholder = st.empty()
        thinking_placeholder.markdown(
            """
            <div class="thinking-box">
                <span>thinking......</span>
                <div class="dot-flashing"></div>
            </div>
            """,
            unsafe_allow_html=True
        )

        response_placeholder = st.empty()
        full_response = ""

        try:
            response_stream = ollama.chat(
                model="tinyllama",
                messages=[
                    {"role": "system", "content": system_prompt},
                    *st.session_state.messages
                ],
                stream=True
            )

            # Wipe away thinking phrase as soon as the first token stream yields text
            first_token = True
            for chunk in response_stream:
                if first_token:
                    thinking_placeholder.empty()
                    first_token = False

                full_response += chunk['message']['content']
                response_placeholder.markdown(full_response + "▊")

            response_placeholder.markdown(full_response)

        except Exception as e:
            thinking_placeholder.empty()
            full_response = f"❌ **Engine Interrupt Exception:** `{str(e)}`"
            response_placeholder.markdown(full_response)

    # 4. Save Response to Thread Memory
    st.session_state.messages.append({"role": "assistant", "content": full_response})