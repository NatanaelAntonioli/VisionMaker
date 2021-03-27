from moviepy.editor import *
import time

blink_clip = VideoFileClip("blink.mp4")
closed_clip = VideoFileClip("closed.mp4")

months_dir = r'out/months'
days_dir = r'out/days'

benchmark = True
vikings = False
real_list = False
template = True


def make_months():
    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

    i = 0

    for current_month in months:

        i = i + 1

        txt_clip = TextClip(current_month, font="Arial-Bold", fontsize=65, color='black')

        txt_clip = txt_clip.set_position((570, 263))
        txt_clip = txt_clip.set_start(0.4)
        txt_clip = txt_clip.set_duration(0.6)

        video = CompositeVideoClip([blink_clip, txt_clip])

        if i < 10:
            video.write_videofile("out/months/0" + str(i) + current_month + ".mp4")
        else:
            video.write_videofile("out/months/" + str(i) + current_month + ".mp4")

    final = VideoFileClip("out/months/01JAN.mp4")

    for current_concat in os.listdir(months_dir):

        if current_concat != "01JAN.mp4":
            final = concatenate_videoclips([final, VideoFileClip("out/months/" + current_concat)])

    final.write_videofile("out/months/FINALMONTHS.mp4")

    return final


def make_days():
    for day in range(31):

        txt_clip = TextClip(str(day + 1), font="Arial-Bold", fontsize=65, color='black', align='center')

        txt_clip = txt_clip.set_position((600, 263))
        txt_clip = txt_clip.set_start(0.4)
        txt_clip = txt_clip.set_duration(0.6)

        video = CompositeVideoClip([blink_clip, txt_clip])

        if (day + 1) < 10:
            video.write_videofile("out/days/0" + str(day + 1) + ".mp4")
        else:
            video.write_videofile("out/days/" + str(day + 1) + ".mp4")

    final_days = VideoFileClip("out/days/01.mp4")

    for current_concat in os.listdir(days_dir):

        if current_concat != "01.mp4":
            final_days = concatenate_videoclips([final_days, VideoFileClip("out/days/" + current_concat)])

    final_days.write_videofile("out/days/FINALDAYS.mp4")

    return final_days


def make_year(year):
    txt_clip = TextClip(str(year), font="Arial-Bold", fontsize=65, color='black', align='center')

    txt_clip = txt_clip.set_position((570, 263))
    txt_clip = txt_clip.set_start(0.4)
    txt_clip = txt_clip.set_duration(0.6)

    final_year = CompositeVideoClip([blink_clip, txt_clip])

    final_year.write_videofile("out/year/FINALYEAR.mp4")

    return final_year


def make_template(year):
    months = make_months()
    days = make_days()
    year = make_year(year)

    output = concatenate_videoclips([closed_clip, months])
    output = concatenate_videoclips([output, days])
    output = concatenate_videoclips([output, year])
    output = concatenate_videoclips([output, closed_clip])

    output.write_videofile("template.mp4")


def make_video(name):
    name = name.upper()

    template = VideoFileClip("template.mp4")

    txt_clip = TextClip(str(name), font="Arial-Bold", fontsize=65, color='black', align='Center')
    txt_clip = txt_clip.set_position((450, 400)).set_duration(63)

    video = CompositeVideoClip([template, txt_clip])

    video.write_videofile("names/" + name + ".mp4")

if template:

    make_template(2021)

if benchmark:
    start_time = time.time()

    make_video("Natanael Antonioli")

    print("Took " + str(round(time.time() - start_time, 2)) + " seconds.")

if vikings:

    start_time = time.time()

    with open("vikings.txt", encoding="utf-8") as file_in:
        for line in file_in:
            make_video(line.rstrip())

    print("Took " + str(round(time.time() - start_time, 2)) + " seconds.")

if real_list:

    start_time = time.time()

    with open("peoplelist.txt", encoding="utf-8") as file_in:
        for line in file_in:
            make_video(line.rstrip())

    print("Took " + str(round(time.time() - start_time, 2)) + " seconds.")
