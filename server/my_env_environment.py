import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models import MyObservation

class MyEnvironment:
    def __init__(self):
        self.state = {}

    def reset(self, seed=None):
        self.state = {"status": "ready"}
        # ✅ Return MyObservation object
        return MyObservation(
            echoed_message="Environment reset successfully",
            message_length=0
        )

    async def reset_async(self, seed=None):
        """Async version of reset"""
        return self.reset(seed)

    def step(self, action):
        # Action se message lo
        if hasattr(action, 'message'):
            message = action.message
        elif isinstance(action, dict):
            message = action.get("message", "")
        else:
            message = ""
        
        # Email generate
        email = f"""
Subject: Leave Request

Dear Sir/Madam,

I need leave for 2 days.

Reason: {message}

Kindly approve my request.

Thank you.

Regards,
Employee
"""
        
        # ✅ Return MyObservation object
        return MyObservation(
            echoed_message=email.strip(),
            message_length=len(message)
        )

    async def step_async(self, action):
        return self.step(action)

    def close(self):
        pass