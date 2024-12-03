import glob
pattern = ".pmk"
fw_files = glob.glob(f'**/*{pattern}', recursive=True)
with open('dir.txt', 'w') as f:
    f.writelines([fw_file.replace("\\", "/") + "\n" for fw_file in fw_files])
