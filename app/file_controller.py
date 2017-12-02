from app import app
import base64
import db
from flask import request, Response
import http_const
import json
import mimetypes

def file_controller_post(new_file_name, new_file_content):
	new_file_id = db.db_execute("INSERT INTO file VALUES (null, ?, ?, 0)", (new_file_name, new_file_content))
	response_body = {
		'response': {
			'status': 'OK',
			'file': {
				'id': new_file_id,
				'file_name': new_file_name,
				'path': '/file/%s/%s' % (new_file_id, new_file_name)
			}
		}
	}
	return json.dumps(response_body), http_const.HTTP_CREATED

def file_controller_get_all():
	db_result =	db.db_select(
		'SELECT id, file_name FROM file WHERE deleted = 0',
		()
	)

	file_list = []
	for row in db_result:
		file_list.append(
			{
				'id': row[0],
				'file_name': row[1],
				'path': '/file/%s/%s' % (row[0], row[1])
			}
		)

	response_body = {
		'response': {
			'status': 'OK',
			'count': len(file_list),
			'files': file_list
		}
	}
	return json.dumps(response_body), http_const.HTTP_OK

def file_controller_get(file_id):
	db_result =	db.db_select(
		'SELECT file_name FROM file WHERE id = ? AND deleted = 0',
		(file_id,),
		True
	)

	if db_result:
		response_body = {
			'response': {
				'status': 'OK',
				'file': {
					'id': file_id,
					'file_name': db_result[0],
					'path': '/file/%s/%s' % (file_id, db_result[0])
				}
			}
		}
		return json.dumps(response_body), http_const.HTTP_OK
	return json.dumps({'response':{'status':'error'}}), http_const.HTTP_NOT_FOUND

def file_controller_put(file_id, file_name, file_content):
	db_result =	db.db_select(
		'SELECT count(*) FROM file WHERE id = ? AND deleted = 0',
		(file_id,),
		True
	)
	if db_result[0] == 0:
		return json.dumps({'response':{'status':'error'}}), http_const.HTTP_NOT_FOUND

	db.db_execute("UPDATE file SET file_name = ?, file_content_b64 = ? WHERE id = ?", (file_name, file_content, file_id))
	response_body = {
		'response': {
			'status': 'OK',
			'file': {
				'id': file_id,
				'file_name': file_name,
				'path': '/file/%s/%s' % (file_id, file_name)
			}
		}
	}
	return json.dumps(response_body), http_const.HTTP_OK

def file_controller_delete(file_id):
	db.db_execute("UPDATE file SET deleted = 1 WHERE id = ?", (file_id,))
	response_body = {
		'response': {
			'status': 'OK'
		}
	}
	return json.dumps(response_body), http_const.HTTP_OK

@app.route('/file', methods=['GET', 'POST'])
def handle_file_no_id():
	if request.method == 'POST':
		json_payload = request.get_json(force=True)
		return file_controller_post(json_payload['file_name'], json_payload['content'])
	elif request.method == 'GET':
		return file_controller_get_all()

@app.route('/file/<int:file_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_file_with_id(file_id):
	if request.method == 'DELETE':
		return file_controller_delete(file_id)
	elif request.method == 'GET':
		return file_controller_get(file_id)
	elif request.method == 'PUT':
		json_payload = request.get_json(force=True)
		return file_controller_put(file_id, json_payload['file_name'], json_payload['content'])

@app.route('/file/<int:file_id>/<file_name>')
def file_server_route(file_id, file_name):
	result = db.db_select(
		'SELECT file_content_b64 FROM file WHERE id = ? AND file_name = ? AND deleted = 0',
		(file_id, file_name),
		True
	)

	if result:
		mime_type = mimetypes.guess_type(file_name)[0]
		r = Response(
			response=base64.b64decode(result[0]),
			status=http_const.HTTP_OK,
			mimetype=mime_type
		)
		r.headers["Content-Type"] = mime_type
		return r
	return Response(
		response='',
		status=http_const.HTTP_NOT_FOUND
	)
