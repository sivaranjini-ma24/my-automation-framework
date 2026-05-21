import pytest
import os
from datetime import datetime

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This hook checks the outcome of every test step execution
    outcome = yield
    report = outcome.get_result()
    
    # If a test case fails during its execution phase
    if report.when == "call" and report.failed:
        # Get the running Playwright page fixture instance
        page = item.funcargs.get("page")
        if page:
            # Create a screenshots folder if it doesn't exist
            os.makedirs("screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"screenshots/fail_{item.name}_{timestamp}.png"
            # Capture the visual state of the browser
            page.screenshot(path=screenshot_path)
            print(f"\n Captured failure screenshot saved to: {screenshot_path}")
