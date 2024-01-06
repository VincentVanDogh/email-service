import sys
import win32com.client as win32
from email_arguments import EmailArguments, MissingInputsException, EmptyInputsException


def generate_email(recipient: str, cc: str, bcc: str, subject: str, body: str, display: bool) -> None:
    """
    Main method of this script - it fills out all email inputs and sends it out
    :param recipient: recipient of the email
    :param cc: copy of the email will be sent out also to these addresses
    :param bcc: copy of the email will be sent out also to these addresses, but it will not be displayed in bcc
    :param subject: subject of the email
    :param body: body of the email
    :param display: specifies whether the email should be displayed by Outlook. If set to false, it is instantly sent out
    """
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.CC = cc if cc else ""
    mail.BCC = bcc if bcc else ""
    mail.Subject = subject
    mail.HtmlBody = body
    if display:
        mail.Display(False)
    else:
        mail.Send()


if __name__ == '__main__':
    try:
        inputs: EmailArguments = EmailArguments(sys.argv)
    except MissingInputsException as e:
        print(e.message)
        sys.exit()
    except EmptyInputsException as e:
        print(e.message)
        sys.exit()

    arg_recipient: str = inputs.get_recipient()
    arg_cc: str = inputs.get_cc()
    arg_bcc: str = inputs.get_bcc()
    arg_subject: str = inputs.get_subject()
    arg_body: str = inputs.get_body()
    debug: bool = inputs.get_debug()
    display: bool = inputs.get_display()

    if debug:
        while True:
            print(inputs.__str__())
            user_resp: str = input("\nDo you want to send out this mail?\n[Y]es/[N]o: \n").strip().lower()
            if user_resp == "y" or user_resp == "yes":
                print("\nGenerating Email")
                generate_email(arg_recipient, arg_cc, arg_bcc, arg_subject, arg_body, display)
                break
            else:
                print("\nCanceling Email")
                break
    else:
        generate_email(arg_recipient, arg_cc, arg_bcc, arg_subject, arg_body, display)

    print("Email generation process finished")
