from faster_whisper import WhisperModel

def transcribe_audio(audio_path, model_size="tiny"):
    """使用 faster-whisper 进行语音识别"""
    model = WhisperModel(model_size, compute_type="int8")
    segments, _ = model.transcribe(audio_path)

    subtitles = []
    for i, segment in enumerate(segments):
        start_time = segment.start
        end_time = segment.end
        text = segment.text.strip()
        subtitles.append((i + 1, start_time, end_time, text))
    
    return subtitles
