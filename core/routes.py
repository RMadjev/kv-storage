from flask import request, make_response, jsonify, redirect

from .validator import validate
from storage import get_storage
from .exceptions import NoItemFound, InvalidRequest
from .utils import get_pagination


def register_routes(app):
    storage = get_storage(app.config['STORAGE'])

    @app.route('/')
    def index():
        return redirect("/docs", code=302)

    @app.route('/set', methods=['GET'])
    def set_pair():
        """
           Create new pair, update if it exists
           ---
           tags:
             - keyValue
           parameters:
             - in: query
               name: k
               required: true
               type: string
               minimum: 1
               maximum: 64
               description: The name of the key
             - in: query
               name: v
               required: true
               type: string
               minimum: 1
               maximum: 256
               description: The value for the given key
           responses:
             200:
               description: Set of key-value pairs
             400:
               description: Key or value are not set correctly
        """
        key = request.args.get('k')
        value = request.args.get('v')

        try:
            validate(key=key, value=value)
        except InvalidRequest as ex:
            return make_response(jsonify({"error": "{0}".format(ex.message)}),
                                 400)

        storage.set(key, value)

        return make_response(jsonify({"message": "OK"}), 200)

    @app.route('/get', methods=['GET'])
    def get_pair():
        """
           Get pair by key
           ---
           tags:
             - keyValue
           parameters:
             - in: query
               name: k
               required: true
               type: string
               minimum: 1
               maximum: 64
               description: The name of the key
           responses:
             200:
               description: Set of key-value pairs
             400:
               description: The key is not set correctly
             404:
               description: No value saved for the key
        """
        key = request.args.get('k')

        try:
            validate(key=key)
            value = storage.get(key)
        except InvalidRequest as ex:
            return make_response(jsonify({"error": "{0}".format(ex.message)}),
                                 400)
        except NoItemFound:
            return make_response(jsonify({
                "error": "No value stored for key: {0}".format(key)}), 404)

        return make_response(jsonify({key: value}), 200)

    @app.route('/is', methods=['GET'])
    def pair_exists():
        """
           Check if pair exists
           ---
           tags:
             - keyValue
           parameters:
             - in: query
               name: k
               required: true
               type: string
               minimum: 1
               maximum: 64
               description: The name of the key
           responses:
             200:
               description: Return True if pair exists
             400:
               description: The key is not set correctly
             404:
               description: Return False if pair doesn`t exists
        """
        key = request.args.get('k')

        try:
            validate(key=key)
            storage.get(key)
        except InvalidRequest as ex:
            return make_response(jsonify({
                "error": "{0}".format(ex.message)}), 400)
        except NoItemFound:
            return make_response(jsonify({"message": False}), 404)

        return make_response(jsonify({"message": True}), 200)

    @app.route('/rm', methods=['GET'])
    def remove_pair():
        """
           Remove a pair
           ---
           tags:
             - keyValue
           parameters:
             - in: query
               name: k
               required: true
               type: string
               minimum: 1
               maximum: 64
               description: The name of the key
           responses:
             200:
               description: Set of key-value pairs
             400:
               description: The key is not set correctly
             404:
               description: No value stored for that key
        """
        key = request.args.get('k')

        try:
            validate(key=key)
            storage.remove(key)
        except InvalidRequest as ex:
            return make_response(jsonify({
                "error": "{0}".format(ex.message)}), 400)
        except NoItemFound:
            return make_response(jsonify({
                "error": "No value stored for key: {0}".format(key)}), 404)

        return make_response(jsonify({"message": "OK"}), 200)

    @app.route('/clear', methods=['GET'])
    def remove_all_pairs():
        """
           Truncate all values from the storage
           ---
           tags:
             - keyValue
           responses:
             200:
               description: Set of key-value pairs
        """
        storage.remove_all()
        return make_response(jsonify({"message": "OK"}), 200)

    @app.route('/getKeys', methods=['GET'])
    def get_all_keys():
        """
           Get all keys
           ---
           tags:
             - keyValue
           parameters:
             - in: query
               name: page
               required: false
               type: integer
               minimum: 1
               default: 1
               description: Number of the page
             - in: query
               name: per_page
               required: false
               type: integer
               minimum: 1
               default: 10
               description: How many items to be shown on the page
           responses:
             200:
               description: Set of key-value pairs
             404:
               description: No keys stored or wrong paginating
        """
        page, per_page = get_pagination(request.args)
        try:
            data = storage.get_all_keys(page, per_page)
        except NoItemFound:
            return make_response(jsonify({"error": "No keys stored"}), 404)

        return make_response(jsonify(data), 200)

    @app.route('/getValues', methods=['GET'])
    def get_all_values():
        """
           Get all values
           ---
           tags:
             - keyValue
           parameters:
             - in: query
               name: page
               required: false
               type: integer
               minimum: 1
               default: 1
               description: Number of the page
             - in: query
               name: per_page
               required: false
               type: integer
               minimum: 1
               default: 10
               description: How many items to be shown on the page
           responses:
             200:
               description: Set of key-value pairs
             404:
               description: No values stored or wrong paginating
        """

        page, per_page = get_pagination(request.args)
        try:
            data = storage.get_all_values(page, per_page)
        except NoItemFound:
            return make_response(jsonify({"error": "No values stored"}), 404)

        return make_response(jsonify(data), 200)

    @app.route('/getAll', methods=['GET'])
    def get_all():
        """
           Get all key-value pairs
           ---
           tags:
             - keyValue
           parameters:
             - in: query
               name: page
               required: false
               type: integer
               minimum: 1
               default: 1
               description: Number of the page
             - in: query
               name: per_page
               required: false
               type: integer
               minimum: 1
               default: 10
               description: How many items to be shown on the page
           responses:
             200:
               description: Set of key-value pairs
             404:
               description: No pairs stored or wrong paginating
        """

        page, per_page = get_pagination(request.args)

        try:
            data = storage.get_all(page, per_page)
        except NoItemFound:
            return make_response(jsonify({"error": "No pairs stored"}), 404)

        return make_response(jsonify(data), 200)
