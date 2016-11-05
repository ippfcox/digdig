#!usr/bin/python



class ManagePath:
    dir_prj = 'E:\\Self\\Python\\Project\\digdig\\' 
    dir_src = dir_prj + 'src\\' 
    path_htm = dir_src + r'137.htm' 
    dir_files = dir_src + '137\\'
    path_htm_module = dir_files + 'feeds_html_module'
    
    @classmethod
    def gettargethtm(cls):
        return cls.path_htm_module

    @classmethod
    def gettargetfilesdir(cls):
        return cls.dir_files

    @classmethod
    def getprjdir(cls):
        return cls.dir_prj
