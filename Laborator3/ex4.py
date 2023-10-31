def build_xml_element(tag,content,**args):
    xml_element=f"<{tag}"
    for key,element in args.items():
         xml_element += f' {key}="{element}"'
    xml_element+=f">{content}</{tag}>"
    return xml_element

rez= build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(rez)