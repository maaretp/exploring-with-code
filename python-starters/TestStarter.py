import requests
from approvaltests.approvals import verify
import bs4

class TestStarter():

    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_maaretp(self):
        response = requests.get("https://maaretp.com")
        assert response.status_code == 200
        verify(response.text)

    def test_h3(self):
        url = "https://maaretp.com"
        html = requests.get(url).text
        soup = bs4.BeautifulSoup(html, "html.parser")
        this = soup.find('h3').get_text()
        verify(this)