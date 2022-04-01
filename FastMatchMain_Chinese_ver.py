# -*- coding: UTF-8 -*-
import streamlit as st 
import time
import matchering as mg

#Main Text
st.title("欢迎使用FastMatch")
st.subheader("将你的音乐变得好听的最快方式")
st.markdown('<style>h3{color: gray;}</style>', unsafe_allow_html=True)

#get the files
st.write("请输入你的目标文件（WAV）:")
tar = st.text_input("格式：文件名绝对路径.wav",key = 1)
target_file = str(tar)
st.write("请输入你的参考文件（WAV）:")
refer = st.text_input("格式：文件名绝对路径.wav",key = 2)
refer_file = str(refer)

#add select-box
limiter_option = st.selectbox("是否使用限制器（limiter）最大化音量:",('是','否'),help="通过选择 是 来使用limiter，选择否关闭limiter")

#add sidebar
side_info = st.sidebar.container()
side_info.title("关于我们")
side_info.write("此应用遵循了一个简单的想法 - 将您的两个音频文件输入其中:")
side_info.write("1.TARGET: (你想要制作母带的曲目，你希望它听起来像参考曲目)")
' ' #an empty line
side_info.write("2.REFERENCE: (另一首曲目，比如某种流行歌曲，你希望你的目标曲目听起来像它)")
' ' #an empty line
side_info.write("我们的算法匹配这两个轨道，并为您提供与参考轨道相同的RMS，FR，峰值振幅和立体声宽度的母带目标轨道")
side_info.write("     ")
side_info.write("     ")
side_info.write("作者 : UltraV")
side_info.write("Email : ultravmusic@qq.com")

#buttons
left_column, right_column = st.columns(2)
button1 = left_column.button("Start",help = "Starting Your Process")
button2 = right_column.button("Preview",help = "Export 30s Preview File")

#functions
def use_limiter():
  if limiter_option == '是':
    return True
  else:
    return False

def process_file():
  mg.process(
    target = target_file,
    reference = refer_file,
    results=[
        mg.Result(target_file + "_mastered_32bit.wav",subtype="PCM_32",use_limiter=use_limiter()),
    ],
  )
  
def infomations():
  mg.log(print)
  
def loading_file():
  latest_iteration = st.empty()
  bar = st.progress(0)
  #for loops
  for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'processing ~ {i + 1}%')
    bar.progress(i + 1)
    time.sleep(0.04)
  #spinner
  with st.spinner('Wait for it...'):
    time.sleep(1)
  st.success('Done!')
  #st.error("Oops!There's sth wrong!")
  st.balloons()

def Preview_file():
  mg.log(
    target = target_file,
    reference = refer_file,
    result = [],
    preview_target=mg.pcm24("preview_my_song.flac"),
    preview_result=mg.pcm24("preview_my_song_master.flac"),
  )


#logics
if button1:
  loading_file()
  infomations()
  process_file()

if button2:
  loading_file()
  infomations()
  Preview_file()
