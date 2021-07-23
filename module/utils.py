import datetime


def to_timeformat(time: datetime.datetime):
    strftime = time.strftime('%Y년 %m월 %d일 %p %I시 %M분 %S초')
    strftime = strftime.replace("AM", "오전")
    strftime = strftime.replace("PM", "오후")
    strftime = strftime.replace("am", "오전")
    strftime = strftime.replace("pm", "오후")
    return strftime


if __name__ == "__main__":
    print(to_timeformat(datetime.datetime.now()))
