import os

from Stock import DynamicLoadStrategyFields


# dynamically load strategies from Stock/Trade/Strategy
__pathList = os.path.dirname(__file__).split(os.path.sep)
__stratgyPath = os.path.sep.join(__pathList[:-2] + ['Strategy'])

DyStockTradeStrategyWidgetAutoFields = DynamicLoadStrategyFields(__stratgyPath, 'Stock.Trade.Strategy')
