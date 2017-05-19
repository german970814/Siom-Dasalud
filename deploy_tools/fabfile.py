from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run


REPO_URL = 'https://german970814@bitbucket.org/ingeniarte/ipsiom.git'
FOLDER_ROOT = 'dasaludsiom'
STRUCTURE_PROJECT = ('static', 'source', 'media', )
ACTUAL_BRANCH = 'feature/laboratorio'

env.user = 'tecno'
env.hosts = 'dasaludsiom.tecno.webfactional.com'

def deploy():
    site_folder = 'home/%s/webapps/%s' % (env.user, FOLDER_ROOT)
    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_virtualenv(env.user, env.host, source_folder)
    # _update_static_files(source_folder, env.user, env.host)
    # update_database_info(source_folder)


def _create_directory_structure_if_necessary(site_folder):
    for subfolder in STRUCTURE_PROJECT:
        run('mkdir -p %s/%s' % (site_folder, subfolder))


def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):
        run('cd %s && git fetch' % (source_folder,))
    else:
        run('git clone %s %s' % (REPO_URL, source_folder))
    current_commit = local('git log origin/{} -n 1 --format=%H'.format(ACTUAL_BRANCH), capture=True)
    run('cd %s && git reset --hard %s' % (source_folder, current_commit))


def _update_settings(source_folder, site_name):
    settings_path = source_folder + '/mysite/settings.py'
    sed(settings_path, 'ALLOWED_HOSTS =.+$', 'ALLOWED_HOSTS = ["%s"]' % (site_name,))


def _update_virtualenv(user, site_name, source_folder):
    virtualenv_folder = '/home/%s/.envs/siom' % (user,)
    if not exists(virtualenv_folder + '/bin/pip'):
        run('virtualenv --python=python2.7 %s' % (virtualenv_folder,))
    run('%s/bin/pip install -r %s/requirements.txt' % (virtualenv_folder, source_folder))


def _update_static_files(source_folder, user, site_name):
    run('cd %s && /home/%s/.envs/siom/bin/python manage.py collectstatic --noinput' % (source_folder, user))


def _update_database(source_folder, user, site_name):
    run('cd %s && /home/%s/.envs/siom/bin/python manage.py migrate --noinput' % (source_folder, user))
