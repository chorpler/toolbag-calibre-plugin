import unicodedata
import re

ALLOWED = [ '–', '—', '‘', '’', '“', '”', '•', '…', '·', '•', '►', '█', '■', '♦', ]

def remove_unicode(obj: str) -> str:
    # if isinstance(obj, dict):
        # return {remove_unicode(key): remove_unicode(value) for key, value in obj.items()}
    # elif isinstance(obj, str):
    stripped = ""
    if isinstance(obj, str):
        for c in obj:
            if c in ALLOWED:
                stripped += c
            else:
                stripped += c.encode('ascii', 'ignore').decode('ascii')
        #         obj = obj.replace(c, '')
        # return obj.encode('ascii', 'ignore').decode('ascii')
    return stripped

# # Example usage
# my_dict = {'key': 'valüe', 'këy2': {'kêy3': 'vàlue3'}}
# cleaned_dict = remove_unicode(my_dict)
# print(cleaned_dict)

def strip_zalgo(text: str, max_combining_marks: int=1) -> str:
    """
    Removes or limits excessive Unicode combining characters (Zalgo text).

    Args:
        text (str): The input string potentially containing Zalgo text.
        max_combining_marks (int): The maximum number of consecutive
                                   combining marks to allow per base character.

    Returns:
        str: The cleaned string with Zalgo marks removed or limited.
    """
    cleaned_text = []
    current_combining_count = 0

    data = str(text, encoding='utf-8') if isinstance(text, bytes) else text
    for char in data:
        if unicodedata.category(char).startswith('M'):  # Check if it's a combining mark
            if current_combining_count < max_combining_marks:
                cleaned_text.append(char)
                current_combining_count += 1
        else:
            cleaned_text.append(char)
            current_combining_count = 0  # Reset count for a new base character

    return "".join(cleaned_text)

# Example Usage:
# zalgo_text = "H̛̛͠ȩl̨̀͞l̨̨͘ơ̧ W͠͡͠or̶͜ld̀"
# stripped_text = strip_zalgo(zalgo_text, max_combining_marks=1)
# stripped_2 = strip_zalgo(stripped_text)
# stripped_3 = strip_zalgo(stripped_2)
# print(f"Original: {zalgo_text}")
# print(f"Stripped 1: {stripped_text}")
# print(f"Stripped 2: {stripped_2}")
# print(f"Stripped 3: {stripped_3}")

# # Alternative: Removing all combining marks
# def remove_all_combining_marks(text):
#     return ''.join(char for char in text if not unicodedata.category(char).startswith('M'))

# completely_stripped = remove_all_combining_marks(zalgo_text)
# print(f"Completely stripped: {completely_stripped}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Strip accents from a string.")
    parser.add_argument("input_file", type=str, help="Path to the input file.")
    args = parser.parse_args()

    with open(args.input_file, "r", encoding="utf-8") as f:
        text = f.read()

    result = remove_unicode(text)
    print(result)


