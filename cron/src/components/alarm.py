from constants import setting
from utils.line_notify import broadcaster

def main(test_mode=False):
    broadcaster.publish(token=setting.notify_token, message="test123")
    return True

# 測試模組用
if __name__ == "__main__":
    main(test_mode=True)
