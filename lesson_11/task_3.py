import re
from typing import List


class EmailValidator:
    """class Validator"""

    PATTERN = r'[^._"][\d\w]+[^._]@[^-.][\d\w.-]{,63}[^.].([a-z]){2,3}'
    regexp = re.compile(PATTERN)

    def __init__(self) -> None:
        self.valid_emails: List[str] = []
        self.invalid_emails: List[str] = []

    def is_valid_email(self, email_str: str) -> bool:
        return bool(self.regexp.match(email_str))

    def check_list_of_emails(self, email_list: List[str]) -> None:
        for email in email_list:
            if self.is_valid_email(email):
                self.valid_emails.append(email)
            else:
                self.invalid_emails.append(email)


validator = EmailValidator()

with open("emails.in", "r", encoding="utf-8") as file_emails:
    emails = [email.strip() for email in file_emails.readlines()]

validator.check_list_of_emails(emails)

with open("emails.out", "w", encoding="utf-8") as file_emails:
    file_emails.write("VALID EMAILS:\n")
    file_emails.writelines(email + "\n" for email in validator.valid_emails)
    file_emails.write("\nINVALID EMAILS:\n")
    file_emails.writelines(email + "\n" for email in validator.invalid_emails)
