from mido import MidiFile
from time import sleep
# from PIL import Image, ImageDraw, ImageFont
import Tkinter as tk
udw = MidiFile('/home/wend/Music/MusicProduction/UeberDenWolken.midi')
from copy import deepcopy

# for i, track in enumerate(udw.tracks):
#     print('Track {}: {}'.format(i, track.name))
#     for msg in track:
#         print(msg)

melody_events = []
for msg in udw.tracks[2]:
    try:
        melody_events.append([msg.channel, msg.note, msg.type, msg.velocity, msg.time])
    except:
        pass

melody_events_3 = melody_events# + melody_events + melody_events
# for event in melody_events_3:
#     print(event)

time_cumulated_melody_events = [melody_events_3[0]]
for idx, event in enumerate(melody_events_3[1:]):
    try:
        event[4] = event[4] + time_cumulated_melody_events[idx][4]
    except:
        print('cumulate time failed at ', idx)
    time_cumulated_melody_events.append(event)

# print(len(melody_events_3))


# print(len(time_cumulated_melody_events))
# print('\ncumulated melody events \n')
# for event in time_cumulated_melody_events:
#     print(event)

text_events = []
for chorus in range(3,4):
    for msg in udw.tracks[chorus]:
        try:
            text_events.append([msg.text, msg.time])
        except:
            pass

time_cumulated_text_events = [text_events[0]]
for idx, event in enumerate(text_events[1:]):
    event[1] = event[1] + time_cumulated_text_events[idx][1]
    time_cumulated_text_events.append(event)

# print(len(text_events))
# print(len(time_cumulated_text_events))

# print('\ncumulated text events \n')
# for event in time_cumulated_text_events:
#     print(event)

# align the cumulated events
combined_events = sorted(time_cumulated_melody_events + time_cumulated_text_events, key=lambda x: x[-1])

# print('\ncombined events \n')
# for event in combined_events:
#     print(event)

# combine by ticks
by_ticks = [ [0, [], []] ]  # only the time and an empty list for the music events
for event in combined_events:
    if event[-1] == by_ticks[-1][0]:
        #  the current event matches the latest tick
        if len(event) == 5:  # a music event
            (by_ticks[-1][1]).append(event)
        else:  # a text event
            by_ticks[-1][2] = event
    else:  # this is a new tick
        new_tick = [event[-1], [], []]
        if len(event) == 5:  # a music event
            (new_tick[1]).append(event)
        else:  # a text event
            new_tick[2] = event
        by_ticks.append(new_tick)

# print('\ncombined events collected\n')
# for tick in by_ticks:
#     print(tick)

# convert to relative milliseconds
# in the music there is no bpm, for this example I guess quarter note = 60 is OK, so since apparently
# one eights corresponds to 192 MIDI ticks and at the quarter note is 1s the eights is 500 ms
# the factor MIDI tick to one ms is 500 / 192, i.e. 2.60416 with sufficient precision, 2.6 probably also good enough

# first make it relative based on the integer ticks (loss free)
by_ticks_relative = deepcopy(by_ticks)
for idx in range(len(by_ticks_relative) - 1):
    by_ticks_relative[idx + 1][0] = by_ticks[idx + 1][0] - by_ticks[idx][0]

print('\nby ticks relative MIDI\n')
for tick in by_ticks_relative:
    print(tick)

# now convert to ms
midi2ms = 2.60416  # this is a candidate for an interactive element in the player, a speed slider or so
by_milliseconds = []
for tick in by_ticks_relative:
    tick[0] = int(round(midi2ms * tick[0]))
    by_milliseconds.append(tick)

for tick in by_milliseconds:
    print(tick)

# almost, but not quite
# make a version with ms clock ticks the speed of scrolling text and that has a fifo for text aligned according to time
# text is appended to the fifo according to the relative times (say text for 3-5 seconds)


# https://stackoverflow.com/questions/34166367/how-to-correctly-convert-midi-ticks-to-milliseconds

# play the combined events, music in the synthesizer, text in the tkinter widget



# img1 = Image.new('RGB', (1600, 900), color = 'white')
# d = ImageDraw.Draw(img1)
# # use a truetype font
# font = ImageFont.truetype("arial.ttf", 36)
# d.text((10,10), "Wind", fill=(0,0,128), font=font)
# d.text((200,10), "Nord", fill=(0,0,128), font=font)
# img1.show()
# sleep(1)
# # img2 = Image.new('RGB', (1600, 900), color = 'white')
# # d = ImageDraw.Draw(img2)
# # d.text((10,10), "Wind", fill=(0,0,128), font=font)
# # d.text((200,10), "Nord", fill=(0,0,128), font=font)
# d.text((400,10), "Ost", fill=(164,0,164), font=font)
# d.text((600,10), "Start", fill=(0,0,128), font=font)
# d.text((800,10), "Bahn", fill=(0,0,128), font=font)
#
# img1.show()

syllables = ["4", "3", "2", "1", "Wind", "nord", "ost", "start", "bahn", "eins", "drei"]
# def play_text():
#     for idx in range(len(syllables)):
#         syl.config(text=syllables[idx])
#         print(syllables[idx])
#         sleep(1)
#
# # mw = tk.Tk()
# # to rename the title of the window
# mw.title("Ueber den Wolken")
# mw.geometry("1500x100")
# mw.resizable(0, 0)
# # pack is used to show the object in the window
# label_play = tk.Label(mw, text = "Play").pack()
# label_stop = tk.Label(mw, text = "Stop").pack()
# label_running_text_1 = tk.Label(mw, text = "Wind", command=play_fn).pack()
# label_running_text_2 = tk.Label(mw, text = "Nord").pack()
# mw.mainloop()

# def write_slogan():
#     print("Tkinter is easy to use!")
#
# root = tk.Tk()
# frame = tk.Frame(root)
# frame.pack()
#
# button = tk.Button(frame,
#                    text="QUIT",
#                    fg="red",
#                    command=quit)
# button.pack(side=tk.LEFT)
# slogan = tk.Button(frame,
#                    text="Play",
#                    command=play_text)
# slogan.pack(side=tk.LEFT)
# syl = tk.Button(frame,
#                    text="Song")
# syl.pack(side=tk.LEFT)
#
# root.mainloop()

# counter = 0
# def counter_label(label):
#   counter = 0
#   def count():
#     global counter
#     counter += 1
#     label.config(text=str(counter))
#     label.after(1000, count)
#   count()
#
#
# root = tk.Tk()
# root.title("Counting Seconds")
# label = tk.Label(root, fg="dark green")
# label.pack()
# counter_label(label)
# button = tk.Button(root, text='Stop', width=25, command=root.destroy)
# button.pack()
# root.mainloop()

# syllable_labels = []
# syllable_index = 0
#
# def new_syllable():
#     global syllable_labels
#     global syllable_index
#     syllable_labels.append(tk.Label(root, fg="dark green"))
#     syllable_labels[-1].pack()
#
# counter = 0
# def counter_label(label):
#   counter = 0
#   def count():
#     global counter
#     if counter % 10 == 0:
#         new_syllable()
#     counter += 1
#     label.config(text=syllables[0])
#     label.place(x=1400-counter, y=50, width=100, height=25)
#     label.after(20, count)
#   count()
#
# root = tk.Tk()
# root.title("Counting Seconds")
# root.geometry("1500x100")
# label = tk.Label(root, fg="dark green")
# label.pack()
# counter_label(label)
# button = tk.Button(root, text='Stop', width=25, command=root.destroy)
# button.pack()
# root.mainloop()