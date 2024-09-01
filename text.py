from moviepy.editor import VideoFileClip
import os

def split_video(video_path, num_parts):
    # 加载视频
    clip = VideoFileClip(video_path)
    duration = clip.duration
    part_duration = duration / num_parts

    # 分割视频
    for i in range(num_parts):
        start_time = i * part_duration
        end_time = (i + 1) * part_duration if i < num_parts - 1 else duration
        subclip = clip.subclip(start_time, end_time)

        # 构建输出文件名
        output_filename = f"{os.path.splitext(video_path)[0]}{i+1}.mp4"

        # 保存分割的视频
        subclip.write_videofile(output_filename, codec='libx264', verbose=False, ffmpeg_params=['-loglevel', 'panic'])

        print(f"完成分割: {output_filename}")

    clip.close()

# 设置视频文件路径为绝对路径
video_file = 'E:/liruii01234/program/xiangmu/HTML/sp/b.mp4'

# 调用函数，分割视频
split_video(video_file, 5)
