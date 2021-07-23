import datetime


def to_timeformat(time: datetime.datetime) -> str:
    """
    주어진 datetime 객체에서 문자열로 포매팅해 반환합니다.

    :param time: datetime 객체.
    :return: 포매팅된 시간 문자열.
    """
    strftime = time.strftime('%Y년 %m월 %d일 %p %I시 %M분 %S초')
    strftime = strftime.replace("AM", "오전")
    strftime = strftime.replace("PM", "오후")
    strftime = strftime.replace("am", "오전")
    strftime = strftime.replace("pm", "오후")
    return strftime


if __name__ == "__main__":
    print(to_timeformat(datetime.datetime.now()))
