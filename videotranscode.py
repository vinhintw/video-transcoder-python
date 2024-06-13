import datetime
import ffmpeg_streaming  # type: ignore
from ffmpeg_streaming import Formats, Bitrate, Representation, Size, FFProbe  # type: ignore
import sys

# ffprobe = FFProbe("https://eccms.vinhintw.com/chapter-1%2Fchapter-1.mp4")
# print(ffprobe.all())

def monitor(ffmpeg, duration, time_, time_left, process):
    per = round(time_ / duration * 100)
    sys.stdout.write("\rTranscoding...(%s%%) %s left [%s%s]"% (per,datetime.timedelta(seconds=int(time_left)),"#" * per,"-" * (100 - per),
    )
    )
    sys.stdout.flush()


# https://image.vinhintw.com/enc.key
save_to = "https://image.vinhintw.com/enc.key"
video_url = "https://eccms.vinhintw.com/chapter-1%2Fchapter-1.mp4"
video = ffmpeg_streaming.input(video_url)
url = "https://image.vinhintw.com/enc.key"
_360p = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
# _480p  = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
# _720p  = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))
_1080p = Representation(Size(1920, 1080), Bitrate(4096 * 1024, 320 * 1024))
_1440p = Representation(Size(2560, 1440), Bitrate(8192 * 1024, 320 * 1024))
hls = video.hls(Formats.h264())
hls.encryption(save_to, url)
hls.auto_generate_representations([1080, 720, 480])
hls.output("./videos/hls.m3u8", monitor=monitor)
