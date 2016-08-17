import logging

logger = logging.getLogger(__name__)


class ManifestBase(dict):
    def __init__(self):
        super(ManifestBase, self).__init__()

    @property
    def resources(self):
        return self.get("resources", [])

    @property
    def deploy(self):
        return self.get("deploy", [])

    @property
    def variables(self):
        return self.get("variables", {})

    @property
    def package(self):
        return self.get("package", {})

    @property
    def shards(self):
        return self.get("shards", [])

    def kubname(self):
        sp = self.package['name'].split('/')
        name = "%s_%s" % (sp[0], sp[1])
        return name

    def package_name(self):
        package = ("%s_%s" % (self.kubname(), self.package['version']))
        return package
