# content of test_yield2.py

import smtplib
import pytest

@pytest.fixture(scope="module")
def smtp():
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as smtp:
        yield smtp  # provide the fixture value