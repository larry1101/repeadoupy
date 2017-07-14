import hashlib


class Detector:
    def __init__(self):
        pass

    @staticmethod
    def sha1(file_path):
        __hash = None
        with open(file_path, 'rb') as f:
            sha1obj = hashlib.sha1()
            sha1obj.update(f.read())
            __hash = sha1obj.hexdigest()
        return __hash

    @staticmethod
    def md5(file_path):
        __hash = None
        with open(file_path, 'rb') as f:
            md5obj = hashlib.md5()
            md5obj.update(f.read())
            __hash = md5obj.hexdigest()
        return __hash

    @staticmethod
    def sha512(file_path):
        __hash = None
        with open(file_path, 'rb') as f:
            sha512obj = hashlib.sha512()
            sha512obj.update(f.read())
            __hash = sha512obj.hexdigest()
        return __hash

    def compare(self, file1path, file2path, method = None):
        if method is None:
            method = self.md5
        return method(file1path) == method(file2path)


# det = Detector()
# f1 = r'E:\rep\1.jpg'
# f1_1 = r'E:\rep\1\1.jpg'
# f2 = r'E:\rep\2.jpg'
# print(det.compare(f1,f1))
# print(det.compare(f1,f1_1))
# print(det.compare(f1,f1_1,Detector.sha1))
# print(det.compare(f1,f2))
