import os

import shutil

from finder import get_all_files, get_all_file_each
from repeat_detector.detector import Detector

# ==============================================================================
# ========================= replace path here ==================================
# ==============================================================================

root_path = r''

# ==============================================================================
# ==============================================================================
# ==============================================================================

def derep_all(_root_path):
    if not os.path.exists(_root_path):
        raise Exception('root path not exists')

    repath = _root_path + os.sep + '##reps'

    if not os.path.exists(repath):
        os.mkdir(repath)
        print('rep dir made\n')

    files = get_all_files(_root_path)  # 希望可以以generator形式来迭代
    print('all files paths got\n', files.__len__(), 'in total\nStarting to traversal')

    file_hashes = {}

    f_hash = None

    for file in files:
        f_hash = Detector.sha512(file)
        if f_hash not in file_hashes:
            file_hashes[f_hash] = file
            # print('\t\tNew file:',file)
        else:
            print(file, '\nrep:', file_hashes[f_hash])
            # 把重复的文件移动到统一文件夹里，到时候检查后删掉

            ori_name = file_hashes[f_hash]
            ori_name = ori_name[ori_name.rfind('\\') + 1:]
            rep_name = file[file.rfind('\\') + 1:]
            rep_ext_name = rep_name[rep_name.rfind('.'):]
            rep_name = rep_name[:rep_name.rfind('.')]

            rep_file_dir = repath + os.sep + ori_name + '.dir'

            if not os.path.exists(rep_file_dir):
                os.mkdir(rep_file_dir)
                if os.path.getsize(file_hashes[f_hash]) > 50906920:
                    with open(rep_file_dir + os.sep + ori_name + '.txt', 'w') as f:
                        f.write('ori = ' + file_hashes[f_hash] + '\n')
                else:
                    shutil.copy(file_hashes[f_hash], rep_file_dir + os.sep + ori_name)

            if os.path.getsize(file_hashes[f_hash]) > 50906920:
                with open(rep_file_dir + os.sep + ori_name + '.txt', 'a') as f:
                    f.write('rep = ' + file + '\n')
            else:
                shutil.move(file,
                            rep_file_dir + os.sep + rep_name + (
                                '_%d' % (os.listdir(rep_file_dir).__len__() + 1)) + rep_ext_name)


def derep_each(_root_path, move_file_max_size=50906920, delete_rep_file=False):
    if not os.path.exists(_root_path):
        raise Exception('root path not exists')

    print('Starting to traversal with generator...\n')

    file_hashes = {}

    f_hash = None

    for file in get_all_file_each(_root_path):
        f_hash = Detector.sha512(file)
        if f_hash not in file_hashes:
            file_hashes[f_hash] = file
            # print('\t\tNew file:',file)
        else:

            ori_name = file_hashes[f_hash]
            ori_name = ori_name[ori_name.rfind('\\') + 1:]
            rep_name = file[file.rfind('\\') + 1:]

            if delete_rep_file:
                # 检查文件名
                if ori_name != rep_name:
                    # 检查文件大小
                    if os.path.getsize(file_hashes[f_hash]) == os.path.getsize(file):
                        # delete file of the same size with diff names
                        print('delete file:', file, '\n\t\trep:', file_hashes[f_hash])
                        if os.path.exists(file):
                            os.remove(file)
                else:
                    # delete file of the same name
                    print('delete file:', file, '\n\t\trep:', file_hashes[f_hash])
                    if os.path.exists(file):
                        os.remove(file)

                pass
            else:
                # 把重复的文件移动到统一文件夹里，到时候检查后删掉

                repath = _root_path + os.sep + '##reps'

                if not os.path.exists(repath):
                    os.mkdir(repath)
                    print('rep dir made\n')

                print('\t', file, '\nrep:', file_hashes[f_hash])
                rep_ext_name = rep_name[rep_name.rfind('.'):]
                rep_name = rep_name[:rep_name.rfind('.')]

                rep_file_dir = repath + os.sep + ori_name + '.dir'

                if not os.path.exists(rep_file_dir):
                    os.mkdir(rep_file_dir)
                    if os.path.getsize(file_hashes[f_hash]) > move_file_max_size:
                        with open(rep_file_dir + os.sep + ori_name + '.txt', 'w') as f:
                            f.write('ori = ' + file_hashes[f_hash] + '\n')
                    else:
                        shutil.copy(file_hashes[f_hash], rep_file_dir + os.sep + ori_name)

                if os.path.getsize(file_hashes[f_hash]) > move_file_max_size:
                    with open(rep_file_dir + os.sep + ori_name + '.txt', 'a') as f:
                        f.write('rep = ' + file + '\n')
                else:
                    shutil.move(file,
                                rep_file_dir + os.sep + rep_name + (
                                    '_%d' % (os.listdir(rep_file_dir).__len__() + 1)) + rep_ext_name)
    print('\ntraversal finished')


derep_each(root_path, 102400000, True)
