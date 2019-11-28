# -*- coding: utf-8 -*-

import sg_config


# this function will create a struct dict for project
def create_project_struct(project_name, user_name, link_type, asset_name=None, asset_step_name=None,
                          asset_step_task_name=None, asset_step_task_version_name=None, sequence_name=None,
                          sequence_step_name=None, sequence_step_task_name=None, sequence_step_task_version_name=None,
                          sequence_shot_name=None, sequence_shot_step_name=None, sequence_shot_step_task_name=None,
                          sequence_shot_step_task_version_name=None):
    '''
    :param project_name: Input you project name
    :param user_name: It will be show in create_by field
    :param link_type: Witch entity type do you link, only one you can selected in (asset|shot|sequence)
    :param asset_name: If you choose link 'asset' entity, you need select asset name in you project(link_type: 'asset')
    :param asset_step_name: Step name below you asset next lower level
    :param asset_step_task_name: You asset task
    :param asset_step_task_version_name: You version in asset(If create_version, please let it empty)
    :param sequence_name:If you choose link 'sequence' or 'shot' entity, you need select sequence name in you project(link_type: 'sequence' or 'shot')
    :param sequence_step_name: If you want to link in 'sequence' entity, get you step name in here
    :param sequence_step_task_name: Task name here in 'sequence'
    :param sequence_step_task_version_name: Version name here in 'sequence' task(If create_version, please let it empty)
    :param sequence_shot_name: Shot name
    :param sequence_shot_step_name: Step in shot
    :param sequence_shot_step_task_name: Task in shot
    :param sequence_shot_step_task_version_name: Version in shot
    :return: Return a shotgun project struct dict
    '''

    dict_data = {"user": user_name,
                 "link_type": link_type,
                 "project": {"name": project_name,
                             "asset": {"name": asset_name,
                                       "step": {"name": asset_step_name,
                                                "task": {"name": asset_step_task_name,
                                                         "version": {"name": asset_step_task_version_name}
                                                         }
                                                }
                                       },

                             "sequence": {"name": sequence_name,
                                          "shot": {"name": sequence_shot_name,
                                                   "step": {"name": sequence_shot_step_name,
                                                            "task": {"name": sequence_shot_step_task_name,
                                                                     "version": {
                                                                         "name": sequence_shot_step_task_version_name}
                                                                     }
                                                            }
                                                   },
                                          "step": {"name": sequence_step_name,
                                                   "task": {"name": sequence_step_task_name,
                                                            "version": {
                                                                "name": sequence_step_task_version_name}
                                                            }
                                                   }
                                          }
                             }
                 }

    return dict_data


