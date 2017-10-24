from django.db import models
# Create your models here.


class Server(models.Model):
    name = models.CharField(max_length=200, unique=True)
    shortcuts = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name


class Project(models.Model):

    server = models.ForeignKey(Server, on_delete=models.CASCADE, db_constraint=False)
    supported = models.BooleanField(default=False)
    network_id = models.IntegerField(default='1')
    name_ru = models.CharField(max_length=200, null=True)
    name_en = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name_ru

    def return_supported(self):
        return self.name_ru if self.supported == 1 else None

class Server_connection_info(models.Model):
    server = models.OneToOneField(Server, on_delete=models.CASCADE, unique=True, primary_key=True, db_constraint=False)
    host = models.CharField(max_length=200)
    host2 = models.CharField(max_length=200, null=True)
    port = models.PositiveSmallIntegerField(null=True)
    vpn = models.GenericIPAddressField(protocol='IPv4', null=True)
    dns = models.CharField(max_length=200, null=True)
    url = models.URLField()
    url2 = models.URLField(null=True)
    send_to_address = models.GenericIPAddressField(protocol='IPv4')
    send_to_port = models.PositiveSmallIntegerField(null=True)
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    stream_path = models.FilePathField(allow_files=False, allow_folders=True, null=True)
    report_path = models.FilePathField(allow_files=False, allow_folders=True, null=True)
    db_login = models.CharField(max_length=200, null=True)
    db_password = models.CharField(max_length=200,null=True)
    db_port = models.PositiveSmallIntegerField(null=True)
    db_name = models.CharField(max_length=200, null=True)
    db_host = models.GenericIPAddressField(protocol='IPv4', null=True)
    encryptPK = models.CharField(max_length=200, null=True)
    encryptLK = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.server

class Project_info(models.Model):
    prj = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='prj_id', unique=True, primary_key=True, db_constraint=False)
    # image = models.ImageField()
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.prj