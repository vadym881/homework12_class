'hw_12.1'
import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    clean_text = []
    in_tag = False
    for char in html:
        if char == '<':
            in_tag = True
        elif char == '>':
            in_tag = False
        elif not in_tag:
            clean_text.append(char)

    clean_text = ''.join(clean_text)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(clean_text)

    with codecs.open(result_file, 'r', 'utf-8') as file:
        text = file.read()
        return text

draft_file = r'..\homework12_class\draft.html'
print(delete_html_tags(draft_file))