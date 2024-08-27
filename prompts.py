character_description_prompt = "Resume in a few words all you know about the character whose name can be writen as: "
system_message = f"""You are a helpful assistant you have access to a list of characters names from a novel where some characters might appear more than once with a different name variation, your job is to put together all the names of each character and return a list with all the character and for each character the different names found. Use this format:
1.James: Jaemy, Mr. James Smith, James Smith.
2.Anna
"""
system_message_metric="You are a helpfull assistant, you job is to determinate if two descriptions match, in case both descriptions are similar you must retunr a 1, otherwise just a 0. Return only the numeric value."
