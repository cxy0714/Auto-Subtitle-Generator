import subprocess
import os

def extract_audio(mp4_path, output_wav_path):
    """使用 ffmpeg 从 MP4 文件中提取音频并保存为 WAV 文件"""
    command = [
        "ffmpeg", "-i", mp4_path, "-ac", "1", "-ar", "16000", "-vn", output_wav_path, "-y"
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_wav_path
