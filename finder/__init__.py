import os


def get_all_files(root_path):
    # print('\nnow at dir:', root_path)
    if os.path.isdir(root_path):
        __dir_files = os.listdir(root_path)
        __dirs = []
        __files = []
        for file in __dir_files:
            path = root_path + os.sep + file
            if os.path.isdir(path):
                if file == '##reps':
                    continue
                __dirs.append(path)
            else:
                __files.append(path)

        # print('dirs', __dirs)
        # print('files', __files)

        for __dir in __dirs:
            __files += get_all_files(__dir)
        return __files


def get_all_file_each(root_path):
    # print('\n', '@', root_path)
    # using os.walk
    for root_dir, dirs, files in os.walk(root_path):
        # yield files in root path first
        # print('@files', root_path, files)
        for file in files:
            yield root_path + os.sep + file

        # print('@dirs', root_path, dirs)
        for dir in dirs:
            if dir == '##reps':
                continue
            for sub_file in get_all_file_each(root_path + os.sep + dir):
                yield sub_file

        break
#
#
# for file in get_all_file_each(r'E:\rep'):
#     print(file)
