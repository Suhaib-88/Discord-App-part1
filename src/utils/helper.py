import re
#---------------------------------------------AI Generation History-------------------------------------------------           

async def generate_response_with_text(message_text,model):
    try:
        prompt_parts = [message_text]
        response = model.generate_content(prompt_parts)
        if response._error:
            return "❌" + str(response._error)
        return response.text
    except Exception as e:
        return "❌ Exception: " + str(e)
            
    