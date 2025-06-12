import streamlit as st

# 设置页面配置
st.set_page_config(page_title="视频编辑器", page_icon="🎬")

# 定义媒体数据（图片+对应视频）<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=441841347&bvid=BV1hL411S7Qb&cid=1076988324&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
media_library = {
    "map1": {
        "image_url": "https://media.9game.cn/gamebase/ieu-gdc-pre-process/images/20230328/4/20/2f125d45598aa2cd0947034f9f82381a.png",
        "video_url": "https://cdn.pixabay.com/video/2025/04/09/270940_tiny.mp4"       
    },
    "map2": {
        "image_url": "https://img.pconline.com.cn/images/upload/upc/tx/photoblog/1011/13/c1/5848328_5848328_1289615909062.jpg",
        "video_url": "https://www.w3schools.com/html/movie.mp4",
        
    },
    "map3": {
        "image_url": "https://picx.zhimg.com/v2-531d0ce464a3409581f33c578d225ffd_720w.jpg?source=172ae18b",
        "video_url": "https://media.w3.org/2010/05/sintel/trailer.mp4"
    
    }
}

# 初始化session_state
if 'selected_media' not in st.session_state:
    st.session_state.selected_media = "map1"

# 页面标题
st.header("🎬Streamlit视频编辑器")

# 视频播放区域
st.subheader("🎬展示集锦")
current_media = st.session_state.selected_media
st.video(media_library[current_media]["video_url"])

# 下拉选择器
st.subheader("选择媒体")
selected = st.selectbox(
    "请选择要播放的媒体：",
    options=list(media_library.keys()),
    index=list(media_library.keys()).index(current_media),
    key="media_selector"
)

if selected != current_media:
    st.session_state.selected_media = selected
    st.rerun()

if st.button("map1", key="btn_natural"):
    st.session_state.selected_media = "map1"
    st.rerun()
st.image(
    media_library["map1"]["image_url"],
    
    use_container_width=True
)

if st.button("map2", key="btn_city"):
    st.session_state.selected_media = "map2"
    st.rerun()
st.image(
    media_library["map2"]["image_url"],
    use_container_width=True
)
if st.button("map3", key="map3_city"):
    st.session_state.selected_media = "map3"
    st.rerun()
st.image(
    media_library["map3"]["image_url"],
    use_container_width=True
)
