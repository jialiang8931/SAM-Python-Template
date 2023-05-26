from components import alarm
from constants import setting

def lambda_handler(event, context):
    alarm.main(test_mode=setting.test_mode)
    return 
