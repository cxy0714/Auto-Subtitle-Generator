# 人工语言

为了搬运YouTube的[Online Causal Inference Seminar](https://www.youtube.com/@onlinecausalinferencesemin2364/videos)讲座到[B站](https://space.bilibili.com/439010560/lists)，进而可以吃饭的时候看B站，但是字幕处理是个问题。

Chatgpt写完了所有代码，在我的轻薄本笔记本上一次跑通！本地部署的 `faster-whisper-tiny`只用cpu就可以做到英语自动识别的好效果，中文翻译b站已经有了，可以双语字幕。

[为祂献上膝盖！Chatgpt聊天记录](https://chatgpt.com/share/67a24602-4368-8006-8201-b6a8fa16a53c)

下载YouTube视频的免费快速在线1080P网址：

[下载Youtube](https://ddownr.com/zh7H/youtube-video-downloader)

## 🔗主要参考：

如何得知自动语言处理的whisper：[PotPlayer播放器创建有声字幕以及实时字幕翻译](https://blog.csdn.net/duke_ding2/article/details/144973709)

faster-whisper-tiny产生的字幕过长之后的处理参考：[SubtitleSpliter](https://github.com/WEIFENG2333/SubtitleSpliter)

另一个项目（一款基于大语言模型(LLM)的视频字幕处理助手，支持语音识别、字幕断句、优化、翻译全流程处理）：[VideoCaptioner项目](https://github.com/WEIFENG2333/VideoCaptioner)的第一部分视频转码我总是失败，不得已而让GPT重新手搓。

# Auto-Subtitle-Generator（Chatgpt4o初稿，claude3.5Sonnet润色，Deepseek服务器繁忙）

一个基于 faster-whisper 的自动视频字幕生成工具，支持批量处理视频并生成优化后的 SRT 字幕文件。

## ✨ 特性

- 📺 支持批量处理 MP4 视频文件
- 🎯 使用 faster-whisper-tiny 模型进行高效语音识别
- 🔄 自动优化字幕长度（单行不超过12个单词）
- 💪 仅需 CPU 即可运行，适合轻量级设备
- 🌍 支持英语语音识别

## 🛠 项目结构

```
📂 Auto-Subtitle-Generator
├── 📂 videos               # 存放待处理视频
├── 📂 output               # 生成的字幕文件（SRT）
├── 📂 utils                # 工具函数
│   ├── audio_utils.py      # 音频处理（提取音频）
│   ├── asr_utils.py        # 语音识别（faster-whisper）
│   ├── srt_utils.py        # SRT处理（字幕分割）
├── main.py                 # 入口脚本
├── requirements.txt        # 依赖库
├── README.md              # 说明文档
```

## 📥 安装步骤

### 前置要求

- Python 3.8+
- FFmpeg
- 约 1GB 磁盘空间（用于模型文件）

### 1. 安装 Python 依赖

```bash
pip install -r requirements.txt
```

### 2. 安装 FFmpeg

#### Windows：

1. 从 [FFmpeg官网](https://www.gyan.dev/ffmpeg/builds/) 下载
2. 解压并将 `bin` 目录添加到系统环境变量
3. 验证安装：`ffmpeg -version`

#### Linux/macOS：

```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg
```

### 3. （可选）预下载模型

```bash
mkdir -p ~/.cache/huggingface/hub
wget -P ~/.cache/huggingface/hub https://huggingface.co/guillaumekln/faster-whisper-tiny/resolve/main/model.bin
```

## 🚀 使用方法

1. 将视频文件放入 `videos` 目录
2. 运行程序：

```bash
python main.py ./videos ./output
```

3. 生成的字幕文件将保存在 `output` 目录

## ❗ 常见问题

### FFmpeg 未找到

**问题**：`FileNotFoundError: [WinError 2] 系统找不到指定的文件`
**解决**：

- 确认 FFmpeg 安装：运行 `ffmpeg -version`
- Windows 用户需重启 VSCode 或运行：

```powershell
$env:Path += ";C:\ffmpeg\bin"
```

### 模型下载问题

模型文件会在首次运行时自动下载并缓存，后续运行无需重复下载。

## 📄 许可证

本项目基于 MIT 许可证开源。
