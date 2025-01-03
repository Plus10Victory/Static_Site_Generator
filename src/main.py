from copy_static import delete_public_files, copy_files_to_dst, check_for_path
from textnode import TextType, TextNode
from generate import generate_page


def main():
    public_dir = "./public"
    static_dir = "./static"
    print("Deleting public directory...")
    check_for_path(public_dir)
    delete_public_files(public_dir)
    print("Copying static files to the public directory...")
    copy_files_to_dst(static_dir, public_dir)

    content_path = "./content/index.md"
    template_path = "./template.html"
    dest_path = "public/index.html"
    generate_page(content_path, template_path, dest_path)





    







main()
