from validators.commonValidator import CommonValidator
from api.models.revenueModel import RevenueModel


class RevenueModelValidator:

    @staticmethod
    def validate_revenue_model(revenue_model: RevenueModel) -> bool:
        return not CommonValidator.is_none(revenue_model) and not CommonValidator.is_empty(revenue_model) and \
                not CommonValidator.is_none(revenue_model.id) and not CommonValidator.is_none(revenue_model.user_id) and \
                not CommonValidator.is_none(revenue_model.category) and not CommonValidator.is_none(revenue_model.name) and \
                not CommonValidator.is_none(revenue_model.amount) and not CommonValidator.is_empty(revenue_model.id) and \
                not CommonValidator.is_empty(revenue_model.user_id) and not CommonValidator.is_empty(revenue_model.category) and \
                not CommonValidator.is_empty(revenue_model.name) and not CommonValidator.is_empty(revenue_model.amount) and \
                CommonValidator.validate_id(revenue_model.id) and CommonValidator.validate_id(revenue_model.user_id) and \
                CommonValidator.validate_string(revenue_model.category, 1, 128) and CommonValidator.validate_string(revenue_model.name, 1, 128) and \
                CommonValidator.validate_number(revenue_model.amount)
