from models import MyObservation
from inference import run_inference

class MyEnvironment:
    def __init__(self):
        self.state = {}

    def reset(self, seed=None):
        self.state = {"status": "ready"}
        return MyObservation(
            echoed_message="Environment reset successfully",
            message_length=0
        )

    def step(self, action):
        # Action se message lo
        if hasattr(action, 'message'):
            message = action.message
        elif isinstance(action, dict):
            message = action.get("message", "")
        else:
            message = ""
        
        # inference.py se email generate
        result = run_inference(message)
        email_content = result["data"]["email"]
        
        # ✅ Return MyObservation object
        return MyObservation(
            echoed_message=email_content,
            message_length=len(message)
        )

    async def step_async(self, action):
        return self.step(action)

    def close(self):
        pass