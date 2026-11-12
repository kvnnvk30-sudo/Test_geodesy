from config import BASE
import pytest
import requests



@pytest.fixture(scope='session')
def get():
    ses = requests.Session()
    def _get(params=None, url=BASE, **kwargs):
        return ses.get(url, params=params, **kwargs)
    return _get


@pytest.fixture(scope='module')
def api(get):
    r = get(params={'api': 'data'})
    assert r.status_code == 200
    assert 'application/json' in r.headers['Content-Type']
    return r.json()
