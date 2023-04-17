import streamlit as st
import openai

OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

# 모델 - GPT 3.5 Turbo 선택
model = "gpt-3.5-turbo"


# completion_executor = CompletionExecutor(
#     host=config['CLOVA']['host'],
#     api_key=config['CLOVA']['api_key'],
#     api_key_primary_val=config['CLOVA']['api_key_primary_val'],
#     request_id=config['CLOVA']['request_id']
# )

st.title('민족의 대답')

preset_base_input = '배달의민족 리뷰에 대한 가게사장님의 대답을 센스있게 가게'

preset_input = st.selectbox(
    '사전 문장',
    ('이모티콘 넣어서 작성해줘',
     '재치있게 작성해줘'
     ),
    index= 0
)

question = st.text_area(
    '리뷰', 
    placeholder='고객의 리뷰를 입력해 주세요', 
)

if preset_input and question:
    preset_text = f'{preset_base_input}{preset_input}\n리뷰:{question}'

    print(preset_text)

    messages = []
    messages.append({"role" : "user", "content" : f"{question}"})

    completion = openai.ChatCompletion.create(model=model, messages=messages)


    assistant_content = completion.choices[0].message["content"].strip()
    print(assistant_content)
    st.markdown(assistant_content)