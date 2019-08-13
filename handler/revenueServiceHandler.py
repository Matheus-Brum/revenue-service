from flask_restful import Resource
from flask import jsonify, abort, make_response, request
from uuid import uuid4
from api.models.revenueModel import RevenueModel
from database.revenueDAO import RevenueDAO
from mapper.revenueMapper import RevenueMapper
from validators.commonValidator import CommonValidator
from validators.revenueModelValidator import RevenueModelValidator


class Revenues(Resource):

    def __init__(self):
        self.revenueDAO: RevenueDAO = RevenueDAO()
        self.revenue_mapper: RevenueMapper = RevenueMapper()

    def get(self):
        if request.args.get('user_id'):
            user_id = request.args.get('user_id')
            user_revenues = self.revenueDAO.retrieve_user_revenues(user_id)
            if user_revenues:
                return make_response(jsonify([self.revenue_mapper.to_model(revenue_entity).serialize()
                                              for revenue_entity in user_revenues]), 200)
            abort(404)
        else:
            return [self.revenue_mapper.to_model(revenue_entity).serialize()
                    for revenue_entity in self.revenueDAO.retrieve_revenues()]
        abort(404)

    def post(self):
        new_revenue: RevenueModel = RevenueModel()
        new_revenue.id = str(uuid4())
        new_revenue.user_id = request.json['userId']
        new_revenue.category = request.json['category']
        new_revenue.name = request.json['name']
        new_revenue.amount = request.json['amount']
        if RevenueModelValidator.validate_revenue_model(new_revenue):
            is_revenue_added: bool = self.revenueDAO.add_revenue(new_revenue)
            if is_revenue_added:
                return make_response(jsonify(new_revenue.serialize()), 201)
            print('unexpected error occurred.')
            abort(500)
        print('invalid revenue model.')
        abort(400)


class Revenue(Resource):

    def __init__(self):
        self.revenueDAO: RevenueDAO = RevenueDAO()
        self.revenue_mapper: RevenueMapper = RevenueMapper()

    def get(self, revenue_id: str):
        if not CommonValidator.is_none(revenue_id) and CommonValidator.validate_id(revenue_id):
            revenue_entity = self.revenueDAO.retrieve_revenue(revenue_id)
            if revenue_entity:
                return make_response(jsonify(self.revenue_mapper.to_model(revenue_entity).serialize()), 200)
            print('no revenue found.')
            abort(404)
        print('invalid revenue id.')
        abort(400)

    def delete(self, revenue_id: str):
        if not CommonValidator.is_none(revenue_id) and CommonValidator.validate_id(revenue_id):
            revenue_entity = self.revenueDAO.retrieve_revenue(revenue_id)
            if revenue_entity:
                is_revenue_removed: bool = self.revenueDAO.remove_revenue(revenue_id)
                if is_revenue_removed:
                    return make_response(jsonify(self.revenue_mapper.to_model(revenue_entity).serialize()), 200)
                print('unexpected error occurred.')
                abort(500)
            print('no revenue found.')
            abort(404)
        print('invalid revenue id.')
        abort(400)

    def put(self, revenue_id: str):
        print('invalid revenue id or revenue model.')
        abort(400)
        pass
