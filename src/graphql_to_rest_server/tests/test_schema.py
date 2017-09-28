import pytest
import requests_mock
import json

from ..schema import YourObject

your_object_1_data = {
    'id': 1,
    'name': 'YO1',
    'ignored_data': 'asdf',
    'related_object_ids': [2, 3],
}
your_object_2_data = {
    'id': 2,
    'name': 'YO2',
    'ignored_data': 'fdsa',
    'related_object_ids': [3],
}
your_object_3_data = {
    'id': 3,
    'name': 'YO3',
    'ignored_data': 'jkl;',
    'related_object_ids': [2]
}
YOUR_OBJECT_HOST = YourObject.base_url


class TestSchema:

    graphql_host = "/graphql"

    def test_related_objects(self, client):
        query = '''
        {
            yourObjects (id: "1") {
                id
                relatedObjects {
                    id
                    name
                    relatedObjects {
                        id
                        name
                    }
                }
            }
        }
        '''
        data = {'query': query}

        with requests_mock.mock() as m:
            m.get(
                '{}/?id=1'.format(YOUR_OBJECT_HOST),
                json={
                    'results': [your_object_1_data]
                })
            m.get('{}/?id=2,3'.format(YOUR_OBJECT_HOST), 
                json={
                    'results': [your_object_2_data, your_object_3_data]
                })
            response = client.post(
                self.graphql_host,
                data=json.dumps(data),
                content_type='application/json',
            )
        assert response.status_code == 200, "{} error: {}".format(
            response.status_code, response.data
        )
        json_response = json.loads(response.data.decode())
        assert 'errors' not in json_response
        object_1 = json_response['data']['yourObjects'][0]
        assert object_1['id'] == str(your_object_1_data['id'])
        object_2 = object_1['relatedObjects'][0]
        assert object_2['name'] == your_object_2_data['name']
        assert len(object_2['relatedObjects']) == 1
