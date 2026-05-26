import streamlit as st
# as st는 python에 streamlit을 가져올 때, 이름을 축약한 것.

"""
# 비즈니스 모델 분석😀😀
[네이버](https://www.naver.com)  # 줄바꿈은 스페이스 2번
###### 아얘 이렇게 띄우는 건 그냥 엔터
[홍익대학교](https://www.hongik.ac.kr)

이것이 일반 본문 **이것이 굵은 글씨** *이것이 기울임 글씨* ~~이것이 취소선~~

:red[빨간색 글씨] :green[초록색 글씨] :blue[파란색 글씨]

```python
import streamlit as st

print("코드 블록")
```

"""

st.caption('캡션(작고 흐린 글씨로 표현됨:st.caption()')

with st.echo():
    # 이 블록의 코드와 결과를 출력
    name='Jihwan Oh'
    st.write("Hello,Streamlit!",name)

st.latex('\int_a^bf(x)dx')
"$$\int_a^bf(x)dx$$"

'### :orange[이미지: st.image()]'  
st.image("../Data/python이미지.jpeg",caption="파이썬 로고",width=500)  
# 상대경로를 써줘야함  (절대경로는 깃허브에서 복잡함)

'### :orange[오디오: st.audio()]'  
st.audio("../Data/음악.mp3", format="audio/mpeg", loop=True)

'### :orange[동영상: st.video()]'
video_file=open("../Data/mp_.mp4","rb")
video_bytes=video_file.read()

st.video(video_bytes)

st.divider()
# streamlit이 .py를 웹용 프로그램으로 바꾸ㅓ줌.(나는 깃허브에 .py 입력)
'### :orange[정보:st.info()]'
st.info(
    icon="ℹ️",
    body='''
    **:sunglasses: 이것은 정보를 제공하는 콜아웃입니다.**
      - : red[빨간색 텍스트] 
         - :blue[파란색 텍스트]
     - :green[초록색 텍스트]
         - :orange[주황색 텍스트]
'''
)

'#### :orange[경고: st.warning()]'
st.warning('This is a warning message', icon="⚠️")

'#### :orange[에러: st.error()]'
st.error('This is an error message', icon="🚫")

'#### :orange[성공: st.success()]'
st. success('This is a success message', icon="✅")

# 이미지-> numpt, deep learning->array
# pandas data 프레임은 index와 columns를 가지고 있음.
# matrix(행렬)은 모든 프레임의 데이터 값이 같아야함(numpy)
# matplitlibrary는 그림
# 데이터 프레임에서는 같은 열의 속성만 같으면 된다.

'#### :red[Pandas 데이터프레임]'
import pandas as pd
df=pd.DataFrame(
    {'id':[1,2,3],
     'name':['Alice','Bob','Charlie'],
     'age':[24,34,45]
    }
)
df # 👈 데이터프레임 출력

"""
| 이름 | 학번 | 학과 |
|---|---|---|
| 오지환 | C531150 | 경영학과 |
| 최유리 | 25 | 경영학과 |
| 장서현 | 26 | 경영학과 |
"""
# 여기서 파이프는 🍎 맥북에서 파이프(|) 기호 입력하는 방법:
# 엔터(Return) 키 바로 위에(또는 근처에) 있는 ₩ (또는 \) 키를 Shift 키랑 같이 누르면 돼! (Shift + ₩)
# 마크다운으로 테이블 만들기

'#### :orange[지표(Metric)]'
col1, col2, col3 = st.columns(3) # 3개의 컬럼 생성
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.divider() # 👈 구분선

'# :blue[Streamlit 그래프]'
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"] # legend
)

'#### :orange[st.area_chart()]'
st.area_chart(chart_data)

'#### :orange[st.line_chart()]'
st.line_chart(chart_data)

'#### :orange[st.bar_chart()]'
st.bar_chart(chart_data)

'#### :orange[st.scatter_chart()]'
st.scatter_chart(chart_data)

'#### :orange[st.map()]'
df = pd.DataFrame(
    np.random.randn(100, 2) / [100, 100] + [37.55, 126.92],
    columns=["lat", "lon"],
)
st.map(df)

st.divider()  # 👈 구분선

# np.random.randn(100,2) -> 100행 2열짜리 만들어버림.
# 위의 지도는 37.55, 126.92 좌표를 중심으로 랜덤으로 점 찍힘.

'# :blue[시각화 라이브러리]'

'#### :orange[Matplotlib: st.pyplot()]'
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig) # 👈 차트 출력
