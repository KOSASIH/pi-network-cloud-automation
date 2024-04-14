import time
import random

class PiCloudHealth:
    def __init__(self):
        self.system_health = 100

    def check_health(self):
        """
        Simulate a health check by generating a random number between 90 and 110.
        """
        self.system_health = random.randint(90, 110)
        print(f"Health check complete: System health is currently at {self.system_health}%.")

    def diagnose_issues(self):
        """
        Simulate diagnosing issues by generating a random number between 0 and 10.
        """
        issues = random.randint(0, 10)
        if issues > 0:
            print(f"Diagnostic complete: {issues} issues found.")
        else:
            print("Diagnostic complete: No issues found.")

    def run(self):
        """
        Continuously monitor the system health and diagnose issues.
        """
        while True:
            self.check_health()
            time.sleep(60)  # Check health every minute
            self.diagnose_issues()
            time.sleep(60)  # Diagnose issues every minute
