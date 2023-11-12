import os, platform, multiprocessing
from src.app_attributes import AppAttributes


if __name__ == '__main__':
    jobs = multiprocessing.cpu_count()
    print('build with %d jobs...' % jobs)

    # Config
    output_dir = 'output'
    output_name = AppAttributes.title
    windows_icon_file = 'src/assets/icon.ico'

    src_file = 'src/main.py'
    is_one_file = False

    build_cmd = ('python -m nuitka --show-progress' +
                 ' --standalone' +
                 ' --lto=no' +
                 ' --plugin-enable=tk-inter' +
                 f' --jobs={jobs:d}' +
                 f' --output-dir={output_dir}' +
                 f' -o {output_name}')

    match(platform.system()):
        case 'Windows':
            build_cmd += (' --windows-disable-console' +
                          f' --windows-icon-from-ico={windows_icon_file}')
        case 'Linux':
            pass
        case 'Darwin':
            build_cmd += ' --macos-create-app-bundle'
        case _:
            print('unknown OS')

    if is_one_file:
        build_cmd += ' --onefile'

    build_cmd += ' ' + src_file

    ret = os.popen(build_cmd)
    print(ret.read())
