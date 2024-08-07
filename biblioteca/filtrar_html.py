from bs4 import BeautifulSoup as bs

def limpar_html_sem_imagem(html_content):
    soup = bs(html_content, 'html.parser')
    # Remove CSS (style tags)
    for style in soup.find_all('style'):
        style.decompose()
    # Remove scripts (script tags)
    for script in soup.find_all('script'):
        script.decompose()
    # Remove inline styles
    for tag in soup.find_all(True):
        tag.attrs = {key: value for key, value in tag.attrs.items() if key not in ['style', 'class']}
    # Remove specific elements: img, video, audio, iframe
    for tag in soup.find_all(['img', 'video', 'audio', 'iframe']):
        tag.decompose()

    return soup.prettify()[:25000]

def limpar_html_com_imagem(html_content):
    soup = bs(html_content, 'html.parser')
    # Remove CSS (style tags)
    for style in soup.find_all('style'):
        style.decompose()
    # Remove scripts (script tags)
    for script in soup.find_all('script'):
        script.decompose()
    # Remove inline styles
    for tag in soup.find_all(True):
        tag.attrs = {key: value for key, value in tag.attrs.items() if key not in ['class']}
    # Remove specific elements: img, video, audio, iframe
    for tag in soup.find_all(['video', 'audio', 'iframe']):
        tag.decompose()

    return soup
    # return soup.prettify()[:25000]

# def limpar_html_caractere(html_content):
#     soup = bs(html_content, 'html.parser')
#     # Remove CSS (style tags)
#     for style in soup.find_all('style'):
#         style.decompose()
#     # Remove scripts (script tags)
#     for script in soup.find_all('script'):
#         script.decompose()
#     # Remove inline styles
#     for tag in soup.find_all(True):
#         tag.attrs = {key: value for key, value in tag.attrs.items() if key not in ['style', 'class']}
#     # Remove specific elements: img, video, audio, iframe
#     for tag in soup.find_all(['img', 'video', 'audio', 'iframe']):
#         tag.decompose()
#
#     return soup.prettify()[:25000]