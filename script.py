#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Para correr este script, es necesario tener en la misma carpeta donde se encuentra
    este archivo, el archivo de groups.json, el cual contiene los groups de django
    que han sido creadas para una aplicacion, y el archivo de users.json, el cual
    contiene los usuarios.

    La forma de obtener estos archivos es desde la CLI con el comando:
    - ./manage.py dumpdata auth.User --indent=4 > users.json
    - ./manage.py dumpdata auth.Group --indent=4 > users.json

    El objetivo de este archivo solo es migrar la base de datos de mysql a postgresql
"""
import os
import sys
import django
import json
import io

DB_NAME = 'postgres'


class ControlException(Exception):
    pass


def get_json(filename):
    bufferer = io.BytesIO()

    with open(filename) as json_file:
        for line in json_file.readlines():
            bufferer.write(line)
    JSON_FILE = json.loads(bufferer.getvalue())
    return JSON_FILE

def load_groups_data():
    from django.contrib.auth.models import Permission, Group

    JSON_GROUPS = get_json('./groups.json')

    for group in JSON_GROUPS:
        try:
            modifier = Group.objects.using(DB_NAME).get(pk=group['pk'])
            if 'fields' in group:
                for field in group['fields']:
                    if isinstance(group['fields'][field], list):
                        for pk in group['fields'][field]:
                            try:
                                permission = Permission.objects.using(DB_NAME).get(pk=pk)
                                modifier.permissions.add(permission)
                            except Permission.DoesNotExist:
                                raise ValueError(
                                    'El permiso con el id {} no fue encontrado en la base de datos `{}`'.format(pk, DB_NAME)
                                )
                            except Exception as exception:
                                raise ControlException(exception)
                    else:
                        setattr(modifier, field, group['fields'][field])
            modifier.save()
            print('Insercion de {} exitosa'.format(modifier))
        except Group.DoesNotExist:
            raise ValueError(
                'No fue encontrado el grupo con el id {} en la base de datos `{}`'.format(group['pk'], DB_NAME)
            )
        except Exception as exception:
            raise ControlException(exception)


def load_users_data():
    from django.contrib.auth.models import User, Group

    JSON_USERS = get_json('./users.json')
    NON_MIGRATE_FIELDS = (
        'password', 'last_login', 'is_superuser',
        'is_active', 'is_staff', 'user_permissions',
        'date_joined'
    )
    for user in JSON_USERS:
        try:
            modifier = User.objects.using(DB_NAME).get(pk=user['pk'])
            if 'fields' in user:
                for field in user['fields']:
                    if isinstance(user['fields'][field], list) and field not in NON_MIGRATE_FIELDS:
                        for pk in user['fields'][field]:
                            try:
                                group = Group.objects.using(DB_NAME).get(pk=pk)
                                modifier.groups.add(group)
                            except Group.DoesNotExist:
                                raise ValueError(
                                    'No fue encontrado el grupo con el id {} en la base de datos `{}`'.format(pk, DB_NAME)
                                )
                            except Exception as exception:
                                raise ControlException(exception)
                    elif field not in NON_MIGRATE_FIELDS:
                        setattr(modifier, field, user['fields'][field])
            modifier.save()
            print('Insercion de {} exitosa'.format(modifier))
        except User.DoesNotExist:
            raise ValueError(
                'No fue encontrado el usuario con el id {} en la base de datos `{}`'.format(user['pk'], DB_NAME)
            )
        except Exception as exception:
            raise ControlException(exception)

if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    django.setup()
    from django.db import transaction
    try:
        transaction.atomic(load_groups_data)()
        transaction.atomic(load_users_data)()
    except Exception as exception:
        print(exception)
