
import streamlit as st
import openai

st.set_page_config(page_title="CapIntel AI", layout="centered")

st.title("🤖 CapIntel AI — ИИ-аналитик по рынку")

ticker = st.text_input("Введите тикер (например, QQQ, AMD, NVDA):")
horizon = st.selectbox("Выберите временной горизонт:", ["Трейд (1-5 дней)", "Среднесрок (1-4 недели)", "Долгосрок (1-6 месяцев)"])
run_analysis = st.button("Проанализировать")

if run_analysis and ticker:
    with st.spinner("Анализирую..."):
        openai.api_key = st.secrets["OPENAI_API_KEY"]

        prompt = f'''
Ты — опытный рыночный аналитик. На основе своей интуиции и опыта определи, что делать с тикером {ticker} в рамках горизонта "{horizon}".
Не упоминай индикаторы. Объясняй просто: что делать сейчас (BUY / SHORT / CLOSE / WAIT), где вход, стоп и цели. Пиши как человек.
'''

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Ты — инвестиционный советник в стиле CapIntel."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=700
        )

        result = response.choices[0].message.content.strip()
        st.markdown("### 🧠 Результат:")
        st.write(result)
