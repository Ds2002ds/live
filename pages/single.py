import streamlit as st

st.set_page_config(page_title="Single Candlestick Pattern", layout="wide")

# -------------------- HEADER --------------------
st.title("📊 Single Candlestick Patterns")

st.markdown("---")

# A reusable function to create pattern sections
def pattern_section(title, description, composition, key_points, strategy, image_path):
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader(title)
        st.write(description)

        st.markdown("### 🧩 Pattern Composition:")
        st.markdown("\n".join([f"- **{item}**" for item in composition]))

        st.markdown("### 🔑 Key Points:")
        st.markdown("\n".join([f"- {item}" for item in key_points]))

        st.markdown("### 📌 Trading Strategy:")
        st.markdown("\n".join([f"- **{item}**" for item in strategy]))

    with col2:
        st.image(image_path, use_column_width=True)


# -------------------- PATTERNS --------------------

pattern_section(
    "Hammer Candlestick Pattern Analysis",
    "The **Hammer** is a **bullish reversal** candlestick pattern that appears after a downtrend.",
    [
        "Small real body near the top of the candle",
        "Long lower shadow (≥ 2× the body)",
        "Little to no upper shadow"
    ],
    [
        "Occurs after a downtrend",
        "Indicates potential bullish reversal",
        "Confirmation required from next bullish candle",
        "Identifies buying opportunities"
    ],
    [
        "Entry: Price breaking above hammer high",
        "Stop-Loss: Below the hammer’s low",
        "Take Profit: Resistance levels or risk-reward ratio"
    ],
    "C:/Users/HP/Pictures/Screenshots/Screenshot 2025-05-26 054640.png"
)

st.markdown("---")

pattern_section(
    "Doji Candlestick Pattern Analysis",
    "The **Doji** represents **market indecision** and can signal reversal or continuation.",
    [
        "Open and close are nearly equal",
        "Shadows vary in length",
        "Cross-like shape"
    ],
    [
        "Indicates indecision",
        "More meaningful after strong trend",
        "Needs confirmation",
        "Can signal reversal or continuation"
    ],
    [
        "Entry: Based on next candle’s direction",
        "Stop-Loss: Below/above the Doji shadow",
        "Take Profit: Key levels or price action"
    ],
    "C:/Users/HP/Pictures/Screenshots/Screenshot 2025-05-26 054937.png"
)

st.markdown("---")

pattern_section(
    "Inverted Hammer Candlestick Pattern Analysis",
    "**Bullish reversal** pattern forming after a downtrend.",
    [
        "Small body near bottom",
        "Long upper shadow (≥ 2× body)",
        "Little or no lower shadow"
    ],
    [
        "Occurs after downtrend",
        "Indicates possible bullish reversal",
        "Needs strong bullish confirmation",
        "Shows bulls gaining strength"
    ],
    [
        "Entry: Break above inverted hammer high",
        "Stop-Loss: Below pattern low",
        "Take Profit: Resistance or risk-reward ratio"
    ],
    "C:/Users/HP/Pictures/Screenshots/Screenshot 2025-05-26 055039.png"
)

st.markdown("---")

pattern_section(
    "Dragonfly Doji Candlestick Pattern Analysis",
    "A **bullish reversal** doji appearing at the bottom of a downtrend.",
    [
        "Open and close at same level",
        "Long lower shadow",
        "No upper shadow"
    ],
    [
        "Appears at bottom of downtrend",
        "Suggests bullish reversal",
        "Needs bullish confirmation",
        "Shows strong buying pressure"
    ],
    [
        "Entry: Break above doji high",
        "Stop-Loss: Below shadow",
        "Take Profit: Resistance or RR ratio"
    ],
    "C:/Users/HP/Pictures/Screenshots/Screenshot 2025-05-26 055144.png"
)

st.markdown("---")

pattern_section(
    "Shooting Star Candlestick Pattern Analysis",
    "**Bearish reversal** pattern forming after an uptrend.",
    [
        "Small body near bottom",
        "Long upper shadow",
        "Little/no lower shadow"
    ],
    [
        "Occurs after uptrend",
        "Indicates bearish reversal",
        "Needs bearish confirmation",
        "Shows rejection of higher prices"
    ],
    [
        "Entry: Drop below shooting star low",
        "Stop-Loss: Above high",
        "Take Profit: Support levels or RR strategy"
    ],
    "C:/Users/HP/Pictures/Screenshots/Screenshot 2025-05-26 055257.png"
)

st.markdown("---")

pattern_section(
    "Hanging Man Candlestick Pattern Analysis",
    "A **bearish reversal** pattern forming after an uptrend.",
    [
        "Small body at top",
        "Long lower shadow",
        "Little or no upper shadow"
    ],
    [
        "Occurs after uptrend",
        "Suggests bearish reversal",
        "Needs bearish confirmation",
        "Warning of weakening bulls"
    ],
    [
        "Entry: Break below low",
        "Stop-Loss: Above high",
        "Take Profit: Support or RR setup"
    ],
    "C:/Users/HP/Pictures/Screenshots/Screenshot 2025-05-26 055356.png"
)

st.markdown("---")

pattern_section(
    "Gravestone Doji Candlestick Pattern Analysis",
    "A **bearish reversal** doji appearing after an uptrend.",
    [
        "Body near bottom",
        "Long upper shadow",
        "Little/no lower shadow"
    ],
    [
        "Occurs after uptrend",
        "Signals bearish reversal",
        "Needs strong bearish confirmation",
        "Shows sellers taking control"
    ],
    [
        "Entry: Break below low",
        "Stop-Loss: Above high",
        "Take Profit: Support levels or RR ratio"
    ],
    "C:/Users/HP/Pictures/Screenshots/Screenshot 2025-05-26 055449.png"
)

# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown("<center>© 2025 Trade Winds • Privacy Policy • Terms of Service • Contact Us</center>", unsafe_allow_html=True)
