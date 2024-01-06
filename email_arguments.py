class MissingInputsException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class EmptyInputsException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class EmailArguments:
    __recipient: str = ''
    __cc: str = ''
    __bcc: str = ''
    __subject: str = ''
    __body: str = ''
    __file: bool = None
    __debug: bool = None
    __display: bool = None

    def __init__(self, argv: [str]):
        for arg in argv:
            option_split: [str] = arg.split("=")
            option: str = option_split[0]
            option_input: str = option_split[1] if len(option_split) > 1 and len(option_split[1].strip()) > 0 else ''
            if (len(option_split) < 2 or not option_input) and \
                    (option == "--recipient" or option == "--subject" or option == "--body"):
                raise EmptyInputsException(
                    "The arguments:\n"
                    "--recipient\n"
                    "--subject\n"
                    "--body\n"
                    "need to have specified values. Example:\n"
                    r'--recipient=john.doe@email.com --subject="Testing Email Script" --body="Hello"'
                )
            if option == "--recipient":
                self.__recipient = option_input
            elif option == "--cc":
                self.__cc = option_input
            elif option == "--bcc":
                self.__bcc = option_input
            elif option == "--subject":
                self.__subject = option_input
            elif option == "--body":
                if self.__file:
                    self.__read_body(option_input)
                else:
                    self.__body = option_input
            elif option == "--file":
                if not option_input or option_input.lower() == "true":
                    self.__file = True
                    if self.__body:
                        self.__read_body(self.__body)
                else:
                    self.__file = False
            elif option == "--debug":
                if not option_input or option_input.lower() == "true":
                    self.__debug = True
                else:
                    self.__debug = False
            elif option == "--display":
                if not option_input or option_input.lower() == "true":
                    self.__display = True
                else:
                    self.__display = False
            elif "issue" in option:
                self.__issue = option_input.strip()
            elif "title" in option:
                self.__title = option_input.strip()
            elif "template" in option:
                self.__template = option_input.strip()

        if not self.__recipient or not self.__subject or not self.__body:
            raise MissingInputsException(
                "Missing arguments, following ones are required:\n"
                "--recipient\t\tSpecifies the recipient of the email\n"
                "--subject\t\tSpecifies the subject of the email\n"
                "--body\t\t\tDefined the body of the email (if it is a path to a file, add the \"--file\" command)\n"
                "Optionally, the user can specify the following inputs:\n"
                "--cc\t\t\tCopy of this mail will be sent out also to these addresses\n"
                "--bcc\t\t\tCopy of this mail will be sent out also to these addresses, but it will not display the address in the BCC field\n"
                "--file\t\t\tSpecifies, that the body is a path to a file that can be read (e.g., an HTML file)\n"
                "--debug\t\t\tAsks the user for a confirmation of the mail before sending it out\n"
                "--display\t\tDisplays the mail in Outlook, from where the user then can send it out\n"
                "Example:\n"
                r'--recipient=john.doe@at.bosch.com --subject="Testing Email Script" --body="C:\Users\GAT1WI\Documents\Git_Repositories\email_generation\body.html" --file'
            )

    def __read_body(self, path: str):
        with open(path, 'r', encoding="utf-8") as html_body:
            self.__body = html_body.read()

    def get_recipient(self):
        return self.__recipient

    def get_cc(self):
        return self.__cc

    def get_bcc(self):
        return self.__bcc

    def get_subject(self):
        return self.__subject

    def get_body(self):
        return self.__body

    def get_debug(self):
        return self.__debug

    def get_display(self):
        return self.__display

    def __str__(self):
        return f"Recipient:\t{self.__recipient}\n" \
               f'CC:\t\t\t{self.__cc if self.__cc else ""}\n' \
               f'BCC:\t\t{self.__bcc if self.__bcc else ""}\n' \
               f"Subject:\t{self.__subject}\n" \
               f"Body:\n{self.__body}"

