import os
import re


def __get_signature() -> str:
    with open(
            os.path.join(os.getenv('APPDATA'), r"Microsoft\Signatures\eForms-External.htm"), encoding="UTF-8"
    ) as fp:
        text = fp.read().replace("\n", " ")
        reg = re.compile(r'.*<body>(.*?)</body>', re.MULTILINE)
        match = reg.match(text)
        return """<p class="MsoNormal">""" + match.group(1) + """</p>""" if match else ""
