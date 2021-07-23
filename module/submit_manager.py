from contextlib import suppress
from typing import Dict, Optional, Union, List
from submits import submits, approved_submits, Bot


class SubmitManager:
    """
    봇 신청 매니저 입니다.

    :ivar submits: 승인 대기중인 봇 리스트.
    :ivar approved_submits: 승인된 봇 리스트.
    """
    def __init__(self):
        self.submits: List[Bot] = submits
        self.approved_submits: List[Bot] = approved_submits

    def get_submits(self) -> Dict[int, Bot]:
        """
        봇 신청 리스트를 ID: Bot 형식의 dict로 반환합니다.
        :return: Dict[int, submits.Bot]
        """
        return {x.id: x for x in self.submits}

    def get_submit(self, query: int, safe: bool = True) -> Optional[Bot]:
        """
        봇 신청 객체를 query 파라메터에 따라 가져옵니다. 봇이 존재하지 않는 경우 ``None``을 반환합니다.

        :param query: 봇 ID 또는 신청 순서.
        :param safe: 봇이 존재하지 않는 경우, 이 값이 ``True``일 경우에는 ``None``을 반환하고, ``False``인 경우에는 예외를 발생시킵니다.
        :return: Optional[submits.Bot]
        :raises: KeyError - 봇이 존재하지 않습니다.
        """
        subs = self.get_submits()
        if query not in subs:
            if query < 1000000000:  # Maximum ID value is 1000000000
                # Maybe it is index?
                with suppress(IndexError):
                    return self.submits[query-1]
            if safe:
                return None
            else:
                raise KeyError("bot not found")
        return subs[query]

    def __del_from_list(self, query: int) -> Optional[Bot]:
        """
        SubmitManager 내부 전용 함수입니다. 봇 신청 리스트에서 해당 봇을 삭제합니다. 봇이 존재하지 않다면 ``None``을 반환하고,
        삭제에 성공했다면 해당 봇을 반환합니다.
        :return: Optional[submits.Bot]
        """
        if isinstance(query, Bot):
            query = query.id
        subs = self.get_submits()
        if query not in subs:
            return None
        bot = subs.pop(query)
        self.submits.remove(bot)
        return bot

    def approve(self, query: Union[int, Bot], safe: bool = True) -> Optional[Bot]:
        """
        봇 신청을 승인합니다. 성공적으로 승인했다면 승인한 봇 객체를 반환합니다.

        :param query: 봇 ID 또는 봇 객체.
        :param safe: 봇이 존재하지 않는 경우, 이 값이 ``True``일 경우에는 ``None``을 반환하고, ``False``인 경우에는 예외를 발생시킵니다.
        :return: Optional[submits.Bot]
        :raises: KeyError - 봇이 존재하지 않습니다.
        """
        if isinstance(query, Bot):
            query = query.id
        res = self.__del_from_list(query)
        if not res:
            if safe:
                return None
            else:
                raise KeyError("bot not found")
        self.approved_submits.append(res)
        return res

    def deny(self, query: Union[int, Bot], safe: bool = True) -> Optional[Bot]:
        """
        봇 신청을 거부합니다. 성공적으로 거부했다면 거부한 봇 객체를 반환합니다.

        :param query: 봇 ID 또는 봇 객체.
        :param safe: 봇이 존재하지 않는 경우, 이 값이 ``True``일 경우에는 ``None``을 반환하고, ``False``인 경우에는 예외를 발생시킵니다.
        :return: Optional[submits.Bot]
        :raises: KeyError - 봇이 존재하지 않습니다.
        """
        if isinstance(query, Bot):
            query = query.id
        res = self.__del_from_list(query)
        if not res:
            if safe:
                return None
            else:
                raise KeyError("bot not found")
        return res
