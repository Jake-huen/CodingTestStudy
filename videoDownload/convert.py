import subprocess

def convert_ts_to_mp4(title):

    infile = f'{title}.ts'
    outfile = f'{title}.mp4'

    subprocess.run(['ffmpeg', '-i', infile, outfile])


def convert_ts_to_mp3(title):
    infile = f'{title}.ts'
    outfile = f'{title}.mp3'

    subprocess.run(['ffmpeg', '-i', infile, outfile])
