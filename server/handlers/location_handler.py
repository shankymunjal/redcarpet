from flask_restful import Resource

class LocationHandler(Resource):
    def get(self):
    	return "get locations"
        # if template_id:
        #     response = fetch('/accounts/%s/templates/%s' % (account_id, template_id), {}, "GET", 200)
        #     return json.loads(response.body)
        # else:
        #     query_string = request.query_string
        #     response = fetch('/accounts/%s/templates?%s' %(account_id, query_string), {}, "GET", 200)
        #     return json.loads(response.body)
