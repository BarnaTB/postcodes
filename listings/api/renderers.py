from rest_framework_xml.renderers import XMLRenderer


class OutcodeRenderer(XMLRenderer):
    root_tag_name = "outcode"

class OutcodesRenderer(XMLRenderer):
    root_tag_name = "outcodes"
    item_tag_name = "outcode"
