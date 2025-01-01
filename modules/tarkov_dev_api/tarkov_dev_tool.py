from langchain.tools import tool
import tarkov_dev_queryer

@tool
def get_all_quests_tool() -> str:
    """
    Retrieve all quests from the Tarkov API, including their objectives and related details.
    """
    try:
        response = get_all_quests()
        return format_response(response)
    except Exception as e:
        return f"An error occurred: {str(e)}"


@tool
def get_item_data_tool(item_name: str) -> str:
    """
    Retrieve detailed information about a specific item by name from the Tarkov API.
    """
    try:
        response = get_item_data(item_name)
        return format_response(response)
    except Exception as e:
        return f"An error occurred: {str(e)}"


@tool
def get_all_item_data_tool() -> str:
    """
    Retrieve information about a predefined item (e.g., 'colt m4a1') from the Tarkov API.
    """
    try:
        response = get_all_item_data()
        return format_response(response)
    except Exception as e:
        return f"An error occurred: {str(e)}"


@tool
def get_server_status_tool() -> str:
    """
    Retrieve the current server status and related messages from the Tarkov API.
    """
    try:
        response = get_server_status()
        return format_response(response)
    except Exception as e:
        return f"An error occurred: {str(e)}"

def format_response(response):
    """
    Formats the response from the API into a readable string.
    """
    if not response or 'data' not in response:
        return "No data available or invalid response."

    formatted = ""
    for key, value in response['data'].items():
        formatted += f"{key}:\n"
        if isinstance(value, list):
            for item in value:
                formatted += f"- {item}\n"
        elif isinstance(value, dict):
            for sub_key, sub_value in value.items():
                formatted += f"  {sub_key}: {sub_value}\n"
        else:
            formatted += f"  {value}\n"

    return formatted.strip()
