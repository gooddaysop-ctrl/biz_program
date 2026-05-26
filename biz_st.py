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
