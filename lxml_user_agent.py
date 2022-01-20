import requests

from lxml.html import fromstring

USER_AGENT = 'Your User_Agent'


def user_agent(url):
    """
        if you using user_agent()

        Args
            url (str): url for crawling

        Returns
            doc (lxml.html.HtmlElement): returns the content of the response
    """
    headers = {
        'User-Agent': USER_AGENT
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response.encoding = 'utf-8-sig'
        doc = fromstring(response.text)
        return doc
    except Exception as error:
        print(error)

        return None


if __name__ == '__main__':
    url = "site_url"

    doc = user_agent(url)

    text = doc.xpath('xpath/text()')

    print(text)