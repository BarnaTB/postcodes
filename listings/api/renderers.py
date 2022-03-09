from rest_framework_xml.renderers import XMLRenderer


class ListingRenderer(XMLRenderer):
    root_tag_name = "outcode"
