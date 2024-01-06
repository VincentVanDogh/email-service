<h1 align="center">Email Generation Script</h1>

<span style="display: flex; justify-content: center">
    <img src="resources/python-logo.png" height="72px">
    <img src="resources/html-logo.png" height="72px">
    <img src="resources/css-logo.png" height="72px">
</span>

## Overview

The email generation script serves the purpose of being able to send out emails automatically to any recipient with
a self definable subject and body.

## How to use

### Default

The user has to specify the following inputs when executing the script over the command line:
* --recipient 
* --subject
* --body

| Input       | Explained                                                                                                                                                                       |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --recipient | Specifies the recipient(s) of the mail. To specify more than one recipient, connect the recipients using semicolons (;), e.g., --recipient=alfa@at.bosch.com;bravo@at.bosch.com |
| --subject   | Specifies the subject of the mail                                                                                                                                               |
| --body      | Specifies the body of the mail (to link to a template, additionally add `--file`                                                                                                |


Additionally, the user has the option to specify further mail inputs:
* --cc
* --bcc
* --file
* --debug
* --display

| Input     | Explained                                                                                                   |
|-----------|-------------------------------------------------------------------------------------------------------------|
| --cc      | Carbon Copy                                                                                                 |
| --bcc     | Blind Carbon Copy                                                                                           |
| --file    | If set to "true" or just typed, will read the body as a path to an expected file                            |
| --debug   | Gives the user to check and confirm his/her inputs after executing the script                               |
| --display | Displays the email in outlook, giving the user the option to check the content and then manually sending it |

### Example
```cmd
python main.py --recipient="alfa@email.com" --subject="test" --body="<h1>Hello</h1><div>How are you doing?</div>"
```
