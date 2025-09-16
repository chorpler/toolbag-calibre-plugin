try:
    from unidecode import unidecode
except ImportError:
    try:
        from .unidecode import unidecode
    except ImportError:
        raise ImportError("The 'unidecode' library is required for this plugin to function. Please install it via pip.")

def strip_accents(text: str) -> str:
    """
    Removes accents and diacritics from a string.
    """
    return unidecode(text)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Strip accents from a string.")
    parser.add_argument("input_file", type=str, help="Path to the input file.")
    args = parser.parse_args()

    with open(args.input_file, "r", encoding="utf-8") as f:
        text = f.read()

    result = strip_accents(text)
    print(result)

# Example usage
# text_with_accents = "François café España"
# stripped_text = strip_accents(text_with_accents)
# print(f"Original: {text_with_accents}")
# print(f"Stripped: {stripped_text}")