class ShotgunBaseFind(object):

    def __init__(self):
        self._config = sg_config.Config()
        self._sg = self._config.login()

    def find(self, entity_type, filters, fields=None, order=None, filter_operator=None, limit=0,
             retired_only=False, page=0, include_archived_projects=True, additional_filter_presets=None):
        '''
        call shotgun find function
        :param entity_type:
        :param filters:
        :param fields:
        :param order:
        :param filter_operator:
        :param limit:
        :param retired_only:
        :param page:
        :param include_archived_projects:
        :param additional_filter_presets:
        :return: find result
        '''
        return self._sg.find(entity_type, filters, fields, order, filter_operator, limit, retired_only, page,
                             include_archived_projects, additional_filter_presets)

    def find_one(self, entity_type, filters, fields=None, order=None, filter_operator=None, retired_only=False,
                 include_archived_projects=True, additional_filter_presets=None):
        '''
        call shotgun find_one function
        :param entity_type:
        :param filters:
        :param fields:
        :param order:
        :param filter_operator:
        :param retired_only:
        :param include_archived_projects:
        :param additional_filter_presets:
        :return: find result
        '''
        return self._sg.find_one(entity_type, filters, fields, order, filter_operator, retired_only,
                                 include_archived_projects, additional_filter_presets)

    def get_project(self, project_name):
        '''
        read a project entity
        :param project_name: Project name
        :return: Project entity
        '''
        entity = "Project"
        filters = [
            ['name', 'is', project_name]
        ]
        return self._sg.find_one(entity, filters)

    def get_asset_list(self, project_name, asset_type=None, limiter=0):
        '''
        read asset entity list
        :param project_name: Project name
        :param asset_type: Asset type(character, environment, prop etc...)
        :param limiter: Max search item, default is unlimit
        :return: Asset entity list
        '''
        entity = "Asset"
        filters = [
            ['project.Project.name', 'is', project_name],
            ['sg_asset_type', 'is', asset_type]
        ]
        field = ["id", "type", "code", "sg_chinesename"]
        return self._sg.find(entity, filters, field, limit=limiter)

    def get_asset_entity(self, project_name, asset_name):
        '''
        read asset entity
        :param project_name: Project name
        :param asset_name: Asset name which you want to get
        :return: Asset entity
        '''
        filters = [
            ['project.Project.name', 'is', project_name],
            ['code', 'is', asset_name]
        ]
        return self._sg.find_one("Asset", filters)

    def get_asset_entity2(self, project_name, asset_name):
        '''
        read asset entity2 using project name
        :param project_name: Project name
        :param asset_name: Asset name which you want to get
        :return: Asset entity
        '''
        filters = [
            ['project.Project.name', 'is', project_name],
            ['code', 'is', asset_name]
        ]
        fields = ["id", "type", "code", "sg_chinesename", "sg_asset_type"]
        return self._sg.find_one("Asset", filters, fields)

    def get_user(self, user_name):
        '''
        read user from shotgun database
        :param user_name: Your user name in the shotgun
        :return: User entity
        '''
        filters = [
            ['login', 'is', user_name]
        ]
        return self._sg.find_one("HumanUser", filters)

    def get_tags(self, tags_name):
        '''
        read tags entity
        :param tags_name: Tags name
        :return: Tags entity
        '''
        filters = [
            ['name', 'is', tags_name]
        ]
        return self._sg.find_one("Tag", filters)

    def get_step_entity_list(self, entity_type):
        '''
        read step entity list
        :param entity_type: One of the (Asset|Shot|Sequence)
        :return: step list of the entity type
        '''
        filters = [
            ['entity_type', 'is', entity_type]
        ]
        fields = ["id", "type", "code"]
        return self._sg.find("Step", filters, fields)

    def upload_thumbnail(self, entity_type, entity_id, file_path):
        '''
        upload thumbnail for entity
        :param entity_type: Entity type, can be one of the (Asset|Shot|Sequence|Version etc...)
        :param entity_id: The entity id
        :param file_path: File path on you local path which you want to upload, supported image file types include .jpg` and ``.png
        :return: Upload result
        '''
        result = self._sg.upload_thumbnail(entity_type, entity_id, file_path)
        return result

    def get_asset_version(self, project_name, asset_name, version_name):
        '''
        read version of the asset entity
        :param project_name: Project name
        :param asset_name: Asset name
        :param version_name: Version name
        :return: Asset version entity
        '''
        filters = [
            ['project.Project.name', 'is', project_name],
            ['entity.Asset.code', 'is', asset_name],
            ['code', 'is', version_name]
        ]
        return self._sg.find_one("Version", filters)

    def get_asset_task(self, project_name, asset_name, step_name, task_name):
        '''
        read asset task entity
        :param project_name: Project name
        :param asset_name: Asset name
        :param step_name: Step name of the asset
        :param task_name: Task name of the asset
        :return: Asset task entity
        '''
        filters = [
            ['project.Project.name', 'is', project_name],
            ['entity.Asset.code', 'is', asset_name],
            ['step.Step.code', 'is', step_name],
            ['content', 'is', task_name]
        ]
        return self._sg.find_one("Task", filters)

    def get_asset_task_list(self, project_name, asset_name, step_name=None):
        '''
        read asset task entity list
        :param project_name: Project name
        :param asset_name: Asset entity
        :param step_name: Step name of the asset
        :return: Asset task list entity
        '''
        if not step_name:
            filters = [
                ['project.Project.name', 'is', project_name],
                ['entity.Asset.code', 'is', asset_name]
            ]
        else:
            filters = [
                ['project.Project.name', 'is', project_name],
                ['entity.Asset.code', 'is', asset_name],
                ['step.Step.code', 'is', step_name]
            ]
        fields = ['content', 'step']
        return self._sg.find("Task", filters, fields)

    def get_asset_task_version(self, project_name, asset_name, version_name):
        '''
        read asset task version entity
        :param project_name: Project name
        :param asset_name: Asset name
        :param version_name: Version name of the asset
        :return: Asset version entity
        '''
        filters = [
            ['project.Project.name', 'is', project_name],
            ['sg_task.Task.entity.Asset.code', 'is', asset_name],
            ['code', 'is', version_name]
        ]
        return self._sg.find_one("Version", filters)

    def get_asset_task_step(self, project_name, asset_name, task_name):
        '''
        read asset task step entity
        :param project_name: Project name
        :param asset_name: Asset name
        :param task_name: Task name of the asset
        :return: Asset step entity
        '''
        filters = [
            ['project.Project.name', 'is', project_name],
            ['entity.Asset.code', 'is', asset_name],
            ['content', 'is', task_name]
        ]
        fields = ['step']
        return self._sg.find("Task", filters, fields)

    def get_mytask_list(self, project_name, assigned_to):
        '''
        read mytask entity list
        :param project_name: Project name
        :param assigned_to: User name who assigned to
        :return: Mytask entity list
        '''
        filters = [
            ['project.Project.name', 'is', project_name],
            ['task_assignees.HumanUser.login', 'is', assigned_to]
        ]
        fields = ['content', 'entity', 'step']
        return self._sg.find("Task", filters, fields)

    def get_sequence_list(self, project_name, limiter=0):
        '''
        read sequence entity list
        :param project_name: Project name
        :param limiter: Max read number for the sequence entity
        :return: Sequence entity list
        '''
        filters = [
            ['project.Project.name', 'is', project_name]
        ]
        fields = ["id", "type", "code"]
        return self._sg.find("Sequence", filters, fields, limit=limiter)

    def get_sequence_entity(self, project_name, sequence_name):
        '''
        read sequence entity
        :param project_name: Project name
        :param sequence_name: Sequence name
        :return: Sequence entity
        '''
        filters = [
            ['project.Project.name', 'is', project_name],
            ['code', 'is', sequence_name]
        ]
        return self._sg.find_one("Sequence", filters)

    def get_sequence_task(self, project_name, sequence_name, step_name, task_name):
        '''
        read sequence task entity
        :param project_name: Project name
        :param sequence_name: Sequence name
        :param step_name: Step name of the sequence
        :param task_name: Task name of the sequence
        :return: Sequence task entity
        '''
        filters = [
            ['project.Project.name', 'is', project_name],
            ['entity.Sequence.code', 'is', sequence_name],
            ['step.Step.code', 'is', step_name],
            ['content', 'is', task_name]
        ]
        return self._sg.find_one("Task", filters)

    def get_sequence_task_list(self, project_name, sequence_name, step_name=None):
        '''
        read sequence task entity list
        :param project_name: Project name
        :param sequence_name: Sequence name
        :param step_name: Step name of the sequence
        :return: Sequence task entity list
        '''
        if not step_name:
            filters = [
                ['project.Project.name', 'is', project_name],
                ['entity.Sequence.code', 'is', sequence_name]
            ]
        else:
            filters = [
                ['project.Project.name', 'is', project_name],
                ['entity.Sequence.code', 'is', sequence_name],
                ['step.Step.code', 'is', step_name]
            ]
        fields = ["id", "type", "content", "step"]
        return self._sg.find("Task", filters, fields)

    def get_sequence_task_version(self, project_name, sequence_name, version_name):
        '''
        read sequence task version entity
        :param project_name: Project name
        :param sequence_name: Sequence name
        :param version_name: Version name of the sequence
        :return: Version entity of the sequence
        '''
        filters = [
            ['project.Project.name', 'is', project_name],
            ['sg_task.Task.entity.Sequence.code', 'is', sequence_name],
            ['code', 'is', version_name]
        ]
        return self._sg.find_one("Version", filters)

    def get_sequence_shot(self, project_name, sequence_name, shot_name):
        '''
        read shot entity
        :param project_name: Project name
        :param sequence_name: Sequence name
        :param shot_name: Shot name
        :return: Shot entity
        '''
        filters = [
            ['project.Project.name', 'is', project_name],
            ['sg_sequence.Sequence.code', 'is', sequence_name],
            ['code', 'is', shot_name]
        ]
        fields = ["id", "type", "code"]
        return self._sg.find_one("Shot", filters, fields)

    def get_sequence_shot_list(self, project_name, sequence_name, limiter=0):
        '''
        read shot entity list
        :param project_name: Project name
        :param sequence_name: Sequence name
        :param limiter: Limit num for list
        :return: Shot entity list
        '''
        filters = [
            ['project.Project.name', 'is', project_name],
            ['sg_sequence.Sequence.code', 'is', sequence_name]
        ]
        fields = ["id", "type", "code"]
        return self._sg.find("Shot", filters, fields, limit=limiter)

    def get_sequence_shot_version(self, project_name, shot_name, version_name):
        '''
        read shot version eneity
        :param project_name: Project name
        :param shot_name: Shot name
        :param version_name: Version name of the shot
        :return: Version entity for the shot
        '''
        filters = [
            ['project.Project.name', 'is', project_name],
            ['entity.Shot.code', 'is', shot_name],
            ['code', 'is', version_name]
        ]
        return self._sg.find_one("Version", filters)

    def get_sequence_shot_task(self, project_name, shot_name, step_name, task_name):
        '''
        read shot task entity
        :param project_name: Project name
        :param shot_name: Shot name
        :param step_name: Step name of the shot
        :param task_name: Task name of the shot
        :return: Task entity for the shot
        '''
        filters = [
            ['project.Project.name', 'is', project_name],
            ['entity.Shot.code', 'is', shot_name],
            ['step.Step.code', 'is', step_name],
            ['content', 'is', task_name]
        ]
        return self._sg.find_one("Task", filters)

    def get_sequence_shot_task_list(self, project_name, sequence_name, shot_name, step_name=None):
        '''
        read shot task entity list
        :param project_name: Project name
        :param sequence_name: Sequence name
        :param shot_name: Shot name
        :param step_name: Step name of the shot
        :return: Task entity list
        '''
        if not step_name:
            filters = [
                ['project.Project.name', 'is', project_name],
                ['entity.Shot.sg_sequence.Sequence.code', 'is', sequence_name],
                ['entity.Shot.code', 'is', shot_name]
            ]
        else:
            filters = [
                ['project.Project.name', 'is', project_name],
                ['entity.Shot.sg_sequence.Sequence.code', 'is', sequence_name],
                ['entity.Shot.code', 'is', shot_name],
                ['step.Step.code', 'is', step_name]
            ]
        fields = ["id", "type", "content", "step"]
        return self._sg.find("Task", filters, fields)

    def get_sequence_shot_task_version(self, project_name, shot_name, version_name):
        '''
        read shot version entity
        :param project_name: Project name
        :param shot_name: Shot name
        :param version_name: Version name of the shot
        :return: Version entity
        '''
        filters = [
            ['project.Project.name', 'is', project_name],
            ['sg_task.Task.entity.Shot.code', 'is', shot_name],
            ['code', 'is', version_name]
        ]
        return self._sg.find_one("Version", filters)

    def create(self, entity_type, data, return_fields=None):
        '''
        call shotgun create function
        :param entity_type:
        :param data:
        :param return_fields:
        :return: create info result
        '''
        return self._sg.create(entity_type, data, return_fields)

    def upload(self, entity_type, entity_id, path, field_name=None, display_name=None, tag_list=None):
        '''
        :param entity_type: Entity type to link the upload to.
        :param entity_id: Id of the entity to link the upload to.
        :param path: Full path to an existing non-empty file on disk to upload.
        :param field_name: The internal Shotgun field name on the entity to store the file in.
        :param display_name: The display name to use for the file. Defaults to the file name.
        :param tag_list: comma-separated string of tags to assign to the file.
        :return: Upload status
        '''
        self._sg.upload(entity_type, entity_id, path, field_name, display_name, tag_list)

    def project_struct_parse(self, dict_data):
        '''
        parse the struct of dict_data
        :param dict_data: dict_data which create by 'create_project_struct' function
        :return: multi entity
        '''
        # parse from dict
        project = dict_data['project']
        link_type = dict_data['link_type']
        user = dict_data['user']
        link_entity = None
        task_entity = None
        version_entity = None

        # begin get entity
        # read project entity
        project_name = project['name']
        project_entity = self.get_project(project_name)
        if not project_entity:
            raise Exception('Not find the project name from server database: ', project_name)
        # read user entity
        user_entity = self.get_user(user)
        if not user_entity:
            raise Exception('Not find the user name from server database: ', user)
        # read link entity
        if link_type == 'asset':
            # read asset entity
            asset_name = project['asset']['name']
            if asset_name:
                link_entity = self.get_asset_entity(project_name, asset_name)
                if not link_entity:
                    raise Exception('Not find the asset name from server database: ', asset_name)

            # read task entity
            asset_step_name = project['asset']['step']['name']
            asset_step_task_name = project['asset']['step']['task']['name']
            if asset_step_task_name and asset_step_name:
                task_entity = self.get_asset_task(project_name, asset_name, asset_step_name, asset_step_task_name)
                if not task_entity:
                    raise Exception('Not find the asset task name from server database: ', asset_step_task_name)

            # read asset task version entity
            asset_step_task_version_name = project['asset']['step']['task']['version']['name']
            if asset_step_task_version_name:
                version_entity = self.get_asset_task_version(project_name, asset_name, asset_step_task_version_name)
                if not version_entity:
                    raise Exception('Not find the asset task version name from server database: ',
                                    asset_step_task_version_name)

        elif link_type == 'shot':
            # read sequence entity
            sequence_name = project['sequence']['name']
            if sequence_name:
                sequence_entity = self.get_sequence_entity(project_name, sequence_name)
                if not sequence_entity:
                    raise Exception('Not find the sequence name from server database: ', sequence_name)

            # read link entity
            sequence_shot_name = project['sequence']['shot']['name']
            if sequence_shot_name:
                link_entity = self.get_sequence_shot(project_name, sequence_name, sequence_shot_name)
                if not link_entity:
                    raise Exception('Not find the sequence shot name from server database: ', sequence_shot_name)

            # read sequence shot task
            sequence_shot_step_name = project['sequence']['shot']['step']['name']
            sequence_shot_step_task_name = project['sequence']['shot']['step']['task']['name']
            if sequence_shot_step_task_name:
                task_entity = self.get_sequence_shot_task(project_name, sequence_shot_name, sequence_shot_step_name,
                                                          sequence_shot_step_task_name)
                if not task_entity:
                    raise Exception('Not find the sequence shot task name from server database: ',
                                    sequence_shot_step_task_name)

            # read sequence shot task version
            sequence_shot_step_task_version_name = project['sequence']['shot']['step']['task']['version']['name']
            if sequence_shot_step_task_version_name:
                version_entity = self.get_sequence_shot_task_version(project_name, sequence_shot_name,
                                                                     sequence_shot_step_task_version_name)
                if not version_entity:
                    raise Exception('Not find the sequence shot task version name from server database: ',
                                    sequence_shot_step_task_version_name)

        elif link_type == 'sequence':
            # read sequence entity and link entity
            sequence_name = project['sequence']['name']
            if sequence_name:
                sequence_entity = self.get_sequence_entity(project_name, sequence_name)
                if not sequence_entity:
                    raise Exception('Not find the sequence name from server database: ', sequence_name)
                else:
                    link_entity = sequence_entity

            # read sequence task
            sequence_step_name = project['sequence']['step']['name']
            sequence_step_task_name = project['sequence']['step']['task']['name']
            if sequence_step_task_name:
                task_entity = self.get_sequence_task(project_name, sequence_name, sequence_step_name,
                                                     sequence_step_task_name)
                if not task_entity:
                    raise Exception('Not find the sequence task name from server database: ',
                                    sequence_step_task_name)

            # read sequence task version
            sequence_step_task_version_name = project['sequence']['step']['task']['version']['name']
            if sequence_step_task_version_name:
                version_entity = self.get_sequence_task_version(project_name, sequence_name,
                                                                sequence_step_task_version_name)
                if not version_entity:
                    raise Exception('Not find the sequence task version name from server database: ',
                                    sequence_step_task_version_name)

        return project_entity, user_entity, link_entity, task_entity, version_entity

    def get_shot_assets_list(self, project_name, shot_name):
        '''
        Get the asset list link below the shot entity
        :param project_name: Project name
        :param shot_name: Shot name
        :return: Asset list
        '''
        filters = [
            ['shot.Shot.project.Project.name', 'is', project_name],
            ['shot.Shot.code', 'is', shot_name]
        ]
        fields = ['asset.Asset.sg_asset_type', 'asset.Asset.code', 'asset.Asset.sg_chinesename', 'asset.Asset.image',
                  'asset.Asset.sg_published_files']
        return self._sg.find("AssetShotConnection", filters, fields)

    def get_published_file_src_path(self, project_name, published_file_id):
        '''
        get published file source path
        :param project_name: Project name
        :param published_file_id: Published file id
        :return: File source path
        '''
        filters = [
            ['project.Project.name', 'is', project_name],
            ['id', 'is', published_file_id]
        ]
        fields = ['code', 'sg_src_path', 'version']
        return self._sg.find_one("PublishedFile", filters, fields)

    def delete(self, entity_type, entity_id):
        '''
        shotgun delete api
        :param entity_type: Shotgun entity type to delete.
        :param entity_id: ``id`` of the entity to delete.
        :return: ``True`` if the entity was deleted, ``False`` otherwise (for example, if the
            entity was already deleted).
        '''
        return self._sg.delete(entity_type, entity_id)

    def test(self):
        # return self._sg.schema_field_read("TimeLog")
        # filters = [
        #     # ['project.Project.name', 'is', 'XCM_Test'],
        #     ['shot.Shot.code', 'is', 'seq005_sc001']
        # ]
        # fields = ['asset.Asset.sg_asset_type', 'asset.Asset.code', 'asset.Asset.sg_chinesename', 'asset.Asset.image']
        # return self._sg.find("AssetShotConnection", filters, fields)
        filters = [
            ['project.Project.name', 'is', "XCM_Test"],
            ['id', 'is', 7]
        ]
        fields = ['user', 'entity', 'duration']
        return self.find_one("TimeLog", filters, fields)
