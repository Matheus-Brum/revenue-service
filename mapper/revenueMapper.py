from api.models.revenueModel import RevenueModel


class RevenueMapper:

    def to_model(self, revenue_entity) -> RevenueModel:
        revenue_model: RevenueModel = RevenueModel()
        if revenue_entity:
            revenue_model.id = revenue_entity["Id"]
            revenue_model.user_id = revenue_entity["RevenueUserId"]
            revenue_model.category = revenue_entity["Category"]
            revenue_model.name = revenue_entity["Name"]
            revenue_model.amount = revenue_entity["Amount"]
        return revenue_model

    def to_entity(self):
        pass
