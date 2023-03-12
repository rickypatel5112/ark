import speedtest

try:
    speed_test = speedtest.Speedtest()
except Exception as e:
    print("No network found for speed test")

def get_download_speed():
    return str(round(speed_test.download()/(10 ** 6), 2)) + " mb p s"

def get_upload_speed():
    return str(round(speed_test.upload()/(10 ** 6), 2)) + " mb p s"
