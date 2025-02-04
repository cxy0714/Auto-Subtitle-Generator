import os
import sys
from utils.audio_utils import extract_audio
from utils.asr_utils import transcribe_audio
from utils.srt_utils import split_subtitle, save_srt

def process_video(mp4_path, output_dir):
    """处理单个视频，生成 SRT 文件"""
    print(f"正在处理: {mp4_path}")
    
    audio_path = os.path.join(output_dir, os.path.splitext(os.path.basename(mp4_path))[0] + ".wav")
    srt_path = os.path.join(output_dir, os.path.splitext(os.path.basename(mp4_path))[0] + ".srt")

    extract_audio(mp4_path, audio_path)
    
    raw_subtitles = transcribe_audio(audio_path)
    
    final_subtitles = []
    for index, start_time, end_time, text in raw_subtitles:
        final_subtitles.extend(split_subtitle(index, start_time, end_time, text))

    save_srt(final_subtitles, srt_path)
    print(f"✅ 处理完成: {srt_path}")

def process_folder(folder_path, output_dir):
    """批量处理文件夹中的所有 MP4 文件"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    mp4_files = [f for f in os.listdir(folder_path) if f.endswith(".mp4")]
    
    if not mp4_files:
        print("❌ 该文件夹中没有找到 MP4 文件")
        return

    for mp4 in mp4_files:
        process_video(os.path.join(folder_path, mp4), output_dir)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("❌ 用法: python main.py [输入文件夹] [输出文件夹]")
    else:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        process_folder(input_folder, output_folder)
