import codecs
import os
from os import listdir
from jinja2 import Environment, FileSystemLoader
from src.jsonclass import JsonClass
from src.layers.javalayer import JavaClassLayer
from src.layers.markdownlayer import MarkdownClassLayer
from src.layers.phplayer import PhpClassLayer
from src.layers.swiftlayer import SwiftClassLayer
import json

java_template = None
java_package = "com.example.test"
php_template = None
markdown_template = None
swift_template = None

env = None

java_classes ={}


def _apply_function_to_each(dir, function, **kwargs):
    """
    Apply fuction to each file in source_dir
    """
    for f in listdir(dir):
        file_path = os.path.join(os.path.abspath(dir), f)
        function(file_path, **kwargs)


def _generate(file_path):
    print("Processing %s" % file_path)
    json_class = JsonClass(file_path)
    java_class = JavaClassLayer(json_class, java_package,'jsons')
    java_classes[java_class.name()]=java_class
    php_class = PhpClassLayer(json_class)
    swift_class = SwiftClassLayer(json_class)
    markdown_class = MarkdownClassLayer(json_class, php_template.render(class_=php_class),
                                        java_template.render(class_=java_class),'jsons')
    _render_and_write(class_=java_class, template=java_template, target_dir='generated/java', extension='java')
    _render_and_write(class_=php_class, template=php_template, target_dir='generated/php', extension='php')
    _render_and_write(class_=markdown_class, template=markdown_template, target_dir='generated/docs', extension='md')
    _render_and_write(class_=swift_class, template=swift_template, target_dir='generated/swift', extension='swift')

    target_flat_file = os.path.join('generated/flat_jsons','{0}.{1}'.format(json_class.json_name, '.json'))
    # Wrting new data to target file
    with codecs.open(target_flat_file, 'w','utf-8') as f:
        json.dump(obj=json_class.get_flat_json_data(),ensure_ascii=False,fp=f,sort_keys="True",indent=4)

def _render_and_write(class_, template, target_dir, extension):
    string_out = template.render(class_=class_)
    target_path = os.path.join(target_dir, '{0}.{1}'.format(class_.name(), extension))
    with codecs.open(target_path, 'w', 'utf-8') as f:
        f.write(string_out)


def generate_yaml(dir, target_path):
    """
    generate yml for mkdocs
    """
    res = []
    for f in listdir(dir):
        res.append(f.replace('.md', ''))
    ytemplate = env.get_template('mkdoc_yaml_template.yaml')
    string_out = ytemplate.render(files=res)
    with codecs.open(target_path, 'w', 'utf-8') as f:
        f.write(string_out)

def generate_graph(target_path):
    """
    generate yml for mkdocs
    """

    ytemplate = env.get_template('graph_template.dot')
    string_out = ytemplate.render(classes=java_classes)
    with codecs.open(target_path, 'w', 'utf-8') as f:
        f.write(string_out)


if __name__ == '__main__':
    env = Environment(loader=FileSystemLoader("../src/templates"), trim_blocks=True)
    markdown_template = env.get_template('markdown_template.md')
    java_template = env.get_template('java_template.java')
    php_template = env.get_template('php_template.php')
    swift_template = env.get_template('swift_template.swift')

    _apply_function_to_each('jsons', _generate)
   # generate_yaml('generated/docs', 'generated/mkdocs.yml')
    generate_graph('generated/class_diagram.dot')
