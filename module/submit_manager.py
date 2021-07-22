from contextlib import suppress
from typing import Dict, Optional, Union
from submits import submits, approved_submits, Bot


class SubmitManager:
    def __init__(self):
        self.submits = submits
        self.approved_submits = approved_submits

    def get_submits(self) -> Dict[int, Bot]:
        return {x.id: x for x in self.submits}

    def get_submit(self, query: int, safe: bool = True) -> Optional[Bot]:
        subs = self.get_submits()
        if query not in subs:

            if query < 1000000000:  # Maximum ID num is 1000000000
                # Maybe it is index?
                with suppress(IndexError):
                    return self.submits[query-1]
            if safe:
                return None
            else:
                raise KeyError("bot not found")
        return subs[query]

    def __del_from_list(self, query: int) -> Optional[Bot]:
        if isinstance(query, Bot):
            query = query.id
        subs = self.get_submits()
        if query not in subs:
            return None
        bot = subs.pop(query)
        self.submits.remove(bot)
        return bot

    def approve(self, query: Union[int, Bot], safe: bool = True) -> Optional[Bot]:
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
        if isinstance(query, Bot):
            query = query.id
        res = self.__del_from_list(query)
        if not res:
            if safe:
                return None
            else:
                raise KeyError("bot not found")
        return res
