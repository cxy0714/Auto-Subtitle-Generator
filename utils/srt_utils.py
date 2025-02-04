import re

def format_time(seconds):
    """将秒转换为 SRT 时间格式"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

def split_subtitle(index, start_time, end_time, text, max_words=12):
    """切分字幕，保证每段不超过 max_words 个单词"""
    words = text.split()
    if len(words) <= max_words:
        return [(index, format_time(start_time), format_time(end_time), text)]

    num_splits = (len(words) // max_words) + (1 if len(words) % max_words != 0 else 0)
    duration_per_split = (end_time - start_time) / num_splits

    split_subs = []
    for i in range(num_splits):
        sub_start = start_time + i * duration_per_split
        sub_end = start_time + (i + 1) * duration_per_split
        sub_text = " ".join(words[i * max_words : (i + 1) * max_words])
        split_subs.append((f"{index}.{i+1}", format_time(sub_start), format_time(sub_end), sub_text))

    return split_subs

def save_srt(subtitles, output_path):
    """将字幕保存为 SRT 文件"""
    with open(output_path, "w", encoding="utf-8") as file:
        for index, start_time, end_time, text in subtitles:
            file.write(f"{index}\n{start_time} --> {end_time}\n{text}\n\n")
