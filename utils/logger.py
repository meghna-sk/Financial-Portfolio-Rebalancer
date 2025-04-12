tool_log = []

def log_tool_usage(tool_name):
    tool_log.append(tool_name)

def get_tool_log():
    return tool_log

def reset_tool_log():
    tool_log.clear()