try:
    from unidecode import unidecode
except ImportError:
    try:
        from .unidecode import unidecode
    except ImportError:
        raise ImportError("The 'unidecode' library is required for this plugin to function. Please install it via pip.")

try:
    from bs4 import BeautifulSoup
    from css_html_js_minify import html_minify
except ImportError:
    try:
        from included_dependencies.bs4 import BeautifulSoup
        from included_dependencies.css_html_js_minify import html_minify
    except ImportError as ie:
           print(f"The 'bs4' and 'css_html_js_minify' libraries are required for this plugin to function. Please install them via pip.")
           raise ie

def strip_accents(text: str) -> str:
    """
    Removes accents and diacritics from a string.
    """
    return unidecode(text)


def minify_html_content(html_content: str) -> str:
    """
    Minifies HTML content by removing unnecessary whitespace and comments.
    """
    return html_minify(html_content)


def prettify_html_content(html_content: str, parser: str = "html.parser") -> str:
    """
    Prettifies HTML content using BeautifulSoup.
    """
    soup = BeautifulSoup(html_content, parser)
    return soup.prettify()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Strip accents from a string.")
    parser.add_argument("--minify", action="store_true", help="Minify HTML content.")
    parser.add_argument("--prettify", action="store_true", help="Prettify HTML content.")
    parser.add_argument("input_file", type=str, help="Path to the input file.")
    args = parser.parse_args()

    COMMAND = "minify" if args.minify else "prettify" if args.prettify else "dezalgo"

    with open(args.input_file, "r", encoding="utf-8") as f:
        text = f.read()

    if COMMAND == "minify":
        result = minify_html_content(text)
    elif COMMAND == "prettify":
        result = prettify_html_content(text)
    else:
        result = strip_accents(text)
    print(result)

# Example usage
# text_with_accents = "François café España"
# stripped_text = strip_accents(text_with_accents)
# print(f"Original: {text_with_accents}")
# print(f"Stripped: {stripped_text}")