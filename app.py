import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="My Python Game", layout="centered")

st.title("🎮 Pyxel x Streamlit Mario")
st.write("GitHubに保存されたコードをブラウザで実行します。")

# スコアの説明（一時的であることの明示）
st.info("※ スコアはブラウザを閉じるとリセットされます。")

# 1. Pyxel公式のWebランチャーを利用する方法
# 自分のGitHubのURLを指定することで、Streamlit内でゲームを読み込めます
github_user = "あなたのユーザー名"
repo_name = "リポジトリ名"
game_file = "game.py"

pyxel_url = f"https://pyxel.jp/launcher/?run={github_user}.{repo_name}.{game_file}"

# iframeでゲーム画面を表示
components.iframe(pyxel_url, height=500, scrolling=False)

st.write("---")
st.subheader("遊び方")
st.markdown("""
- **スペースキー**: ジャンプ
- **矢印キー**: 移動
- **リセット**: ブラウザを再読み込みしてください
""")
