from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime, timezone


def wait_for_page_load(driver, timeout=10):
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script('return document.readyState') == 'complete'
    )

def to_snake(input_string):
    snake_case_string = input_string.replace(' ', '_')
    snake_case_string = snake_case_string.lower()
    return snake_case_string

def convert_to_epoch_time(timestamp_str):
    try:
        timestamp_str = timestamp_str.replace('(UTC)', '').strip()
        provided_time = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        provided_time_utc = provided_time.replace(tzinfo=timezone.utc)
        epoch_time = int(provided_time_utc.timestamp())
        return epoch_time
    except ValueError as e:
        print(f"Error: {e}")
        return None