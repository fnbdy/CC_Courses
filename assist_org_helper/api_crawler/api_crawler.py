from re import L
from typing import Optional
import requests
from requests.models import Response


class API_URLS:
    API_VARS = {
        '<institution_id>': '',
        '<r_institution_id>': '',
        '<s_institution_id>': '',
        '<academic_year_id>': '',
        '<category_code>': '',
    }

    ACADEMIC_YEARS = 'https://assist.org/api/AcademicYears'
    APP_SETTINGS = 'https://assist.org/api/appsettings'
    INSTITUTIONS = 'https://assist.org/api/institutions'
    AGREEMENTS_OV = 'https://assist.org/api/institutions/<institution_id>/agreements'
    AGREEMENTS = 'https://assist.org/api/agreements?receivingInstitutionId=<r_institution_id>&sendingInstitutionId=<s_institution_id>&academicYearId=<academic_year_id>&categoryCode=<category_code>'

    def get_url(self, url, **kwargs):
        for key in self.API_VARS:
            if kwargs.get('key', None):
                self.API_VARS[key] = kwargs[key]

            if key in url and not self.API_VARS[key]:
                print('Insufficient Parameters!')
                return False

            url = url.replace(key, self.API_VARS[key])
        return url


def get_response(url: str, headers: dict = {}, timeout=5) -> Response:
    try:
        r = requests.get(url, headers=headers, timeout=timeout)
    except Exception as e:
        print(f'Request failed,{e}')
        return False

    if r.status_code != 200:
        print(f'Request failed,{r}')
        return False

    return r


def get_json_from_api(url: str, headers: dict = {}, timeout=5):
    r = get_response(url, headers=headers, timeout=timeout)

    if not r:
        return False

    return r.json()
