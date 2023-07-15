from flask import Flask, request, jsonify
import json


def create_app():
    app = Flask(__name__)

    @app.route('/exchane_rate', methods=['GET'])
    def exchane_rate():

        source = request.args.get('source')
        target = request.args.get('target')
        amount = request.args.get('amount')

        # 檢查必填參數
        if not all([source, target, amount]):
            return jsonify({"error": "Missing parameters"})

        # 檢查參數格式
        try:
            amount = float(amount)
        except ValueError:
            return jsonify({"error": "Invalid amount"})


        rate_info = open("rate.json", "r")
        rate_info_data = json.loads(rate_info.read())
        rate_info.close()

        # 檢查幣別是否存在
        if source not in rate_info_data['currencies'] or target not in rate_info_data['currencies'][source]:
            return jsonify({"error": "Invalid source or target currency"})

        #執行匯率計算
        target_rate = rate_info_data['currencies'][source][target]
        calculation_results = float(target_rate) * float(amount)
        calculation_results = "{:,.2f}".format(calculation_results)
        print(rate_info_data)
        response = json.dumps({"msg": "success", "amount": calculation_results})

        return response
    return app