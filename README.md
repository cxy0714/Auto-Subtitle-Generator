# Auto-Subtitle-Generator

为了搬运YouTube的[Online Causal Inference Seminar](https://www.youtube.com/@onlinecausalinferencesemin2364/videos)讲座到[B站](https://space.bilibili.com/439010560/lists)，进而可以吃饭的时候看B站，但是字幕处理是个问题。

Chatgpt写完了所有代码，在我的轻薄本笔记本上一次跑通！本地部署的 `faster-whisper-tiny`只用cpu就可以做到英语自动识别的好效果，中文翻译b站已经有了，可以双语字幕。

[为祂献上膝盖！Chatgpt聊天记录](https://chatgpt.com/share/67a24602-4368-8006-8201-b6a8fa16a53c)

## 📌 项目简介

本项目是一个  **批量视频字幕生成工具** ，通过 `faster-whisper` 进行语音识别，并结合 `ffmpeg` 提取音频，最终生成  **自动字幕 (SRT 文件)** 。

主要功能：

* 批量处理一个文件夹中的 **所有 MP4 视频**
* 使用 `faster-whisper`（优化版 Whisper）进行 **高效语音识别**
* 通过 `ffmpeg` **提取音频**
* **自动优化字幕长度** ，保证单行不超过 **12 个单词**

---

## 🛠 代码结构

```
📂 Auto-Subtitle-Generator
├── 📂 videos               # 存放待处理视频
├── 📂 output               # 生成的字幕文件（SRT）
├── 📂 utils                # 工具函数
│   ├── audio_utils.py      # 处理音频的工具（提取音频）
│   ├── asr_utils.py        # 语音识别工具（调用 faster-whisper）
│   ├── srt_utils.py        # 处理 SRT（分割字幕）
├── main.py                 # 入口脚本，批量处理视频
├── requirements.txt        # 依赖库
├── README.md               # 说明文档
```

---

## 🚀 安装指南

### 1️⃣ 安装 Python 依赖

本项目基于 Python 3.8+，请先安装必要的库：

```sh
pip install -r requirements.txt
```

`requirements.txt` 包含：

* `faster-whisper`：用于高效语音识别
* `ffmpeg`：用于提取视频中的音频

### 2️⃣ 安装 FFmpeg

**Windows** 用户请手动下载并配置 `FFmpeg`：

1. 下载 FFmpeg（推荐 `ffmpeg-master-latest-win64`）：

   [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
2. 解压后，将 `bin` 目录路径（如 `C:\ffmpeg\bin`）添加到系统环境变量 `PATH`
3. 运行 `ffmpeg -version` 确保安装成功

**Linux / Mac** 用户可以直接安装：

```sh
sudo apt install ffmpeg   # Ubuntu/Debian
brew install ffmpeg       # macOS
```

### 3️⃣ 预下载 Faster-Whisper 模型（可选）

如果不想每次运行时下载，可以手动下载 `tiny` 版模型，并存放到 Hugging Face 缓存：

```sh
mkdir -p ~/.cache/huggingface/hub
wget -P ~/.cache/huggingface/hub https://huggingface.co/guillaumekln/faster-whisper-tiny/resolve/main/model.bin
```

---

## 🎯 使用方法

### **1️⃣ 运行脚本**

```sh
python main.py ./videos ./output
```

* `./videos/` 目录下的所有 `.mp4` 文件都会被处理
* 生成的 `.srt` 字幕文件保存在 `./output/` 目录

### **2️⃣ 处理结果示例（SRT 格式）**

```
1
00:00:00,000 --> 00:00:02,500
This is an example subtitle.

2
00:00:02,500 --> 00:00:05,000
The sentence is automatically split.
```

---

## ⚠️ 常见问题

### 1️⃣ `FileNotFoundError: [WinError 2] 系统找不到指定的文件`

✅ 解决方法：

* **确认 `ffmpeg` 是否安装** ，运行 `ffmpeg -version` 测试
* **Windows 可能需要重启 VSCode** ，或者运行：

```sh
  $env:Path += ";C:\ffmpeg\bin"
```

### 2️⃣ 运行 `faster-whisper` 时  **每次都下载 `model.bin`** ？

✅ 解决方法：

* **手动指定本地模型路径** ，修改 `main.py`：

```python
  model = WhisperModel("C:/Users/你的用户名/.cache/huggingface/hub/models--guillaumekln--faster-whisper-tiny", compute_type="int8")
```

---

## 📜 许可证

本项目基于 MIT 许可证发布，欢迎自由修改和使用！ 🎉
