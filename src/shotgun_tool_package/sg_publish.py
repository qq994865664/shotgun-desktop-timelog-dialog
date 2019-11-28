# -*- coding: utf-8 -*-

import os
import sg_base_find


class ShotgunPublish(sg_base_find.ShotgunBaseFind):

    def __init__(self):
        super(ShotgunPublish, self).__init__()

    # create version
    def create_version(self, version_name, description, dict_data, file_link_type, file_path, tags=None,
                       version_status='rev'):
        '''
        create version function
        :param file_link_type: 'upload' or 'local'
        :param file_path: Full path to an existing non-empty file on disk to upload
        :param version_name: Version name
        :param description: This version description
        :param dict_data: The Project struct dict, create a dict_data from create_project_struct function
        :param tags: Tags name
        :param version_status: The default state of this version at creation time
        :return: Created info result
        '''

        # ignore version name
        if dict_data['project']['asset']['step']['task']['version']['name']:
            dict_data['project']['asset']['step']['task']['version']['name'] = None
        elif dict_data['project']['sequence']['shot']['step']['task']['version']['name']:
            dict_data['project']['sequence']['shot']['step']['task']['version']['name'] = None
        elif dict_data['project']['sequence']['step']['task']['version']['name']:
            dict_data['project']['sequence']['step']['task']['version']['name'] = None
        project_entity, user_entity, link_entity, task_entity, version_entity = self.project_struct_parse(dict_data)

        file_name = os.path.basename(file_path)
        url = 'file://' + file_path

        tags_entity = None
        if tags:
            tags_entity = self.get_tags(tags)
            if not tags_entity:
                raise Exception('Not find the tags from server database: ', tags)

        if tags_entity:
            if file_link_type == 'upload':
                data = {'project': project_entity,
                        'code': version_name,
                        'description': description,
                        'created_by': user_entity,
                        'user': user_entity,
                        'sg_status_list': version_status,
                        'entity': link_entity,
                        'sg_task': task_entity,
                        'tags': [tags_entity],
                        'sg_src_path': file_path
                        }
            else:
                data = {'project': project_entity,
                        'code': version_name,
                        'description': description,
                        'created_by': user_entity,
                        'user': user_entity,
                        'sg_status_list': version_status,
                        'entity': link_entity,
                        'sg_task': task_entity,
                        'tags': [tags_entity],
                        'sg_src_path': file_path,
                        'sg_uploaded_movie': {
                            'link_type': 'local',
                            'local_path': file_path,
                            'local_path_linux': None,
                            'local_path_mac': None,
                            'local_path_windows': file_path,
                            'name': file_name,
                            'type': 'Attachment',
                            'url': url
                        }
                        }
        else:
            if file_link_type == 'upload':
                data = {'project': project_entity,
                        'code': version_name,
                        'description': description,
                        'created_by': user_entity,
                        'user': user_entity,
                        'sg_status_list': version_status,
                        'entity': link_entity,
                        'sg_task': task_entity,
                        'sg_src_path': file_path
                        }
            else:
                data = {'project': project_entity,
                        'code': version_name,
                        'description': description,
                        'created_by': user_entity,
                        'user': user_entity,
                        'sg_status_list': version_status,
                        'entity': link_entity,
                        'sg_task': task_entity,
                        'sg_src_path': file_path,
                        'sg_uploaded_movie': {
                            'link_type': 'local',
                            'local_path': file_path,
                            'local_path_linux': None,
                            'local_path_mac': None,
                            'local_path_windows': file_path,
                            'name': file_name,
                            'type': 'Attachment',
                            'url': url
                        }
                        }

        result_create = self.create('Version', data)
        result_upload = None
        if file_link_type == 'upload':
            # upload file and attacher to 'Versions'
            result_upload = self.upload("Version", result_create['id'], file_path, field_name="sg_uploaded_movie")
        return result_create, result_upload, True

    # publish file
    def create_publishes_file(self, file_link_type, file_path, description, dict_data, tags=None,
                              thumbnail_local_path=None, status='wtg'):
        '''
        publish file to shotgun server
        :param file_link_type: 'upload' or 'local'
        :param file_path: File path
        :param description: File description
        :param dict_data: dict_data which create by 'create_project_struct' function
        :param tags: Tags name
        :param thumbnail_local_path: Thumbnail path
        :param status: Default status for the publish file
        :return: The publish info result
        '''
        project_entity, user_entity, link_entity, task_entity, version_entity = self.project_struct_parse(dict_data)
        tags_entity = None
        if tags:
            tags_entity = self.get_tags(tags)
            if not tags_entity:
                raise Exception('Not find the tags from server database: ', tags)

        publish_file_name = os.path.basename(file_path)
        url = 'file://' + file_path
        if tags_entity:
            if file_link_type == 'upload':
                data = {'project': project_entity,
                        'code': publish_file_name,
                        'description': description,
                        'created_by': user_entity,
                        'image': thumbnail_local_path,
                        'sg_status_list': status,
                        'entity': link_entity,
                        'task': task_entity,
                        'version': version_entity,
                        'tags': [tags_entity],
                        'sg_src_path': file_path
                        }
            else:
                data = {'project': project_entity,
                        'code': publish_file_name,
                        'description': description,
                        'created_by': user_entity,
                        'image': thumbnail_local_path,
                        'path': {
                            'link_type': 'local',
                            'local_path': file_path,
                            'local_path_linux': None,
                            'local_path_mac': None,
                            'local_path_windows': file_path,
                            'name': publish_file_name,
                            'type': 'Attachment',
                            'url': url
                        },
                        'sg_status_list': status,
                        'entity': link_entity,
                        'task': task_entity,
                        'version': version_entity,
                        'tags': [tags_entity],
                        'sg_src_path': file_path
                        }
        else:
            if file_link_type == 'upload':
                data = {'project': project_entity,
                        'code': publish_file_name,
                        'description': description,
                        'created_by': user_entity,
                        'image': thumbnail_local_path,
                        'sg_status_list': status,
                        'entity': link_entity,
                        'task': task_entity,
                        'version': version_entity,
                        'sg_src_path': file_path
                        }
            else:
                data = {'project': project_entity,
                        'code': publish_file_name,
                        'description': description,
                        'created_by': user_entity,
                        'image': thumbnail_local_path,
                        'sg_status_list': status,
                        'entity': link_entity,
                        'task': task_entity,
                        'version': version_entity,
                        'sg_src_path': file_path,
                        'path': {
                            'link_type': 'local',
                            'local_path': file_path,
                            'local_path_linux': None,
                            'local_path_mac': None,
                            'local_path_windows': file_path,
                            'name': publish_file_name,
                            'type': 'Attachment',
                            'url': url
                        }
                        }

        result_publish_file = self.create("PublishedFile", data)
        result_upload = None
        if file_link_type == 'upload':
            # upload file and attacher to 'Publish file'
            result_upload = self.upload("PublishedFile", result_publish_file['id'], file_path, field_name="path")
        return result_publish_file, result_upload, True

    # read the publish file from shotgun database
    def get_published_file_list(self, dict_data, tags=None, pulished_file_type=None):
        '''
        read publish file info list from shotgun database
        :param dict_data: dict_data which create by 'create_project_struct' function
        :param tags: Tags name
        :param pulished_file_type: File type
        :return: The publish file info list
        '''
        project_entity, user_entity, link_entity, task_entity, version_entity = self.project_struct_parse(dict_data)
        tags_entity = None
        if tags:
            tags_entity = self.get_tags(tags)
            if not tags_entity:
                raise Exception('Not find the tags from server database: ', tags)
        if version_entity:
            if tags_entity:
                filters = [
                    ['project', 'is', project_entity],
                    ['entity', 'is', link_entity],
                    ['task', 'is', task_entity],
                    ['version', 'is', version_entity],
                    ['tags', 'is', tags_entity]
                ]
            else:
                filters = [
                    ['project', 'is', project_entity],
                    ['entity', 'is', link_entity],
                    ['task', 'is', task_entity],
                    ['version', 'is', version_entity]
                ]
        else:
            if tags_entity:
                filters = [
                    ['project', 'is', project_entity],
                    ['entity', 'is', link_entity],
                    ['task', 'is', task_entity],
                    ['tags', 'is', tags_entity]
                ]
            else:
                filters = [
                    ['project', 'is', project_entity],
                    ['entity', 'is', link_entity],
                    ['task', 'is', task_entity]
                ]
        fields = ["code", "description", "tags", "version", "sg_src_path"]
        return self.find("PublishedFile", filters, fields)

    # read the version from shotgun database
    def get_version_list(self, dict_data, tags=None):
        '''
        read version info list from shotgun database
        :param dict_data: dict_data which create by 'create_project_struct' function
        :param tags: Tags name
        :return: The version info list
        '''

        # ignore version name
        if dict_data['project']['asset']['step']['task']['version']['name']:
            dict_data['project']['asset']['step']['task']['version']['name'] = None
        elif dict_data['project']['sequence']['shot']['step']['task']['version']['name']:
            dict_data['project']['sequence']['shot']['step']['task']['version']['name'] = None
        elif dict_data['project']['sequence']['step']['task']['version']['name']:
            dict_data['project']['sequence']['step']['task']['version']['name'] = None

        project_entity, user_entity, link_entity, task_entity, version_entity = self.project_struct_parse(dict_data)
        tags_entity = None
        if tags:
            tags_entity = self.get_tags(tags)
            if not tags_entity:
                raise Exception('Not find the tags from server database: ', tags)

        if tags_entity:
            filters = [
                ['project', 'is', project_entity],
                ['entity', 'is', link_entity],
                ['sg_task', 'is', task_entity],
                ['tags', 'is', tags_entity]
            ]
        else:
            filters = [
                ['project', 'is', project_entity],
                ['entity', 'is', link_entity],
                ['sg_task', 'is', task_entity]
            ]
        fields = ["code", "description", "tags", "sg_src_path"]
        return self.find("Version", filters, fields)

    def get_task_status(self, dict_data):
        project_entity, user_entity, link_entity, task_entity, version_entity = self.project_struct_parse(dict_data)
        filters = [
            ['project', 'is', project_entity],
            ['entity', 'is', link_entity],
            ['id', 'is', task_entity['id']]
        ]
        fields = ["content", "sg_status_list"]
        return self.find_one("Task", filters, fields)

    def create_time_log(self, date, duration, dict_data, description=None):
        project_entity, user_entity, link_entity, task_entity, version_entity = self.project_struct_parse(dict_data)
        data = {'project': project_entity,
                'updated_by': user_entity,
                'created_by': user_entity,
                'user': user_entity,
                'description': description,
                'date': date,
                'entity': task_entity,
                'duration': duration
                }
        result_create = self.create('TimeLog', data)
        return result_create

    def get_time_log(self, dict_data):
        project_entity, user_entity, link_entity, task_entity, version_entity = self.project_struct_parse(dict_data)
        filters = [
            ['project', 'is', project_entity],
            ['entity', 'is', task_entity],
            ['user', 'is', user_entity]
        ]
        fields = ["user", "date", "duration", "description", "id"]
        return self.find("TimeLog", filters, fields)
