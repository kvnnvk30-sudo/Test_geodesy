import re
from markers import *


@T01
def test_t01_page_html(get):
    """Сторінка відкривається (HTML, до 10 с)"""
    r = get()
    assert r.status_code == 200, f'статус {r.status_code}'
    assert 'accounts.google.com' not in r.url, 'редірект на вхід Google'
    assert 'text/html' in r.headers['Content-Type'], r.headers['Content-Type']
    assert r.elapsed.total_seconds() < 10, f'відповідь {r.elapsed.total_seconds():.1f} с'


@T02
def test_t02_no_config_error(get):
    """Сторінка без помилки конфігурації"""
    text = get().text
    assert 'Вкажіть SPREADSHEET_ID_' not in text, 'не задано ID таблиці'
    assert 'Script function not found' not in text, 'немає функції doGet'


@T03
def test_t03_xss_not_reflected(get):
    """XSS: сторонній параметр не відбивається"""
    payload = '<script>alert(1)</script>'
    assert payload not in get({'x': payload}).text, 'параметр відбито в HTML'


@T04
def test_t04_api_json(get):
    """API віддає JSON"""
    r = get({'api': 'data'})
    assert r.status_code == 200, f'статус {r.status_code}'
    assert 'application/json' in r.headers['Content-Type'], r.headers['Content-Type']


@T05
def test_t05_no_error(api):
    """API: немає помилки (аркуші знайдено)"""
    assert 'error' not in api, api.get('error')


@T06
def test_t06_pgz_lines(api):
    """Схема ходу: є лінії з аркуша"""
    assert len(api['pgz']['lines']) >= 1, 'масив pgz.lines порожній'


@T07
def test_t07_line_d_positive(api):
    """Схема ходу: довжина лінії d > 0"""
    d = api['pgz']['lines'][0]['d']
    assert d > 0, f'd = {d}'


@T08
def test_t08_niv(api):
    """Нівелювання: є секції"""
    assert len(api['niv']) >= 1, 'масив niv порожній'


@T09
def test_t09_net_p_positive(api):
    """Точність мереж: периметр P > 0"""
    p = api['net'][0]['P']
    assert p > 0, f'P = {p}'


@T10
def test_t10_ngo_array(api):
    """НГО: записи — масив"""
    assert isinstance(api['ngo'], list), f'тип {type(api["ngo"]).__name__}'


@T11
def test_t11_fresh_version(get):
    """Оновлення даних: &fresh=1 дає версію v"""
    v = get({'api': 'data', 'fresh': 1}).json()['v']
    assert re.fullmatch(r'[0-9a-f]{12}', v), f'v = {v!r}'


@T12
def test_t12_unknown_api_error(get):
    """Невідомий api → поле error"""
    data = get({'api': 'nonsense'}).json()
    assert 'error' in data, f'відповідь без error: {data}'