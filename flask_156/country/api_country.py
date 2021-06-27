from flask_restx import Namespace, Resource, fields

api = Namespace('country', description='Countrys related operations')

country = api.model('country', {
    'id': fields.String(readonly=True, description='The task unique identifier'),
    'name': fields.String(required=True, description='The task details'),
    "totalCases": fields.Integer(),
    "totalDeaths": fields.Integer()
})

COUNTRIES = [
        {
            "id": "1",
            "name": "Usa",
            "totalCases": 124565,
            "totalDeaths": 161156,
        },
        {
            "id": "2",
            "name": "Udddsa",
            "totalCases": 124565,
            "totalDeaths": 161156,
            
        },
        {
            "id": "3",
            "name": "brasil",
            "totalCases": 15545465,
            "totalDeaths": 1616,
            
        },
        
    ]

@api.route('/')
class CountryList(Resource):
    @api.doc('list_countries')
    @api.marshal_list_with(country)
    def get(self):
        '''List all countries'''
        return COUNTRIES


@api.route('/<id>')
@api.param('id', 'The Country identifier')
@api.response(404, 'Country not found')
class Country(Resource):
    @api.doc('get_country')
    @api.marshal_with(country)
    def get(self, id):
        '''Fetch a Country given its identifier'''
        for country in COUNTRIES:
            if country['id'] == id:
                return country
        api.abort(404)