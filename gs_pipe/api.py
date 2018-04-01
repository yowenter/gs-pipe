from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

from gs_pipe.controller import list_mod, create_task, get_task

app = Flask(__name__)
api = Api(app)


class Task(Resource):

    def get(self, task_id):
        return get_task(task_id)


class TaskList(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('input_argument', type=list,
                            location='json', required=True)
        parser.add_argument('pipeline', type=list,
                            location='json', required=True)
        args = parser.parse_args()

        print(args)
        task = create_task(args['input_argument'], args['pipeline'])

        return task

    def get(self):
        #todo 
        return []


class ModList(Resource):
    def get(self):
        #todo
        return list_mod()



api.add_resource(Task, '/task/<string:task_id>')
api.add_resource(TaskList, '/task')
api.add_resource(ModList, '/admin/mods')




if __name__ == '__main__':
    app.run(debug=True)
