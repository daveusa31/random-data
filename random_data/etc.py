from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

from . import functions

numbers = "0123456789"
words = "abcdefghinopqrstuvyxwz"
special_chars = "!?@$"


_operating_systems = {
    "windows": OperatingSystem.WINDOWS.value,
    "linux": OperatingSystem.LINUX.value,
}
_software_names = {
    "chrome": SoftwareName.CHROME.value,
}


def password(length=15, number=True, word=True, special_char=False, upper=True):
    symbols = ""

    symbols += numbers if number else ""
    symbols += words if word else ""
    symbols += special_chars if special_char else ""

    if upper:
        symbols = symbols.upper()

    symbols = list(symbols)

    while True:
        _password = "".join(functions.random_element(symbols) for _ in range(length))

        if functions.list_in_string(_password, special_chars):
            break
        if not functions.list_in_string(_password, special_chars):
            continue

    return _password


def uuid(parts=4, length=4):
    _uuid = "".join(password(length=length, upper=False) + "-" for _ in range(parts))

    _uuid = _uuid.strip("-")
    return _uuid


def user_agent(operating_systems=["windows"], software_names=["chrome"]):
    __software_names = [_software_names[system] for system in software_names]
    __operating_systems = [_operating_systems[system] for system in operating_systems]

    user_agent_rotator = UserAgent(
        software_names=__software_names,
        operating_systems=__operating_systems,
        limit=100,
    )

    _user_agent = user_agent_rotator.get_random_user_agent()
    return _user_agent
